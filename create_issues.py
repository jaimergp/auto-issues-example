"""
Script to create issues with labels and milestones
from a series of Markdown files with YAML frontmatter.

The frontmatter schema is:

- title: str.
    Title of the issue.
- labels: list of str.
    Labels to assign to the issue. They will be created 
    if they don't exist.
- milestone: str.
    Name of the milestone to assign to the issue. 
    It will be created if it does not exist.

3rd party dependencies:
- requests.
- python-frontmatter.

Create a personal access token with read&write issue and pull_request
permissions in the target repo and export it as `GITHUB_PAT`.
"""
import argparse
import os
import sys
import time
import traceback
from collections import defaultdict
from functools import lru_cache

import requests
import frontmatter

try:
    GITHUB_PAT = os.environ["GITHUB_PAT"]
except KeyError:
    raise RuntimeError("Environment variable 'GITHUB_PAT' required.")

GITHUB_BASE_URL = "https://api.github.com"


def _gh_request(method, url, **kwargs):
    kwargs.setdefault("headers", {})
    kwargs["headers"].update(
        {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {GITHUB_PAT}",
        }
    )
    if GITHUB_BASE_URL not in url:
        url = f"{GITHUB_BASE_URL}{url}"

    r = requests.request(method, url, **kwargs)
    r.raise_for_status()
    return r


@lru_cache(maxsize=0)
def _ensure_label(repo, label):
    r = _gh_request("get", f"/repos/{repo}/labels")

    for remote_label in r.json():
        if label.lower() == remote_label["name"].lower():
            return remote_label["name"]

    r = _gh_request(
        "post",
        f"/repos/{repo}/labels",
        json={"name": label},
    )
    return r.json()["name"]


@lru_cache(maxsize=0)
def _ensure_milestone(repo, milestone):
    r = _gh_request("get", f"/repos/{repo}/milestones")

    for remote_milestone in r.json():
        if milestone.lower() == remote_milestone["title"].lower():
            return remote_milestone["number"]

    r = _gh_request(
        "post",
        f"/repos/{repo}/milestones",
        json={"title": milestone},
    )
    return r.json()["number"]


def _create_issue(repo, title, body, labels=(), milestone=None):
    data = {"title": title, "body": body}
    if milestone is not None:
        data["milestone"] = milestone_number = _ensure_milestone(repo, milestone)
        data["body"] = body.replace(
            "__MILESTONE_URL__",
            f"https://github.com/{repo}/milestone/{milestone_number}",
        )
    if labels:
        data["labels"] = [_ensure_label(repo, label) for label in (labels or ())]

    return _gh_request(
        "post",
        f"/repos/{repo}/issues",
        json=data,
    )


def _cli():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "directory",
        help="Directory containing *.md files with a YAML frontmatter. "
        "Files starting with '_' will be ignored. It will be recursively scanned.",
    )
    p.add_argument(
        "--repo",
        default=None,
        help="Github repository where issues must be created. "
        "Must follow format <owner>/<repo>. Not required if --dry_run is used.",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not create issues, labels or milestones, but list some stats.",
    )
    return p.parse_args()


def create_issues(path, repo, dry_run=True):
    if not repo and not dry_run:
        raise ValueError("'repo' must be set unless 'dry_run' is True")
    all_labels = defaultdict(int)
    all_milestones = defaultdict(int)
    n_issues = 0
    for dirpath, directories, filenames in os.walk(path):
        for filename in sorted(filenames):
            abs_filename = os.path.join(dirpath, filename)
            if filename.startswith("_"):
                print(f"[ i ] Ignoring '{abs_filename}' (starts with underscore)")
                continue
            doc = frontmatter.load(abs_filename)
            if not doc.metadata:
                print(f"[ i ] Ignoring '{abs_filename}' (no frontmatter)")
                continue
            labels = doc.get("labels") or ()
            milestone = doc.get("milestone")
            for label in labels:
                all_labels[label] += 1
            if milestone:
                all_milestones[milestone] += 1
            n_issues += 1
            if dry_run:
                print(f"[ i ] Would create issue for '{abs_filename}'.")
                print("      Title:", doc["title"])
                print("      Labels:", ", ".join(labels) or "N/A")
                print("      Milestone:", milestone or "N/A")
                continue
            try:
                _create_issue(
                    repo=repo,
                    title=doc["title"],
                    milestone=milestone,
                    labels=labels,
                    body=doc.content,
                )
            except Exception:
                print(f"[ERR] Could not create issue for {abs_filename}!")
                traceback.print_exc()
            else:
                print(f"[OK!] Created issue for {abs_filename}")
            time.sleep(0.1)

    print("-------")
    print("Summary")
    print("-------")
    created = "Would have created" if dry_run else "Created"
    print(f"{created} {n_issues} issues")
    print(
        f"{created} {len(all_labels)} labels:",
        *[f" - '{label}' ({count})" for label, count in sorted(all_labels.items())],
        sep="\n",
    )
    print(
        f"{created} {len(all_milestones)} milestones:",
        *[
            f" - '{milestone}' ({count})"
            for milestone, count in sorted(all_milestones.items())
        ],
        sep="\n",
    )


def main():
    args = _cli()
    create_issues(args.directory, args.repo, args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
