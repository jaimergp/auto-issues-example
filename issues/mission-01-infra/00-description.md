---
title: Reduce the technical debt in conda-forge infrastructure
milestone: null
labels:
- "type: mission"
- "team: quansight-labs"
---

## 📌 Summary

Audit conda-forge infrastructure to generate a roadmap that can be followed over the course of the project to improve the long-term sustainability of the ecosystem. 

## 📝 Background

Since its emergence in 2015, the conda-forge project has seen explosive growth in contributors, maintainers, repositories, artifacts, and packages served. 
To serve such a vast ecosystem (and around 300M downloads per month), the core team has heavily relied on automation, Continuous Integration and Delivery platforms and in-kind donations from multiple infrastructure providers.

Current conda-forge's infrastructure and tooling are distributed across many GitHub repositories, external CI services (Azure DevOps, GitHub Actions, TravisCI, Drone.io, CircleCI), Heroku "dynos" and AWS instances. 
Many were built as ad-hoc fixes and currently lack documentation or risk mitigation plans. 

We plan to migrate the configuration and infrastructure provisioning to reproducible, vendor-agnostic tools such as Terraform, complemented with rigorous testing, vulnerability detection, and documentation strategies to enable better security, reliability, and recovery from adverse events.

## 🚀 Tasks / Deliverables

> See issues labeled as `mission::infra`

## ℹ️ References

- [Azure DevOps Pipelines dashboard for conda-forge](https://dev.azure.com/conda-forge/feedstock-builds/_build)
- [Travis CI dashboard for conda-forge](https://app.travis-ci.com/github/conda-forge/)
- [Conda-forge repositories that are not regular feedstocks](https://hackmd.io/nlD1rNVzQ-iA2B6o2mLWRA)
- [Docker images](https://quay.io/organization/condaforge)
