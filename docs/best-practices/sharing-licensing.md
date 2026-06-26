# Sharing & licensing

Properly sharing research software involves more than just uploading it somewhere. It involves a series of small decisions: choosing a repository, creating a registry entry, assigning a persistent identifier, adding a citation file, and selecting a license. These decisions make your work findable, retrievable, citable, and legally reusable.

LUMC supports the [Open Science](https://www.openscience.nl/en/what-is-open-science) principle of being **"as open as possible, as closed as necessary"**. In line with its [strategic](https://www.lumc.nl/en/about-lumc/maatschappelijke-rol/strategy-202428/) commitment to making research outputs such as datasets, code, and models broadly accessible, openness is the default.
Choosing a closed-source approach can be appropriate in cases involving GDPR, intellectual property, medical device regulations, or contractual obligations, but such restrictions require clear justification.

## Repository

Any project beyond a quick, one-off script should be kept in version control from the start (e.g., using Git). It should be hosted on a *forge*—a platform that combines version control with collaboration features (such as GitHub or GitLab). The choice of forge depends on the intended use of the software.

- **LUMC GitLab** (`gitlab.lumc.nl`) is the right home for internal tools, sensitive content, software with patient-data adjacencies, and anything not yet ready for the open world.
- **GitHub** is the right home for open-source projects intended for community use. Most of the research-software ecosystem (Zenodo integration, GitHub Actions for CI, well-trodden release workflows) sits there.
- **Public GitLab**, **Codeberg**, or other forges are reasonable when there is a specific governance, license, or platform reason.

What is *not* an acceptable place for research code:

- A laptop only (one disk failure away from no code at all).
- A shared drive (no history, no diffs, no review).
- A *personal* GitHub or GitLab account (when the person leaves, so does the project).

If a repository must be **private** for legitimate reasons (GDPR, IP, MDR/IVDR, security through obscurity for a small subset of components, contractual obligations), write the reason down in the SMP. *"Private for now"* is fine if there is a plan to open it later; *"private indefinitely with no documented reason"* is not.

> **In the SMP:** record the repository URL, whether it is publicly accessible, and (if not) the specific reason. Plan to revisit the openness decision at every major release.

## Registries

A *registry* is a structured metadata catalog that describes, indexes, and helps discover software. It is distinct from a *package repository* (PyPI, conda-forge, Docker Hub, CRAN), which hosts installable artefacts. Registry entries primarily support discoverability and citation, while package entries primarily support distribution and installation. You usually want both.

Useful registries depend on the audience:

- **[bio.tools](https://bio.tools/)** - for life-science software; tightly integrated with ELIXIR.
- **[Research Software Directory](https://research-software-directory.org/)** - Dutch-academic-flavoured registry; LUMC and other UMCs have entries here.
- **[WorkflowHub](https://workflowhub.eu/)** - A registry for describing, sharing and publishing scientific computational workflows
- **[Zenodo](https://zenodo.org/)** - strictly speaking a deposit/archive, but it issues DOIs and is searchable.
- **[Software Heritage](https://www.softwareheritage.org/)** - universal archive; assigns a SWHID identifier that resolves to a specific commit, even if the original repository disappears.

Using multiple registries is encouraged, as different communities rely on different platforms. Registering in several involves only limited one-time effort.

For a curated, audience-specific overview, see [Awesome Research Software Registries](https://github.com/NLeSC/awesome-research-software-registries), a registry index organised by country, organisation, language, and domain.

> **In the SMP:** for each registry, capture the name and the URL or ID of your entry.

## Persistent identifiers

A persistent identifier (PID) is a long-lasting, resolvable identifier that remains stable even if the location or metadata of the resource changes.
For research software, a common practice is to use a **DOI**, e.g., minted via Zenodo when archiving a tagged release.

The recommended workflow is short:

1. Connect your GitHub or GitLab repository to [Zenodo](https://zenodo.org/account/settings/github/).
2. Tag and push a release in the repository.
3. Create a GitHub/GitLab Release for that tag.
4. Zenodo mints a [**version DOI**](https://support.zenodo.org/help/en-gb/1-upload-deposit/97-what-is-doi-versioning) (specific to that release) and a **concept DOI** (always resolves to the latest archived version).
5. Add the DOI badge to your README and the DOI to your `CITATION.cff`.

The concept DOI is the one you usually want to share in papers and slides - it never goes stale. The version DOI is the one to cite when reproducibility requires exact identity.

For finer-grained provenance, [Software Heritage](https://www.softwareheritage.org/) assigns a **SWHID** to specific commits, trees, or blobs. This is useful when you need to refer to a precise state of the code rather than a release.

Useful resources on identifiers themselves:

- [The DOI System](https://www.doi.org/) - the canonical reference.
- [DataCite](https://datacite.org/) - the registrar behind most research DOIs, including Zenodo's.

> **In the SMP:** record the identifier type (DOI, SWHID, bio.tools ID), the identifier, and which version of the software it corresponds to. For the concept DOI, write `concept` in the version field.

## Citation

A `CITATION.cff` file in the repository root is the modern way to make software citable. It is plain YAML, machine-readable, and recognised natively by GitHub, GitLab, and Zenodo. When a Zenodo release is created, the `CITATION.cff` is read automatically and used to populate the deposit's authors and metadata.

A minimal `CITATION.cff` includes:

- the **software title**;
- **authors** with ORCID IDs where possible;
- the **version**;
- the **release date**;
- the **DOI** for that version (or the concept DOI);
- a **preferred-citation message**, especially if a method paper exists.

The [CFF INIT](https://citation-file-format.github.io/cff-initializer-javascript/) tool generates a valid file from a web form - useful when you are not yet comfortable with YAML.

If a methods paper exists for the software, be explicit in the citation: *cite the paper for the method and cite the software DOI for the exact implementation/version*.

A practical reference on the whole workflow: [The Turing Way - Software Citation with `CITATION.cff`](https://book.the-turing-way.org/communication/citable/citable-cff.html).

> **In the SMP:** the Publications question captures the paper(s) that describe the method, with their DOI/PMID/PMCID. The software DOI lives under Persistent identifiers. Keeping these separate is intentional. A piece of software can outlive its methods paper, or vice versa.

## Software license

Without a license, code is "all rights reserved" by default - even if it is publicly visible on GitHub. **"Public on GitHub" is not the same as "open source".** Without a license, no one (sometimes not even you, depending on your contract) can legally reuse, fork, modify, or build on your code. Even compiling or running the software can constitute a violation in some jurisdictions.

[Choose A License - No License](https://choosealicense.com/no-permission/) explains the implications.

### Which license?

The LUMC default is **"as open as possible, as closed as necessary"**. Concretely, the recommended default is the [**Apache License 2.0**](https://www.apache.org/licenses/LICENSE-2.0). It is permissive (compatible with most other open licenses, including commercial use), includes an explicit patent grant (a real practical advantage over MIT or BSD-3-Clause for software that might touch patentable methods), and is widely understood.

If you have a specific reason to prefer something else:

- **MIT** or **BSD-3-Clause** - even simpler permissive licenses; lack the explicit patent grant.
- **GPL-3.0** or **AGPL-3.0** - copyleft. Forces downstream users to keep their derivatives open under the same terms. Choose deliberately; copyleft is a real constraint on adopters.
- **CC-BY 4.0** - usually for *data and documentation*, not code. Avoid licensing code under a Creative Commons license, they were not designed for that.

Always use the [SPDX identifier](https://spdx.org/licenses/) (`Apache-2.0`, not "Apache 2.0"). It is machine-readable and recognised by package registries, GitHub, and most other tooling.

Useful references:

- [OSI Approved Licenses](https://opensource.org/licenses) - Open source licenses approved by open source initiative
- [Choose A License](https://choosealicense.com/) - a quick licenses walk-through.
- [tl;dr Legal](https://www.tldrlegal.com/) - plain-English summaries of common licenses.
- [Public License Selector](http://ufal.github.io/public-license-selector/) - a quiz for choosing a license.
- [Free Software Foundation - Licensing & Compliance](https://www.fsf.org/licensing/) - FSF's licensing recommendations and FAQ.
- [The Turing Way - Licensing chapter](https://book.the-turing-way.org/reproducible-research/licensing) - broader treatment with legal and ethical context.
- [eScience Center - How to share software](https://esciencecenter-digital-skills.github.io/research-software-support/modules/licenses/how_to_share) - practical guide.

The repository should contain a `LICENSE` file (the full license text) at the root. Most forges create one for you when you initialise the repository or run a "Choose a license" wizard.

> **In the SMP:** the License question uses the SPDX identifier list (an integrated search via the SciWiz form). If the software is unreleased and you have not yet chosen a license, write down *which* license you intend to use.

## License compatibility

If your software depends on or includes code under other licenses, your license must be compatible with them. Incompatible licenses can:

- prevent you from distributing the combined software;
- require you to adopt a more restrictive license;
- create real legal risks if your code is widely used downstream.

A few practical guidelines:

- **Permissive licenses** (Apache-2.0, MIT, BSD-3-Clause) compose easily with each other and with copyleft licenses, but the result is often constrained by the most restrictive component.
- **GPL** in a dependency forces the rest of the *distributable combined work* to be GPL or compatible.
- **CC-BY-NC** (non-commercial) dependencies are usually a problem for shared research software. Avoid them in distributable code.
- For commercial dependencies, **read the license carefully** before assuming it allows redistribution.

Tooling can do most of the work:

- **Python**: [`licensecheck`](https://github.com/FHPythonUtilities/licensecheck), [`pip-licenses`](https://github.com/raimon49/pip-licenses).
- **Rust**: [`cargo-deny`](https://github.com/EmbarkStudios/cargo-deny).
- **Node**: [`license-checker`](https://github.com/davglass/license-checker).
- **Cross-language**: [FOSSA](https://fossa.com/), [Snyk](https://snyk.io/), and **GitHub Advanced Security** (the dependency graph + license alerts).

For Level A, a manual check of direct dependencies before public release is acceptable. For Level B/C, automate it in CI so a problematic license added in a dependency update fails the build.

References:

- [The Turing Way - License Compatibility](https://book.the-turing-way.org/reproducible-research/licensing/licensing-compatibility.html) - clear treatment with a compatibility matrix.
- [SBOM (Software Bill of Materials)](https://www.cisa.gov/sbom) - for Level C: a formal inventory of components and licenses, generated with tools like [Syft](https://github.com/anchore/syft) or [CycloneDX](https://cyclonedx.org/).

> **In the SMP:** the question asks whether you check dependency-license compatibility, and how. Automated tooling is preferred; manual checks are acceptable for small projects but fragile.

## Publications

If a methods paper, preprint, or application-note exists for your software, link it. Capture the **DOI** (preferred), and where applicable also **PMID** and **PMCID** for PubMed-indexed work. Note which version of the software the paper describes.

> **In the SMP:** the Publications list is open-ended. If one exists, list at least the foundational methods paper cited with the software in `CITATION.cff`.

## Further reading

- [Choose A License](https://choosealicense.com/) - license picker.
- [SPDX](https://spdx.org/licenses/) - canonical machine-readable license identifiers.
- [The Turing Way - Software Citation](https://book.the-turing-way.org/communication/citable/) and [Licensing](https://book.the-turing-way.org/reproducible-research/licensing) - broader treatment.
- [Zenodo–GitHub integration guide](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content) - official walk-through of the recommended workflow.
- [Awesome Research Software Registries](https://github.com/NLeSC/awesome-research-software-registries) - registry directory.
