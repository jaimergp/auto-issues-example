---
title: Show feedstock/repository data in Quetz
milestone: "18 months"
labels: [quetz, data, mission::dashboard]
---

## 📌 Summary

Integrate feedstock data (GitHub repositories) representation in the Quetz maintainer's dashboard.

## 📝 Background

With 20K+ feedstocks, it's difficult to assess the state of each repository in a timely manner.
Maintainers are often drowned in notifications, mentions and review requests, which hinders the ability of members to help out other volunteers.

We'd like to provide better ways to assess where help is needed as part of the maintainer's dashboard.
This needs to account for both multi-repository organizations like conda-forge and monolith-based orgs like bioconda.

At this point, we should have input from the community about which metrics are relevant and informative.
The UI/UX team will have provided modern mockups that account for accessibility.

## 🚀 Tasks / Deliverables

- [ ] Enumerate required information and derived metrics, as well as their sources (e.g. created packages, their contents, metadata... but also "health metrics")
- [ ] Make sure data sources are retrievable in an easy way
- [ ] Finalize backend plugins in Quetz (prototypes should be already available)
- [ ] Finalize frontend components (prototypes should be already available)

## 📅 Estimated completion

This task should be finished within the first 18 months.

## ℹ️ References

> See main dashboard mission issue.
