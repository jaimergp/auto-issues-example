---
title: Add OCI registry support in conda/mamba
milestone: "12 months"
labels:
- "area: oci"
- "area: upstream"
- "mission: mirror"
- "team: quantstack"
---

## 📌 Summary

Make `conda` and `mamba` support OCI registries as repodata and packages sources.

## 📝 Background

Having an OCI mirror is only the archival part.
The tooling has to learn how to "speak" to it.

`conda` and `mamba` should be able to download repodata and packages from OCI-backed servers.

## 🚀 Tasks / Deliverables

- [ ] Add support for OCI servers on `conda`
- [ ] Add support for OCI servers on `libmamba` via `powerloader`

## 📅 Estimated completion

This task should be finished in the first [12 months](__MILESTONE_URL__).

## ℹ️ References

- [`conda/conda`](https://github.com/conda/conda)
- [`mamba-org/mamba`](https://github.com/mamba-org/mamba)
- [`mamba-org/powerloader`](https://github.com/mamba-org/powerloader)
