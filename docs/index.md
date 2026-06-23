# README

Research software (RS) plays an important role in the transparency and reproducibility of research and research outcomes.
Following best practices in software development can help enhance quality, maintainability and usability of research software. Additionally, FAIR Principles for Research Software ([FAIR4RS]) provide guidelines to increase its findability, accessibility, interoperability, and reusability (FAIR).
A Software Management Plan (SMP) integrates these guidelines and practices by describing how software is developed, maintained, shared, and used throughout its lifecycle, from initial planning to long-term preservation.
Given the diverse nature of research software, this guide provides practical recommendations for writing an SMP to plan the development of research software that will serve as an integral part of the research cycle.

[FAIR4RS]: https://doi.org/10.15497/RDA00068

## What is research software?

> *Research Software includes source code files, algorithms, scripts, computational workflows and executables that were created during the research process or for a research purpose.*
> -- [Gruenpeter *et al.* 2021]

[Gruenpeter *et al.* 2021]: https://doi.org/10.5281/zenodo.5504016

Research software can be a research output in itself, or it can be developed to support research activities
throughout the research lifecycle, from data collection and analysis to visualization and dissemination.
It can be used to analyze data, simulate systems, visualize results, and more.

The scope of research software is broad and can include scripts, libraries, (simple or complex) applications, and APIs.
Research software can be developed by researchers or software engineers.
In the following, we will refer to them as research software developers.

For more information and to understand whether you are developing research software, see
[definitions and examples of RS](rs/definitions-examples.md).

## Scope and limitations of this guide

This guide focuses on the role of research software in supporting reproducible and reusable research outcomes.
Within this context, it applies to a broad range of research software: from small, single-use scripts to more complex applications serving as research infrastructure.

> **IMPORTANT:** In some cases, additional regulations may apply that are not covered by this guide.
> Please make sure to check for additional guidelines or regulations related to, e.g., clinical research, [software as a medical device], processing of potentially personally identifiable information, software security, or security of (cloud) computing environments.

[software as a medical device]: https://www.albinusnet.nl/en/products-and-services/research/research-facilities/research-with-medical-devices/?

## Assumed knowledge

This guide assumes that you have a basic understanding of software development and research practices.
Additionally, it is helpful if you are familiar with Git.
If you are not familiar with Git, you can enroll in the [LUMC's Git course](https://git.lumc.nl/courses/gitcourse).
You can find more training on our [LUMC FAIR Research Software Training website](https://lumc-dcc.github.io/research_software_training/).

## Guide organization & usage

This guide is organized to provide a navigable approach to managing and developing research software (RS).
The first section covers RS definitions and helps you determine whether your work qualifies as RS.
The section on software management plans (SMPs) explains what an SMP is, how it can benefit your work and how to write an SMP using our supporting tool SciWiz.
The section on best practices outlines FAIR4RS principles and provides detailed guidance on different aspects of RS management.
Additionally, the guide includes an overview of key organizations and communities supporting RS development,
offering tools and guidance for continued learning.

## License

The Research Software Guide by LUMC DCC is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
