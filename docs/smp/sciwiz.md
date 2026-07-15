# Software Management Plan in SciWiz

[**SciWiz**](https://sciwiz.lumc.nl/) is the LUMC’s instance of the platform that provides the SMP template as an
interactive online form. You can log in, create a project, and step through the questions at your own pace. SciWiz provides a flexible approach to standardizing software management across LUMC, while also accommodating diverse project needs.

> Note: SciWiz is currently only accessible via the LUMC network.

## How to create an SMP

1. Access [SciWiz](https://sciwiz.lumc.nl/).
    - Go to [sciwiz.lumc.nl]((https://sciwiz.lumc.nl/)). 
    - Log in or create an account using your LUMC email address.
2. Create a new project
    - Once logged in, in the left-hand navigation bar, click **Projects**.
    - Click **Create** (top right).
    - Enter the name of your software project.
    - Select the following Knowledge Model: “LUMC-DCC Software Management Plan”.
    - When prompted to select Question Tags, you can filter questions according to your project’s complexity, see [Management levels](#management-levels) for more details.
    - Click **Create** to start.
3. Write the SMP by answering questions. You can save your progress at any time and return later to complete it. You can also invite collaborators.

The **Research Software best practices** section of this guideline roughly maps onto the questions in the SMP and is designed to help you think about your project and fill out the questions efficiently.

## Management levels

The SMP uses three management levels—A, B and C—to adjust the questions according to management needs, with A being the lowest level and C the highest.

| Level | Typical software | Expected rigour |
|---|---|---|
| **A — personal / one-off** | A script or notebook for one paper | Repository, license, purpose, maintainership, minimal reproducibility notes |
| **B — project / shared** | A reusable pipeline, package, workflow or tool used by a group | Documentation, testing, citation, packaging, dependency management, maintenance plan |
| **C — critical / institutional** | Software used in production, by external users, or in clinical/institutional contexts | Full governance, monitoring, security, auditability, support contracts, robust continuity |

When creating a project in SciWiz, you can hover over a management level tag to see its description and applicability.

Starting too low is risky: the project may grow before the basics are in place. Starting higher than needed may cost a little extra time, but it usually prevents worse work later. In SciWiz (the platform that hosts the SMP), the level you choose acts as a filter on the question set; you will only see questions tagged for your level and below. The level cannot be changed later, so choose carefully. If you are unsure, select the higher level.

## Answering questions at different project phases

Each question in the SMP is assigned a project phase. This determines whether you describe future plans or current practice.

**Project phases and expectations**

- **Ideation** and **Planning**—describe the *intended* or planned state.
- **Active development**—provide *concrete details*: real URLs, files, tools, and named responsibilities.
- **Maintenance**—focus on *changes over time*: releases, deprecations, maintainer updates, and support status.

**How to read and answer the questions**

For consistency, questions are written in the present tense.
In early project phases, read **"Does the project…"** as **"Does or will the project…"**.

Do not answer with terms such as **"planned"** or **"not yet implemented"**. Instead, answer the question directly and describe the intended setup. The project phase already indicates whether you are describing current practice or future plans.

## A note on regulated software

The SMP is **not** a substitute for the regulatory documentation that must be produced for medical device or in vitro diagnostic software.
While it can complement such documentation,it cannot replace the artefacts required for Software as a Medical Device (SaMD), IVD software, clinical decision-support tools, or software developed under a formal quality-management system (ISO 13485, IEC 62304, ISO 14971, MDR, IVDR, etc.).

If your software produces or influences a clinical recommendation, triages patients, is embedded in a regulated device, or is otherwise covered by a sectoral regime, flag this in the General chapter and contact <LUMC legal> early. Treat the SMP as a high-level overview that complements, not replaces, your regulated documentation.

## A note on data: the SMP does not replace the DMP

The LUMC SMP addresses data only in relation to how software *handles* it. Details about legal basis, retention, consent, and storage of personal data belong in your Data Management Plan. The [Risks & mitigation](../best-practices/risks.md) chapter only flags that the software has a relationship with sensitive data and points to the corresponding DMP.