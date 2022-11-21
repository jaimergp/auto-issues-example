---
title: Enhancements to feedstocks' verification and validation workflows
milestone: "18 months"
labels: [mission::infra, security]
---

Primarily focused on performance and reliability.

## 📌 Summary

Improve the artifact verification and validation workflows as they are moved from `cf-staging` to `conda-forge`.

## 📝 Background

conda-forge feedstocks are repositories equipped with the build machinery provided by conda-smithy.

When a PR is merged to a feedstock branch, the resulting conda packages are not uploaded directly to conda-forge.
They are first placed in a staging channel named `cf-staging`.
The artifact validation bot hosted in a Heroku instance downloads the artifacts, runs some analysis and if successful, then they are copied to the actual `conda-forge` channel.

The analysis includes checks like:

- File clobbering: is the package producing files that belong to another package? This is reported as an issue
- Package name squatting: is the feedstock producing packages that belong to other feedstocks? If true, it prevents the upload.
    - This check is needed to work around the lack of permission granularity in anaconda.org

Depending on the size of the package, this causes some strains on the already overworked Heroku dyno.
## 🚀 Tasks / Deliverables

- [ ] Profile load and usage, and decide if the current implementation needs performance improvements
- [ ] Consider hardware alternatives beyond a single machine: a multi-worker approach with auto-scaling
- [ ] Perform risk analysis and decide if other validation aspects are needed, if server load stopped being a bottleneck

## 📅 Estimated completion

This task should be completed within the first 18 months.

## ℹ️ References

- [`conda-forge/conda-forge-webservices`](https://github.com/conda-forge/conda-forge-webservices): the Heroku app deployed to run conda-forge admin commands and linting
- [`conda-forge/artifact-validation`](https://github.com/conda-forge/artifact-validation): code and workflows to validate conda-forge artifacts
