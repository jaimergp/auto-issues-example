## Create issues from files

Script to create issues with labels and milestones
from a series of Markdown files with YAML frontmatter.

The frontmatter schema is:

```
title: str.
    Title of the issue.
labels: list of str.
    Labels to assign to the issue. They will be created
    if they don't exist.
milestone: str.
    Name of the milestone to assign to the issue.
    It will be created if it does not exist.
```

## Requirements

3rd party dependencies:
- requests.
- python-frontmatter.

## Tokens

Create a personal access token with `read&write` issue and pull_request
permissions in the target repo and export it as `GITHUB_PAT`.
