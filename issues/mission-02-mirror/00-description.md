---
title: Enabling mirroring capabilities with OCI-based storage
milestone: null
labels:
- "type: mission"
- "team: quantstack"
---

## 📌 Summary

Prepare the conda ecosystem for OCI-based storage compatibility.

## 📝 Background

OCI (Open Container Initiative) registries are a well-defined standard for versioned blob storage already implemented by many public cloud providers (i.e. GitHub). 
We plan to leverage the OCI registry on GitHub Packages to develop a community-maintained mirror for bioconda and conda-forge. 

Besides, adopting an OCI-based strategy will provide additional flexibility for metadata expansion. 
With this in mind, we aim to produce and capture more comprehensive package metadata, which we will later use for: maintenance dashboards, package search functions, and security checks.

> A prototype mirror is already available at the [`channel-mirrors` organization](https://github.com/orgs/channel-mirrors/packages).

## 🚀 Tasks / Deliverables

> See issues labeled as `mission::mirror`

## ℹ️ References

- [Github Packages](https://github.com/features/packages): OCI-compliant storage on Github
- [OCI](https://opencontainers.org/): Open Container Initiative
- [ORAS](https://oras.land/): OCI Registry As Storage
- [`oras-py`](https://github.com/oras-project/oras-py): a Python library to interact with an OCI registry
- [`channel-mirrors` organization](https://github.com/orgs/channel-mirrors/packages): OCI-based mirror of conda-forge and bioconda
- [anaconda.org/conda-forge](https://anaconda.org/conda-forge): The official Anaconda channel for conda-forge