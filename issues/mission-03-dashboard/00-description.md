---
title: Building a maintainers dashboard with Quetz
milestone: null
labels:
- "type: mission"
---

## 📌 Summary

Prepare the conda ecosystem for OCI-based storage compatibility.

## 📝 Background

There is no straightforward way to monitor the operational status of conda-forge's infrastructure. 

conda-forge.org/status offers a "maintainers dashboard" with information about:

- Operational status of many of the services that conda-forge relies on, including CI, bots, CDN cloning, webservices, documentation...
- Ongoing migrations (collection of PRs automatically issued by the bots)
- Communication about known incidents

Unfortunately, this is far from being comprehensive view of ongoing maintenance tasks, bottlenecks, or the overall health of the many bots and infrastructure pieces. 

Having a detailed picture of the infrastructure and automation tools will significantly improve the maintainers' workflow and aid with identifying critical risks— which is essential to keeping up with the increasing growth and demand from the community. 

Quetz is chosen as an open-source server for hosting conda packages, thus allowing for increased transparency and extensibility. 
This would have the added benefit of centralizing the currently scattered-across-repositories packaging metadata in a canonical, API-first, performant-at-scale database, laying the foundation for further infrastructure automation and improvements to the building processes.


## 🚀 Tasks / Deliverables

> See issues labeled as `mission::dashboard`

## ℹ️ References

- [conda-forge.org/status](https://conda-forge.org/status): Status dashboard on conda-forge.org
- [OCI](https://opencontainers.org/): Open Container Initiative
- [ORAS](https://oras.land/): OCI Registry As Storage
- [`oras-py`](https://github.com/oras-project/oras-py): a Python library to interact with an OCI registry
- [`channel-mirrors` organization](https://github.com/orgs/channel-mirrors/packages): OCI-based mirror of conda-forge and bioconda
