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

Create a personal access token with read&write issue permissions in
the target repo and export it as `GITHUB_PAT`.
"""
import argparse
import os
import sys
import time
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
    r = _gh_request(
        "get",
        f"/repos/{repo}/labels"
    )

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
    r = _gh_request(
        "get",
        f"/repos/{repo}/milestones"
    )

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
        data["milestone"] = _ensure_milestone(repo, milestone)
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
        "Files starting with '_' will be ignored. It will be recursively scanned."
    )
    p.add_argument(
        "--repo",
        required=True,
        help="Github repository where issues must be created. "
        "Must follow format <owner>/<repo>."
    )
    return p.parse_args()


def create_issues(path, repo):
    for dirpath, directories, filenames in os.walk(path):
        for filename in sorted(filenames):
            abs_filename = os.path.join(dirpath, filename)
            if filename.startswith("_"):
                print("[ i ] Ignoring", abs_filename, file=sys.stderr)
                continue
            doc = frontmatter.load(abs_filename)
            try:
                _create_issue(
                repo=repo,
                title=doc['title'],
                milestone=doc.get("milestone"),
                labels=doc.get("labels", ()),
                body=doc.content,
                )
            except Exception:
                print(f"[ERR] Could not create issue for {abs_filename}!", file=sys.stderr)
            else:
                print(f"[OK!] Created issue for {abs_filename}", file=sys.stderr)
            time.sleep(0.1)


def main():
    args = _cli()
    create_issues(args.directory, args.repo)


if __name__ == "__main__":
    sys.exit(main())
