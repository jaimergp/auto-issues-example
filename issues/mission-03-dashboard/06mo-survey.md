---
title: Survey the community for feedstock health metrics ideas
milestone: "Dashboard - 6 months"
labels: [community, mission::dashboard]
---

## 📌 Summary

Investigate and design prototype mockups with the desired features for the maintenance board

## 📝 Background

conda-forge.org/status offers a "maintainers dashboard" with information about:

- Operational status of many of the services that conda-forge relies on, including CI, bots, CDN cloning, webservices, documentation...
- Ongoing migrations (collection of PRs automatically issued by the bots)
- Communication about known incidents

It could also show how "healthy" the feedstocks (conda-forge) and package-creating repositories (bioconda) are.

To inform what content should be displayed in the dashbaord, we would like ti survey the community for any other features that could be considered usegul, such as:

- Tasks that require attention by conda-forge members or volunteers (e.g. pending reviews, blocking PRs, newcomer-friendly issues...)
- Feedstocks list with relevant metrics about their health and maintenance status (e.g. risks of abandonment)

## 🚀 Tasks / Deliverables

- [ ] Survey the communities for dashboard panel ideas
- [ ] Consolidate feedback and generate report

## 📅 Estimated completion

This task should be completed within the first six months.

## ℹ️ References

- [conda-forge.org/status](https://conda-forge.org/status) (implemented in the [`conda-forge/status`](https://github.com/conda-forge/status) repo)
