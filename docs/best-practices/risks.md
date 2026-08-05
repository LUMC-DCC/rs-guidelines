# Risks & mitigation

Research software projects do not fail because nobody anticipated *every* failure mode. They fail because nobody anticipated the *obvious* ones in time to do anything about them. The goal of this chapter is risk awareness with proportionate mitigation, not a catalog of every conceivable thing that could go wrong.

This chapter complements, it does **not** replace, the [LUMC Data Management Plan (DMP)](https://www.albinusnet.nl/en/products-and-services/research/data-stewardship/dmp/) (internal). Personal-data legal bases, consent, retention, Data Protection Impact Assessments (DPIAs), and storage policies belong in the DMP. The Risks chapter only flags that the software has a relationship with sensitive data and points to the right document.

## Personal and sensitive data

When a question asks "does the software handle personal data?", there are three useful answers, not just yes or no. The distinction matters because it changes both the obligations and the mitigations.

- **Yes, directly handles personal data.** The software is designed to read, store, transmit, log, or process personal or otherwise sensitive data as part of its normal operation, it expects such data to be present. Examples: a Castor extraction script that pulls records including dates of birth, a clinical decision-support API, an imaging pipeline that ingests DICOM files from the hospital PACS. If you are unsure what counts as personal data, see {{data-stewardship}}.
- **Yes, but user-supplied data only.** The software is a generic library, CLI, or tool that does not itself expect or require personal data, but a user *could* feed it such data. The software has no special relationship to the data: it does not depend on the data being personal, and does not see, store, or relate to it beyond the immediate operation. Examples: a statistical analysis library, a plotting tool, a deduplication algorithm.
- **No, does not handle personal data.** The software is not expected to handle such data at all. Examples: a synthetic-data generator, a build-tool plugin, a tool that operates only on simulated inputs.

The difference between the first two is *intent and design*: the first is built around real personal data, the second only permits it. A common confusion: *"my tool can be used with patient data"* sounds like the first case but is usually the second. You are not the data controller for data that someone else feeds your tool, but you are still responsible for not making it easy to leak.

Synthetic or simulated data that only *resembles* personal data, with no link to real individuals, is not itself personal data, so a tool that produces or uses only such data falls under **No, does not handle personal data**. Two cautions: generating synthetic data *from* real personal data is itself processing personal data (that step is the first case); and if individuals could be re-identified from the synthetic data, it may still count as personal. When in doubt, confirm with {{data-stewardship}}.

### What to do when the answer is *Yes, directly handles personal data*

Three things:

1. **Make sure a DMP exists for the project.** Confirm with your division's privacy officer; see {{data-stewardship}}. Link the DMP in the Software Management Plan (SMP).
2. **Document where the sensitive data lives, who has access, and how access is logged.** Even if the SMP itself stays high-level, your developer documentation should describe approved storage (Research Drive, sFTP, Vault, controlled-access HPC), the authentication path, and the access-review cadence.
3. **Decide and document the mitigation for the failure modes you can actually imagine.** Mitigations do not need to be elaborate. *"All access is via institutional SSO; access is reviewed annually; logs are written to `<X>` and retained for `<Y>` years; a suspected breach is reported through the LUMC data-breach procedure"* is a strong answer. Every LUMC employee is responsible for reporting a suspected data breach without delay, through the {{data-breach}}.

### What to do when the answer is *Yes, user-supplied data only*

Your software may not control whether users provide sensitive data, but it should still be designed to minimize the risk of accidental data leakage.
Document the design choices that prevent that:

- No telemetry by default (and certainly no telemetry that includes user data).
- No silent caching of inputs to disk in unspecified locations.
- Logs scrubbed of inputs unless explicitly enabled (and even then, with a warning).
- Clear, prominent user-facing guidance to anonymize upstream or run in a controlled environment when sensitive data is in play.

For libraries used in clinical or research workflows, these design choices are a key part of risk mitigation. Document them clearly.

### What *No* means

"No" is correct only if there is no personal data, clinical data, patient-derived data, contact data for identifiable individuals, or any data covered by an institutional sensitivity policy in the software's normal workflow.
If the software could be used with such data by downstream users, it should be classified as *Yes, user-supplied data only*.

> **In the SMP:** the answer triggers the right follow-up questions and warnings. For *directly handles*, the SMP expects a DMP reference, data categories, and a mitigation; for *user-supplied data only*, only the mitigation; for *No*, nothing further.

## Security & access control

Security obligations apply mostly to *services, APIs, and daemons*, anything that exposes a network endpoint, processes untrusted input, stores secrets, or runs with elevated privileges. Pure libraries, analysis scripts, and notebooks usually do not face these obligations directly, although they may depend on services that do.

For services and APIs, document a small number of things that matter most:

- **Authentication.** Who can access the service? Institutional SSO, OAuth, API keys, mutual TLS, Internet Protocol (IP) allowlist?
- **Authorization.** What can each role do once authenticated? Read-only, read-write, admin?
- **Secret management.** Where do keys, passwords, and tokens live? *Never* in the repository. Use a secrets manager (HashiCorp Vault, GitHub/GitLab secrets, your CI's secret store), and document what to do when a secret leaks.
- **Input validation.** How is malicious or malformed input handled? At minimum, do not pass user input to a shell, a SQL query, or a deserialiser without protection.
- **Logging - and what *not* to log.** Logs are useful for debugging and forensic analysis, and dangerous when they include personal data, secrets, or session tokens. Decide what is logged, where, for how long, and who can read it.
- **Dependency vulnerability scanning.** Most ecosystems offer this - `pip-audit`, `cargo audit`, `npm audit`, GitHub Dependabot, Snyk, FOSSA. Pick one and run it on a schedule.
- **An incident contact and disclosure path.** A `SECURITY.md` file in the repository, with a contact address, response timeline, and disclosure expectations, is the minimum. For NEN-7510 or MDR-relevant software, this is not optional.

The [OWASP Top Ten](https://owasp.org/www-project-top-ten/) is the canonical short list of common security risks in web applications and how to prevent them. If your software has a network face, read it.

> **In the SMP:** if the software is a service, expect the security follow-up to ask which measures you have in place. For libraries with no network face, "No" is the correct and sufficient answer.

## Compliance & regulatory considerations

Compliance is broader than legal regulation alone. This applies if the software is subject to any of:

- legal frameworks (e.g., **GDPR / AVG**);
- sectoral regulation (**MDR**, **IVDR**, **FDA**, comparable rules outside the EU/US);
- domain standards adopted as institutional policy (**NEN 7510**, **ISO 13485**, **IEC 62304**, **ISO 14971**);
- departmental standard operating procedures (SOPs) that govern the software's use;
- funder software-management requirements;
- journal software-availability requirements (more and more journals now require code to be archived and citable);
- data-transfer or collaboration agreements that constrain what the software can do or where it can run.

For each that applies, state which requirements it triggers, who is responsible for satisfying them, and where the corresponding documentation lives (often outside the SMP - in a DMP, an SOP, a contract, a quality-management system).

If you are unsure whether a regime applies, ask early - {{legal}} can help disambiguate.

> **In the SMP:** answer "Yes" if *any* regulatory or institutional regime applies. The follow-up asks you to tick the applicable regimes from a controlled list.

## External dependency risks

Every project has dependencies that may eventually be deprecated, break compatibility, change license, or be abandoned. The aim here is **not** to enumerate every transitive package (that lives in your lock file). It is to identify the dependencies whose loss or change would be *expensive* to recover from, and to plan for that.

Four archetypes worth flagging explicitly:

| Risk type | What it means | Typical mitigation |
|---|---|---|
| **Vendor lock-in** | A commercial or hosted service is hard to replace | Isolate behind an interface; document an exit plan; keep a local-only path if feasible |
| **Unstable upstream API** | Upstream breaks compatibility often | Pin versions; CI test against newer versions; subscribe to upstream releases |
| **Abandoned upstream** | A critical library is no longer maintained | Fork and maintain; vendor the relevant code; reduce reliance; switch |
| **Proprietary data format** | Input or output depends on closed-source tooling | Prefer open formats where possible; document the conversion path; keep a snapshot of the spec |

On choosing sustainable, preferably open file and folder formats, see the LUMC [Folders, files and formats](https://www.albinusnet.nl/weten-en-regelen/onderzoek/data-stewardship/folders-files--formats/) (internal) page.

Two more that come up in clinical contexts:

- **Hardware dependency.** Specialized equipment whose drivers, firmware, or vendor support ends. State alternatives and minimum specifications.
- **External data/source availability.** A public API, a reference dataset, or an ontology disappears or changes. Cache permitted snapshots; archive metadata; document fallback behavior.

A useful sanity check: for each dependency you list, ask *"if this stopped working tomorrow, what would we do?"* If there is no ready answer, it belongs here.

> **In the SMP:** in the External dependencies follow-up, identify the dependencies that would be *expensive to replace* and the mitigation for each. Be realistic, and focus on the dependencies that would cause real problems if they failed.

## Risk mitigation

A mitigation is only useful if it is specific enough to execute. The difference between weak and strong mitigations is concreteness, not length.

- *Weak:* "We will monitor dependencies."
- *Strong:* "Dependabot opens weekly dependency-update PRs; CI must pass before merge; the primary maintainer reviews high-severity security alerts within five working days."

For Level C projects, mitigations should also name:

- **Who owns each risk.** A role, not a name (so it survives staff changes).
- **How often it is reviewed.** Monthly, per release, annually.
- **What triggers escalation.** A failed CI run for N days, a missed maintainer hand-over.
- **Where the evidence lives.** Issue tracker labels, CI logs, release notes, a risk table in the repository, a project board.

Evidence can be lightweight. The point is that someone, possibly a future you, can audit what was promised and what actually happened, without a lengthy investigation.

## Further reading

- [OWASP Top Ten](https://owasp.org/www-project-top-ten/). Canonical short list of common web-application security risks and prevention strategies.
- The Turing Way. [Risk assessment: complexity and impact](https://book.the-turing-way.org/reproducible-research/risk-assess/risk-assess-impact.html). Explains the risk matrix and how to measure complexity and impact for research software.
- [How to perform a software risk assessment](https://www.devteam.space/blog/how-to-perform-a-software-risk-assessment/). A generic, but practical, walk-through.
- Ranković & Ivanović. [Risk Analysis Tools for Managing Software Projects](https://research.tilburguniversity.edu/en/publications/risk-analysis-tools-for-managing-software-projects). Comparative paper, useful for Level C projects considering a more structured tool.
- [pip-audit](https://github.com/pypa/pip-audit), [cargo audit](https://github.com/RustSec/rustsec/tree/main/cargo-audit), [npm audit](https://docs.npmjs.com/cli/v10/commands/npm-audit). Language-native vulnerability scanners.
- [Dependabot](https://docs.github.com/en/code-security/dependabot) and [Renovate](https://docs.renovatebot.com/). Automated dependency-update bots.
- {{data-stewardship}}. For DMP.
