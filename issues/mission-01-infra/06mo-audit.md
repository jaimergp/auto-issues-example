---
title: Audit of the current infrastructure, tooling, and credentials
milestone: "6 months"
labels:
- "area: documentation"
- "area: security"
- "team: quansight-labs"
- "mission: infra"
---

## 📌 Summary

The goal is to audit and document existing conda-forge's infrastructure.

> This will be done in public. 
> We need to ensure no critical security details such as credentials are exposed.

## 📝 Background

To propose technical debt reduction measures and ensure the long-term viability of the project and its growing ecosystem, we first need to understand and document the current status of the platform.

Expected challenges:

- Large number of moving parts across services and platforms
- Several accounts and credentials key to the normal operating conditions
- Lack of documentation for each part
- Scattered institutional knowledge

## 🚀 Tasks / Deliverables

- [ ] Choose / create repository to store WIP documentation
- [ ] Document existing infrastructure
- [ ] Safely enumerate required credentials
- [ ] Access control: on- and off-boarding core members
- [ ] Compile an audit report with suggestions and best practices

## 📅 Estimated completion

This task should be finished in the first [six months](__MILESTONE_URL__).

## ℹ️ References

- [conda-forge's Security and Systems Sub-Team](https://conda-forge.org/docs/orga/subteams.html#security-and-systems-sub-team)
- [conda-forge's Bot Sub-Team](https://conda-forge.org/docs/orga/subteams.html#bot-sub-team)
- [conda-forge repositories that are not regular feedstocks](https://hackmd.io/nlD1rNVzQ-iA2B6o2mLWRA)
- [`regro/cf-scripts` documentation](https://regro.github.io/cf-scripts/)
- [Talks about conda-forge](https://conda-forge.org/docs/user/talks.html) (some cover infrastructure)
- [regro.github.io](https://regro.github.io/)
