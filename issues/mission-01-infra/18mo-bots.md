---
title: Improve security, performance, reliability and developer experience on conda-forge bots
milestone: "18 months"
labels:
- "mission: infra"
- "area: security"
- "team: quansight-labs"
---

## 📌 Summary

Work on bots to eliminate long-lived credentials, improve performance and
reliability, and develop end-user and maintainer's documentation.

## 📝 Background

The term "conda-forge bots" encompasses several pieces of automated infrastructure key to the operating status of the organization.
It has grown organically, with improvements, additions and hotfixes being made on an "as-needed" basis.
As a result the documentation has some gaps that need to be filled.

Since there was no initial design for its current state, no systematic review of its bottlenecks or risks has been performed.

This makes it difficult to maintain, and given the lack of a testing infrastructure, scary to even try if unfamiliar.

The audit report from the first year will have included security recommendations, performance improvement suggestions and reliability measures.
On top of that, we will make it easier to for newcomers to contribute to the valuable automation ecosystem in conda-forge.


## 🚀 Tasks / Deliverables

- [ ] Consolidate documentation pieces in a single place, with an excellent Getting Started guide
- [ ] Automate credentials provisioning without relying on long-lived tokens
- [ ] Infrastructure as code approach for the deployment of the bots

## 📅 Estimated completion

This task should be finished in the first [18 months](__MILESTONE_URL__).

## ℹ️ References

- [conda-forge's Security and Systems Sub-Team](https://conda-forge.org/docs/orga/subteams.html#security-and-systems-sub-team)
- [conda-forge's Bot Sub-Team](https://conda-forge.org/docs/orga/subteams.html#bot-sub-team)
- [conda-forge repositories that are not regular feedstocks](https://hackmd.io/nlD1rNVzQ-iA2B6o2mLWRA)
- [`regro/cf-scripts` documentation](https://regro.github.io/cf-scripts/)
- [Talks about conda-forge](https://conda-forge.org/docs/user/talks.html) (some cover infrastructure)
- [regro.github.io](https://regro.github.io/)
