# Best practices details & SMP elements

In addition to categorizing FAIR4RS principles and best practices for FOSS development according to the FAIR principles, 
these principles can also be organized by software implementation categories. 
Each category can then be expanded to outline specific components and their respective best practices in greater detail.

This section outlines the categories and components mentioned, 
each of the latter corresponding to an entry in an SMP. 
For each element, we 

* Indicate the FAIR4RS principles and/or best practices it addresses;
* Include a brief description of the element for guidance in implementing the best practices;
* Provide example content that can be included in the SMP. When an exemplary response to a best practice is available for an SMP element, 
it is labeled as "Good answer (v0)" for the initial version (before development) 
and "Good answer (later versions)" for subsequent versions (during and after development);
* Provide links to resources to learn more about relevant best practices (for applicable elements).

____________________________________________________________________________________________________________________

## General management

_____________________________________________________________________________________________________________________

### Title
↳ *[BR2]*

> Provide a clear, descriptive title for the software project. 
> It should be unique, recognizable, and informative.

_____________________________________________________________________________________________________________________

### Purpose
↳ *[BI1, R3, BR2]*
  
> Provide general information such as: 
> what problem does it solve, who is the intended audience, what are its advantages and limitations, etc.. 
> Explain why developing new software is necessary. 
> New software should not be developed when it would be more cost-efficient and beneficial for the overall community to contribute to existing software.

_____________________________________________________________________________________________________________________

### Risk analysis
↳ *[R3]*

> Describe the main external factors that should be considered by developers and users of the software. 
> For example, compliance with privacy policies, security considerations, reliability requirements, portability / vendor lock, etc..

🔗 **Resources:**

| Resource                                                                                                                                                                                        | Description                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [OWASP Top Ten](https://owasp.org/www-project-top-ten/)                                                                                                                                         | The top ten security risks for web applications and prevention suggestions          |
| [The Turing Way guide on Risk assessment: complexity and impact](https://ttw-rtd.readthedocs.io/en/latest/reproducible-research/risk-assess/risk-assess-impact.html)                            | Explanation of the risk matrix and measuring complexity and impact                  |
| [How to Perform a Software Risk Assessment?](https://www.devteam.space/blog/how-to-perform-a-software-risk-assessment/)                                                                         | A guide on how to perform a software risk assessment (on generic software)          |
| [Risk Analysis Tools for Managing Software Projects (2018) by Ranković and Ivanovic](https://research.tilburguniversity.edu/en/publications/risk-analysis-tools-for-managing-software-projects) | A paper with comparative analysis of the 4 types of different risk management tools |

_____________________________________________________________________________________________________________________

### Maintainers
↳ *[R1.2, BR2]*

> List the names and contact information of the software maintainers (at least two people).
> The maintainers are responsible for the software's development, maintenance, and support.

🟢 **Good answer (v0 + later versions):**

```
Primary maintainer: <name + contact>, 
other maintainers: <names + contacts>
```

_____________________________________________________________________________________________________________________

### Support and resources during development

> How do you plan to procure development and long term maintenance of your software? 
> Plan resources for support-related activities such as training, hiring research software engineers, infrastructure, hardware, etc.. 
> The level of support should be in line with promises made regarding the level of service provided by your software.

_____________________________________________________________________________________________________________________

### Maintenance plan
↳ *[A2, R3, BR6]*

> How do you plan to procure long term maintenance of your software? 
> What level of support will be provided for users of the software and how will this support be organised? 
> Make sure there are arrangements in place for the maintenance and reuse of your software.

_____________________________________________________________________________________________________________________

### Retirement plan
↳ *[A2]*

> Describe how the software will be retired, including how users will be informed and how data will be handled.
> Include a plan for archiving the software and its documentation.
> Specify the expected end-of-life date for the software.
> If the software is to be maintained indefinitely, explain how this will be ensured.

_____________________________________________________________________________________________________________________


## Licensing & accessibility

_____________________________________________________________________________________________________________________

### Repository
↳ *[A1, BA1, R1.2]*

> Describe where the software will be stored and whether it will be publicly available.
> If you do not plan to make it publicly available you should provide a justification.

🟢 **Good answer (v0):**
```
The software will be stored in a <public or private> GitHub (or Gitlab) repository
```

🟢 **Good answer (later versions):**
```
<link to a GitHub (or GitLab) repository> 
```

_____________________________________________________________________________________________________________________

### Metadata

`TODO`

_____________________________________________________________________________________________________________________

### Registries
↳ *[F4, BF2, A1, R1.2]*

> List relevant software registries where the software will be findable.

🟢 **Good answer (v0):**
```
The software will be findable through the following relevant registries: 
<registry links> 
```

🟢 **Good answer (later versions):**
```
<links to the software in the registries> 
```

🔗 **Resources:**

| Resource                                                                                                      | Description                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [Awesome Research Software Registries](https://github.com/NLeSC/awesome-research-software-registries)         | eScience Center's curated list of research software registries (organized by country, organization, language and domain + generic registries) |

_____________________________________________________________________________________________________________________

### Persistent identifier
↳ *[F1, F3, BF1]*

> Specify the identifier system (e.g., DOI) to be used for versioning and citing the software.

🟢 **Good answer (v0):**
```
The software will be assigned a DOI for each major release via <DOI issuing system/registry> 
```

🟢 **Good answer (later versions):**
```
<DOIs for each major release> 
```

🔗 **Resources:**

| Resource                                                                                                      | Description                                                      |
|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [Digital Object Identifier (DOI) System](https://www.doi.org)                                                 | DOI system's official website                                    |
| [DataCite](https://datacite.org)                                                                              | support the creation and management of DOIs for research outputs |

_____________________________________________________________________________________________________________________

### Citation
↳ *[BR2]*

> Describe how users should cite the software in publications or other projects. 
> Specify if a CITATION.cff file or similar will be used.

🟢 **Good answer (v0):**
```
The repository will include a CITATION.cff file
```

🟢 **Good answer (later versions):**
```
<link to CITATION.cff> 
```

🔗 **Resources:**

| Resource                                                                                                                                                | Description                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [The Turing Way guide on Software Citation with CITATION.cff](https://the-turing-way.netlify.app/communication/citable/citable-cff.html#cm-citable-cff) | A guide on how to cite software and data in your research publications                                 |
| [CFF INIT](https://citation-file-format.github.io/cff-initializer-javascript/#/)                                                                        | A tool to help you generate citation metadata and create CITATION.cff files for your software projects |

_____________________________________________________________________________________________________________________

### License
↳ *[BA1, R1.1, BR4]*

> Specify the software license.
> The license should be as open as possible, and as closed as necessary.
> Recommended license: [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

🟢 **Good answer (v0):**
```
The software will be licensed under the <preferably Apache 2.0>  license, 
and the repository will include a LICENSE file
```

🟢 **Good answer (later versions):**
```
<Apache 2.0 or other license name> : <link to LICENSE> 
```

🔗 **Resources:**

| Resource                                                                                                                                             | Description                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [No License](https://choosealicense.com/no-permission/)                                                                                              | Explanation for what happens when you don't use a license                                 |
| [Free Software Foundation (FSF) Licensing & Compliance Team](https://www.fsf.org/licensing/)                                                         | Licensing recommendations, analysis, and FAQ                                              |
| [The Turing Way guide on licensing](https://the-turing-way.netlify.app/reproducible-research/licensing)                                              | Explains how important it is to understand how laws and licensing can affect your project |
| [Public License Selector](http://ufal.github.io/public-license-selector/)                                                                            | A quiz to help you choose a license for your project                                      |
| [ChooseALicense.com](https://choosealicense.com)                                                                                                     | A website to help you choose an open source license for your project                      |
| [tl;dr Legal](https://www.tldrlegal.com)                                                                                                             | A website that explains software licenses in plain English                                |
| [eScience Center guide on sharing software](https://esciencecenter-digital-skills.github.io/research-software-support/modules/licenses/how_to_share) | A guide on how to share software and data legally and ethically                           |

_____________________________________________________________________________________________________________________

### License compatibility
↳ *[R1.1, BR4]*

> Does your software respect the licences of dependencies it uses? How will you check that?

🟢 **Good answer (v0):**
```
The software license will respect the licenses of all its dependencies. 
We will check that by < > 
```

🟢 **Good answer (later versions):**
```
The software license respects the licenses of all its dependencies
```

🔗 **Resources:**

| Resource                                                                                                                                      | Description                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [The Turing Way guide on License Compatibility](https://book.the-turing-way.org/reproducible-research/licensing/licensing-compatibility.html) | A guide on how to checking if licenses are compatible with each other, including a permissions overview matrix            |
| [Various Licenses and Comments about Them](https://www.gnu.org/licenses/license-list.html)                                                    | A list of various licenses and information on compatibility and whether they qualify as FS and copyleft and compatibility |

_____________________________________________________________________________________________________________________


## Documentation

🔗 **Resources:**

| Resource                                                                               | Description                                                                                                                                            |
|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Write the Docs' guide on Software documentation](https://www.writethedocs.org/guide/) | Community wisdom on best practices for creating software documentation                                                                                 |
| [Sphinx](https://www.sphinx-doc.org/en/master/)                                        | A tool that makes it easy to create intelligent documentation (including API reference) using reStructuredText or MyST Markdown for various languages. |
| [MkDocs](https://www.mkdocs.org)                                                       | A fast and simple static site generator that's geared towards building project documentation using Markdown.                                           |
| [Redoc](https://redoc.ly)                                                              | An open-source documentation tool that generates API documentation from OpenAPI definitions.                                                           |

_____________________________________________________________________________________________________________________

### User documentation
↳ *[R1, BR2, BR6]*

> How will your software be documented for users?

🟢 **Good answer (v0):**
```
The user documentation will provide step-by-step installation, configuration, and usage instructions 
It will also include a tutorial to guide new users and input/output examples to demonstrate typical use cases
```

🟢 **Good answer (later versions):**
```
<link to user documentation> 
```

_____________________________________________________________________________________________________________________

### Deployment documentation
↳ *[R1, BR2]*

> How will you document the installation requirements of your software?
 
🟢 **Good answer (v0):**
```
The deployment documentation will outline system requirements, dependencies, and setup instructions for supported environments
It will also cover configuration steps and include detailed system requirements to ensure successful installation and deployment
```

🟢 **Good answer (later versions):**
```
<link to deployment documentation> 
```

_____________________________________________________________________________________________________________________

### Developer documentation
↳ *[R1, BR2, BR5]*

> How will your software be documented for future developers?

🟢 **Good answer (v0):**
```
The developer documentation will include an overview of the code structure and content 
It will also provide an API reference, contributing guidelines, and a code of conduct to support collaboration and maintain code quality
```

🟢 **Good answer (later versions):**
```
<link to developer documentation> 
```

_____________________________________________________________________________________________________________________

### API documentation
↳ *[BI3, R1, BR2]*

> How will you document functions or endpoints, and what format will be used (e.g., Sphinx, Swagger)?

🟢 **Good answer (v0):**
```
We will create an API reference using <Sphinx or some other tool> 
```

🟢 **Good answer (later versions):**
```
The API reference is included in the Developer documentation
```

_____________________________________________________________________________________________________________________

### Docstring/comments in the source code
↳ *[BI3, R1, BR2]*

> Will the source code include docstrings and comments?

🟢 **Good answer (v0):**
```
The source code will include in-line comments and docstrings
```

🟢 **Good answer (later versions):**
```
The source code includes docstrings and in-line comments
```

_____________________________________________________________________________________________________________________

### Tutorial
↳ *[R1, BR2]*

> Will you include a tutorial?
> If so, provide a summary of what it will cover.

🟢 **Good answer (v0):**
```
We will provide a basic tutorial to get users started with setup, configuration, and sample runs
The tutorial will be included in the User documentation
```

🟢 **Good answer (later versions):**
```
The tutorial is included in the User documentation
```

_____________________________________________________________________________________________________________________

### Contributing guidelines
↳ *[R1.2, BR2, BR5]*

> Will you include guidelines for contributing to the software? 
> If so, provide a summary of what they will cover.

🟢 **Good answer (v0):**
```
The repository will include a CONTRIBUTING file with instructions for code submissions, 
including <(e.g., coding standards, testing requirements)>
The contributing guidelines will be included in the Developer documentation
```

🟢 **Good answer (later versions):**
```
<link to CONTRIBUTING file> 
The contributing guidelines are included in the Developer documentation
```

🔗 **Resources:**

| Resource                                                                                                                                                                                           | Description                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [Setting guidelines for repository contributors (GitHub)](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors) | GitHub's instructions on including contributing guidelines to a repository |


_____________________________________________________________________________________________________________________

### Code of conduct
↳ *[BR2, BR5]*

> Will you include a code of conduct for contributors with standards for how to engage in a community?
> If so, provide a summary of what it will cover.

🟢 **Good answer (v0):**
```
The repository will include a CODE_OF_CONDUCT file with contributor behavior standards,
adopted from <Contributor Covenant v2.1 or other templates>
The code of conduct will be included in the Developer documentation
```

🟢 **Good answer (later versions):**
```
<link to CODE_OF_CONDUCT file> 
The code of conduct is included in the Developer documentation
```

🔗 **Resources:**

| Resource                                                                                                                                                                                | Description                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [Adding a code of conduct to your project (GitHub)](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project)  | GitHub's instructions on adding a code of conduct along with accessing templates |
| [Contributor Covenant](https://www.contributor-covenant.org)                                                                                                                            | A code of conduct template for open source projects                              |

_____________________________________________________________________________________________________________________

### Changelog
↳ *[F1.2, BF1, R1.2, BR2]*

> Will you include a changelog?
> If so, explain how version updates and changes will be tracked and note any specific format used

🟢 **Good answer (v0):**
```
The repository will include a CHANGELOG file with all release details and patch notes
```

🟢 **Good answer (later versions):**
```
<link to CHANGELOG file> 
```

🔗 **Resources:**

| Resource                                                                                                                                                                         | Description                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [Keep a changelog](https://keepachangelog.com/en/1.1.0/)                                                                                                                         | Style guide for changelogs                                                |
| [Common changelog](https://github.com/vweevers/common-changelog)                                                                                                                 | Adapted from and a stricter subset of "Keep a changelog" (resource above) |
| [A Beginner’s Guide to Git — What is a Changelog and How to Generate it](https://www.freecodecamp.org/news/a-beginners-guide-to-git-what-is-a-changelog-and-how-to-generate-it/) | A guide on how to generate a changelog using Git                          |

_____________________________________________________________________________________________________________________

### Release notes
↳ *[F1.2, BF1, R1.2, BR2]*

> Describe what information will be included in each release note, such as new features, fixes, and known issues

🟢 **Good answer (v0):**
```
The release notes will list version features, fixes, known issues, and improvements
```

🟢 **Good answer (later versions):**
```
The release notes are included in the [Software Releases](#software-releases)
```

🔗 **Resources:**

| Resource                                                                                                         | Description                                                                  |
|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| [About releases (GitHub)](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)   | GitHub's info on releases along with managing, creating, and automating them |

_____________________________________________________________________________________________________________________

### Bug reporting & feature request
↳ *[BR5, BR6]*

> Outline the process for reporting bugs or requesting features, 
> including where users can submit these and any templates to guide their input

🟢 **Good answer (v0):**
```
We will use GitHub (or Gitlab) issues with templates
```

🟢 **Good answer (later versions):**
```
<link to the Issues> 
```

🔗 **Resources:**

| Resource                                                                                                                                                                                                        | Description                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [About issues (GitHub)](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)                                                                                                          | GitHub's info on issues along with configuring, using, and administering them |
| [Configuring issue templates for your repository (GitHub)](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository) | GitHub's instructions on creating and configuring issue templates             |

_____________________________________________________________________________________________________________________

## Testing & quality assurance

🔗 **Resources:**

| Resource                                                                                                                                                  | Description                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [The Turing Way guide on good practice for testing](https://the-turing-way.netlify.app/reproducible-research/testing/testing-guidance.html)               | General guidance that applies to all types of testing                                                   |
| [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)                                                               | A guide on how to structure your tests for maximum efficiency and effectiveness with practical examples |
| [Testing with pytest. Unit, Integration and Smoke tests. (**Python**)](https://ucldevs.hashnode.dev/testing-with-pytest-unit-integration-and-smoke-tests) | A guide on how to use pytest for testing your **Python** software                                       |

_____________________________________________________________________________________________________________________

### Smoke tests
↳ *[R3, BR3]*

> How will you make sure that critical parts of the software work?
> Describe which parts of the software are most critical and will be covered by smoke tests to ensure they work as expected.

🟢 **Good answer (v0):**
```
We will write smoke tests to ensure the critical parts of the software do not fail
```

🟢 **Good answer (later versions):**
```
<link to smoke tests> 
```

_____________________________________________________________________________________________________________________

### Utility tests / doctests
↳ *[R3, BR2, BR3]*

> How will you show the expected working examples of components (functions, methods)?

🟢 **Good answer (v0):**
```
We will create doctests in the documentation to show implementation examples
```

🟢 **Good answer (later versions):**
```
The API reference includes the doctests
```

🔗 **Resources:**

| Resource                                                                                         | Description                                   |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------|
| [doctest — Test interactive **Python** examples](https://docs.python.org/3/library/doctest.html) | Official **Python** documentation on doctests |

_____________________________________________________________________________________________________________________

### Unit tests
↳ *[R3, BR3]*

> How will you make sure components (functions, methods) of the software work as expected?
> Specify the core functions covered by unit tests and the framework or tools used. 
> Mention integration with CI/CD if relevant.

🟢 **Good answer (v0):**
```
We will create unit tests for core functions using <pytest or some other tool>  
and link them to a CI/CD pipeline
```

🟢 **Good answer (later versions):**
```
<link to unit tests> 
The tests are linked to the CI/CD pipeline
```

_____________________________________________________________________________________________________________________

### Integration / system tests
↳ *[R3, BR3]*

> How will you make sure that the combination of components and the software as a whole function as expected?
> Describe the scenarios covered by integration tests and how they validate that components work together properly.
> Mention integration with CI/CD if relevant.

🟢 **Good answer (v0):**
```
We will create integration and system tests for the software using <pytest or some other tool>  
and link them to a CI/CD pipeline
```

🟢 **Good answer (later versions):**
```
<link to integration and system tests> 
The tests are linked to the CI/CD pipeline
```

_____________________________________________________________________________________________________________________

### Regression tests
↳ *[R3, BR3]*

> How will you make sure that new changes do not break existing functionality?
> Describe the scenarios covered by regression tests and how they validate that new changes do not break existing functionality.
> Mention integration with CI/CD if relevant.

🟢 **Good answer (v0):**
```
We will create regression tests for the software using <pytest or some other tool>
and link them to a CI/CD pipeline
```

🟢 **Good answer (later versions):**
```
<link to regression tests> 
The tests are linked to the CI/CD pipeline
```

🔗 **Resources:**

| Resource                                                                                                                                                                                             | Description                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| [Plan your regression testing strategy by asking the relevant questions](https://community.atlassian.com/t5/Jira-articles/Plan-your-regression-testing-strategy-by-asking-the-relevant/ba-p/1158403) | A guide on how to plan your regression testing strategy |

_____________________________________________________________________________________________________________________

### Code quality standards
↳ *[BI3, R3, BR3]*

> Do you follow specific software quality guidelines? If yes, which ones? 
> Does your code adhere to relevant code quality standards (styling, modularity, etc.)?

🟢 **Good answer (v0):**
```
We will follow <PEP 8 or some other standards> for code quality
```

🟢 **Good answer (later versions):**
```
Code quality standards applied: <PEP 8 or some other standard>
```

🔗 **Resources:**

| Resource                                                                                       | Description                                                                                                             |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [OpenSSF Best Practices Badge Program](https://bestpractices.coreinfrastructure.org/en)        | Self-certifying badge is a way for Free/Libre and Open Source Software projects to show that they follow best practices |
| [**Python** Code Quality: Tools & Best Practices](https://realpython.com/python-code-quality/) | A guide on how to improve the quality of your **Python** code                                                           |
| [Stylized presentation: PEP 8 — the Style Guide for **Python** Code](https://pep8.org)         | A presentation of the **Python** Enhancement Proposal 8, which is the Style Guide for **Python** Code                   |
| [PEP 8 – Style Guide for **Python** Code](https://peps.python.org/pep-0008/)                   | The official **Python** Style Guide                                                                                     |

_____________________________________________________________________________________________________________________

### Linting
↳ *[BI3, R3]*

> How will you ensure that the code is clean and follows best practices?
> Specify the tools used for linting and the rules enforced.

🟢 **Good answer (v0):**
```
We will use <flake8 or some other tool> to lint the code and enforce <PEP 8 or quality standards> rules
```

🟢 **Good answer (later versions):**
```
We use <flake8 or some other tool> to lint the code and enforce <PEP 8 or quality standards> rules
```

_____________________________________________________________________________________________________________________

### Sample data/parameters
↳ *[R1, BR2]*

> Will you provide sample data or parameters for testing the software?
> If yes, describe the type of data or parameters that will be provided.

🟢 **Good answer (v0):**
```
<Sample data / parameters> will be provided for testing basic functionality
```

🟢 **Good answer (later versions):**
```
<link to sample data / parameters> 
```
_____________________________________________________________________________________________________________________


## Interoperability

_____________________________________________________________________________________________________________________

### Programming languages
↳ *[I1, BI3]*

> List the programming languages used and explain why each is included in the software.

🟢 **Good answer (v0):**
```
The primary programming language will be <language> because <reason>
<If applicable, additional languages> will be used for <reason>
```

🟢 **Good answer (later versions):**
```
The primary programming language is <language>
<If applicable, additional languages> are used for <roles>
```

_____________________________________________________________________________________________________________________

### Input formats
↳ *[I1, BI3]*

> Describe the data input formats supported (e.g., JSON or CSV), and any requirements for structuring input data

🟢 **Good answer (v0):**
```
The software will accept <common formats>  formats
```

🟢 **Good answer (later versions):**
```
The software accepts <common formats>  formats
```

_____________________________________________________________________________________________________________________

### Output formats
↳ *[I1, BI3]*

> Specify the output formats available (e.g., JSON or CSV)

🟢 **Good answer (v0):**
```
The software will output <common formats>  formats
```

🟢 **Good answer (later versions):**
```
The software outputs <common formats>  formats
```

_____________________________________________________________________________________________________________________


## Versioning & release management

_____________________________________________________________________________________________________________________

### Version control system
↳ *[F1.1, F1.2, BF1, R1.2, R3]*

> Explain the version control system used and describe the approach to tagging releases and writing commit messages

🟢 **Good answer (v0):**
```
Git; every change will be documented with "Conventional Commits" and version tags
```

🟢 **Good answer (later versions):**
```
Git; every change is documented with "Conventional Commits" and version tags
```

🔗 Resources:

| Resource                                                               | Description                                                                      |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) | A specification for adding human and machine readable meaning to commit messages |

_____________________________________________________________________________________________________________________

### Versioning scheme
↳ *[F1.1, F1.2, BF1, BI3, R3]*

> Describe the chosen versioning scheme and how users can interpret version numbers

🟢 **Good answer (v0 + later versions):**
```
Semantic: MAJOR.MINOR.PATCH
```

_____________________________________________________________________________________________________________________


## Reproducibility & reuse

_____________________________________________________________________________________________________________________

### Packaging
↳ *[R3, BR1]*

> How will your software be packaged and distributed? 
> Do you use appropriate package managers to allow users to install/deploy your software with ease?

🟢 **Good answer (v0):**
```
The software will be packaged and distributed using <Conda or some other tool>
```

🟢 **Good answer (later versions):**
```
<link to entry in a packaging registry> 
```

🔗 **Resources:**

| Resource                                                                                                                                      | Description                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [The Turing Way guide on Package Management Systems - Conda](https://the-turing-way.netlify.app/reproducible-research/renv/renv-package.html) | A guide on how to use Conda to install and keep track of the different software packages (and their versions) |

_____________________________________________________________________________________________________________________

### Software releases
↳ *[BF1, R1.2, BR6]*

> How will you manage software releases and ensure that users can access previous versions?
> Outline the release strategy, including frequency, stability of each release, and channels where users can access releases.
> Describe how users can access previous versions of the software.

🟢 **Good answer (v0):**
```
Releases will be tagged using <Git tags or other tools> and made available in the repository's Releases page with stable, beta, and archived versions
```

🟢 **Good answer (later versions):**
```
<link to Releases> 
```

_____________________________________________________________________________________________________________________

### Dependencies
↳ *[I1, I2, BI1, BI2, R1, BR2]*

> Provide a detailed list of all dependencies, both language-specific and system-level, 
> along with required versions and compatibility notes.

🟢 **Good answer (v0):**
```
Language-specific dependencies  : <libraries, packages, and frameworks with versions (e.g., numpy ≥ 2.1)>       
System-level dependencies       : <system tools and utilities with versions (e.g., OpenSSL ≥ 3.4)>   
The dependencies will be detailed in the Deployment documentation                                          
```

🟢 **Good answer (later versions):**
```
The dependencies are detailed in the Deployment documentation                                        
```

_____________________________________________________________________________________________________________________

### System requirements
↳ *[BI2, R1, BR2]*

> Specify the hardware and operating system requirements necessary to run the software

🟢 **Good answer (v0):**
```
Supported operating systems       : macOS <version>+, Ubuntu <version>+, Windows <version>+       
Special computing requirements    : <special hardware or configuration requirements (e.g., GPU)>  
Minimum processor requirements    : <processor type>, <clock speed> GHz+                          
Minimum memory requirements       : <RAM size> GB                                                
Minimum storage requirements      : <storage size> GB    
The system requirements will be detailed in the Deployment documentation                                         
```

🟢 **Good answer (later versions):**
```
The system requirements are detailed in the Deployment documentation
```

_____________________________________________________________________________________________________________________

### Input/output examples
↳ *[BR2]*

> Are you providing input/output examples to ensure reproducibility of your software?

🟢 **Good answer (v0):**
```
We will provide input/output examples that cover <common use cases> for reproducibility
The examples will be included in the User documentation
```

🟢 **Good answer (later versions):**
```
<link to input/output examples> 
The examples are included in the User documentation
```

_____________________________________________________________________________________________________________________
