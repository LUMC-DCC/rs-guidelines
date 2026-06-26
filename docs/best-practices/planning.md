# Planning & sustainability

The development of research software involves multiple phases that should be considered from the outset.
Taking the whole software life cycle into account, rather than only the part leading to a publication, is essential for long-term code sustainability.

Estimates are perfectly adeqaute in this context. The goal is to make resource needs explicit so that shortfalls are identified early, when they can still be addressed.

## Infrastructure & hardware

List the physical, virtual, or cloud resources the project needs to build, test, run, or maintain.

Common categories:

- **Local servers** or departmental compute;
- HPC allocations on **LUMC Shark** or **SURF Snellius**;
- **GPUs**;
- **Storage tiers**;
- **Managed databases** - institutional or cloud-hosted;
- **Cloud compute or storage** - AWS, Azure, GCP, SURF cloud;
- **Specialised lab instruments** that the software controls, reads from, or feeds.

This is *not* the place for GitHub or GitLab hosting, package registries, or documentation hosting, those belong in [Sharing & licensing](sharing-licensing.md) and [Documentation & community](documentation-community.md), unless you are using paid tiers with explicit capacity or contract implications.

For each item, capture:

- **Requirement** - what you need;
- **Details** - capacity, access constraints, funding source.

> **In the SMP:** the Infrastructure list is open-ended. Be specific enough that a hand-over to a new team would not require guessing. "GPU access" is not enough; "2× NVIDIA A100 80GB on Shark, allocation under PI <X>, valid until end of 2027" is.

## External services

External services are the people, contracts, and paid tiers outside your immediate team that the project relies on.

Examples:

- **IT&DI** support and infrastructure tickets;
- **LUMC-DCC** consultancy (RSE review, FAIR support, DMP help);
- **External RSE review** or audit;
- **Penetration testing** (for Level C with a network face);
- **Paid CI minutes** on GitHub or GitLab when free tiers are exhausted;
- **Commercial APIs** (OpenAI, Anthropic, mapping services, payment processors);
- **Legal or IP support**;
- **Vendor support contracts** for instruments or proprietary software.

Quantify where you can. *"Need DCC help"* is not enough. *"~5 days of DCC RSE consultancy across the project; ~10 hours/year of IT&DI support; €1,200/year for CI minutes once we move to a self-hosted runner"* is.

If a service is unfunded, say so. *"To be arranged"* is a valid early answer and a real planning risk; flagging it in the SMP is precisely the point.

> **In the SMP:** the External services list captures service, provider, type(s), quantity, and cost coverage. The distinction from Infrastructure (physical/virtual resources you *consume*) and Expertise (skills *inside* your group) is intentional, keep the lists separated.

## Development effort

Estimate the effort needed to reach a usable version. Use whatever unit fits the project: **person-days**, **person-months**, **FTE-time**, **sprint count**, **student-project duration**, or **work-package effort** if you are inside a larger grant.

Recommended format: `<FTE-fraction> for <duration>`, e.g.:

- `0.5 FTE for 18 months`;
- `1.0 FTE-month one-off`;
- `one PhD student, 20% time for 24 months, with monthly RSE review`.

Order-of-magnitude is fine. The number does not need to be defensible to a procurement officer; it needs to be defensible to *you in six months*.

Include the hidden work. For software that is meant to be used by others, **documentation, testing, release setup, packaging, code review, user support, and deployment** are typically needed, they account for a sizeable percentage of the total effort. Budget for them.

## Updates & maintenance

What level of maintenance can realistically be provided once the project transitions out of active development?
Provide a realistic assessment and avoid overpromising.

Useful categories:

- **Active / routine maintenance.** Regular bug fixes, dependency updates, and minor improvements on a defined cadence.
- **Security maintenance only.** No new features; security and critical-compatibility issues are handled. Acceptable for software past its main grant.
- **Best-effort.** Maintainers respond when they can, without a guaranteed timeline. Acceptable for shared but non-critical tools.
- **Frozen / archived.** No updates expected; users are warned in the README and on the documentation landing page.

## Maintenance effort

Estimate annual effort *after* active development ends:

- `0.05 FTE/year` for dependency updates and issue triage on a small library;
- `0.2 FTE/year` for a Level C production tool with users to support;
- `0 FTE/year - project archived at end of grant`.

Zero maintenance is an acceptable answer **only** if there is an explicit retirement and accessibility plan. Zero maintenance with no archive is just abandonment.

## Continuity & hand-over

Describe what happens if the current maintainer leaves, changes role, or loses access. Even a paragraph is enough, as long as it covers the basics.

A minimum viable continuity plan:

- A **backup maintainer** has repository/admin access (this is also why the SMP requires at least two maintainers; see [Project identity & people](identity.md)).
- **Installation and release instructions** are written down somewhere a stranger can find them.
- **Open issues are triaged** before hand-over: labelled, prioritised, or closed with a reason.
- **Credentials and secrets** are not tied to a personal account; they live in a shared secrets manager or a service account.
- The **repository is transferred** to an LUMC or project organisation, not held in a personal GitHub account.

For Level C, the continuity plan might need more: named roles, escalation timelines, a hand-over checklist, and how users are notified.

## Expertise

Listing required expertise separately from people makes gaps visible.

Be specific. *"Programming"* is not a skill statement. *"Python + pytest + CI on GitHub Actions; intermediate"* is. Examples of useful entries:

- Research-software engineering (Python packaging, CI, code review).
- MLOps (training pipelines, experiment tracking, model registries).
- Web/API development (REST, OpenAPI, FastAPI, OAuth, async I/O).
- Data stewardship (FAIR metadata, repository deposit workflows).
- Domain knowledge (clinical genomics, biostatistics, image analysis, neurology).
- DevOps / infrastructure (Kubernetes, Terraform, Docker, Ansible).
- Security (NEN-7510, OWASP, audit response).
- Regulatory (IEC 62304, ISO 14971, MDR).
- UX/UI for clinicians or non-developer users.

If a skill is missing in your team, name where it will come from: an external collaborator, a training course, a hire.

## Retirement criteria

Retirement is not the same as deletion. For research software, retirement usually means: **no new development**, **clear archival status**, **preserved access to relevant releases**, and **users informed**.

Good retirement triggers:

- A successor project replaces it.
- The cohort, study, or grant ends.
- An upstream dependency is no longer viable and replacing it is not justified.
- Regulatory or institutional requirements make continued use impossible.
- Maintenance funding ends.
- Security risk becomes unacceptable.

Write the conditions down *before* they happen. Projects without retirement criteria might drift into an unclear half-alive state where users assume they are maintained when they are not.

## Post-retirement accessibility

If retired software remains accessible, specify how:

- **Archive location**: [Zenodo](https://help.zenodo.org/docs/github/archive-software/), [Software Heritage](https://docs.softwareheritage.org/#landing-preserve), an institutional repository, or a GitHub/GitLab archive flag on the repository.
- **Persistent identifier**: a DOI or other PID if available (a [Concept DOI from Zenodo](https://support.zenodo.org/help/en-gb/1-upload-deposit/97-what-is-doi-versioning) is ideal - it always points to the latest archived version; see [Sharing & licensing](sharing-licensing.md)).
- **Retention period**: 5 years, 10 years, indefinite, or "until superseded".
- **Successor project**, if any, with a link.
- **User notice**: a README banner, a release-note announcement, and (for active user bases) an email.

If software *cannot* remain accessible, explain why. Valid reasons include sensitive data, contractual restrictions, or legal/regulatory constraints. "Lack of time" is a weak reason, a metadata-only archive (a Zenodo deposit with just the documentation and CITATION) is almost always feasible.

> **In the SMP:** In early stages of the project, write down how you *would* handle its retirement. It is much easier to plan for end-of-life when the project is still hypothetical than when it is already overdue.

## Further reading

- [The Turing Way - Project Management](https://book.the-turing-way.org/project-design/project-design) - chapters on planning, hand-over, and lifecycle management.