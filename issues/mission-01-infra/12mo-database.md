---
title: Design and implement a database for the conda-forge graph and relevant metadata
milestone: "12 months"
labels:
- "area: data"
- "area: documentation" 
- "mission: infra"
- "team: quansight-labs"
---

## 📌 Summary

Migration of existing data sources into a purpose-built database, including a suitable
data schema and schema validation.

## 📝 Background

The metadata supporting the diverse automations at conda-forge is made of a number of repositories that serve JSON files in a given directory structure.

Depending on the tool, the metadata will be used to build a graph. 
This data is downloaded, and the graph recreated, every time the job runs, adding to substantial overhead as conda-forge grows.

Other tools depend on a different presentation of the metadata, and are supported a different repository.
This means that the same data is duplicated just to be presented in a different way.

This is not sustainable or considerate with the available resources, and we would prefer a single source of truth that runs in a performant way.

## 🚀 Tasks / Deliverables

- [ ] Enumerate data sources and their intended usage
- [ ] Design a database schema and implementation that strikes a balance of performance and maintainability
- [ ] Devise am automated, provider-agnostic deployment strategy
- [ ] Consolidate the existing data sources into the proposed database
- [ ] Study how the existing bot infrastructure can benefit from the database to inform the next steps

## 📅 Estimated completion

This task should be finished in the first [12 months](__MILESTONE_URL__).

## ℹ️ References

- https://github.com/conda-forge/feedstock-outputs
- https://github.com/regro/cf-graph-countyfair
- https://github.com/regro/conda-suggest-conda-forge
- https://github.com/regro/libcfgraph
- https://github.com/regro/libcflib