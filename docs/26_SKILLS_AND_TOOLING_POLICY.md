# 26 — Skills and Tooling Policy

**Document:** `26_SKILLS_AND_TOOLING_POLICY.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Skills, Tools, Plugins, External Capabilities, Installation, Permissions, Security, Validation & Governance Specification
**Status:** `APPROVED_AS_BASELINE_SKILLS_AND_TOOLING_POLICY`
**Authority:** Baseline specification for discovering, evaluating, installing, configuring, using, validating, monitoring, updating, restricting, and retiring skills, tools, plugins, libraries, providers, and external capabilities used by the project.

---

# 1. Purpose

This document defines how the project discovers and uses external capabilities required for:

* development,
* research,
* SEO analysis,
* AI execution,
* data acquisition,
* testing,
* debugging,
* design,
* deployment,
* observability,
* project management.

The project must not assume that every required capability needs to be implemented manually.

When an appropriate skill, tool, library, plugin, provider, or integration already exists, the system should evaluate whether it can safely and appropriately use it.

The central principle is:

```text
Identify Capability
        ↓
Discover Existing Tools / Skills
        ↓
Evaluate Suitability
        ↓
Check Permission
        ↓
Install / Enable if Allowed
        ↓
Validate
        ↓
Use
        ↓
Observe
        ↓
Document
        ↓
Maintain / Replace / Retire
```

---

# 2. Core Principle

The project follows:

```text
Build What Is Strategic
Use What Is Commodity
Integrate What Is Specialized
Verify Everything
```

The existence of a tool does not automatically make it appropriate.

The project must evaluate:

* correctness,
* security,
* reliability,
* maintainability,
* compatibility,
* cost,
* licensing,
* vendor dependency,
* data handling,
* operational complexity.

---

# 3. Definition of Skill

A **Skill** is a reusable capability that enables an AI agent or development workflow to perform a defined class of work.

Examples:

```text
SEO Research Skill
SERP Analysis Skill
Web Research Skill
Database Debugging Skill
Testing Skill
Frontend Design Skill
Documentation Skill
```

A skill may internally use:

* prompts,
* tools,
* APIs,
* libraries,
* scripts,
* workflows,
* models.

---

# 4. Definition of Tool

A **Tool** is an executable capability available to an agent, workflow, application, or developer.

Examples:

```text
Web Search
SERP API
HTTP Client
Database Client
File System
Git
Browser Automation
Crawler
Vector Search
LLM Provider
Analytics API
```

---

# 5. Definition of Plugin

A **Plugin** is an externally packaged integration that extends the environment or application with additional functionality.

A plugin may provide:

* tools,
* APIs,
* UI functionality,
* external service access,
* specialized workflows,
* data connectors.

Plugins must follow the same security and validation requirements as other tools.

---

# 6. Definition of Provider

A **Provider** is an external service supplying a capability or data source.

Examples:

```text
LLM Provider
Search Provider
SERP Provider
SEO Data Provider
Crawler Provider
Analytics Provider
Storage Provider
Embedding Provider
```

Providers must be accessed through application-level abstractions where practical.

---

# 7. Definition of Library

A **Library** is a software dependency incorporated into the project codebase.

Libraries differ from runtime tools because they become part of the application's dependency graph.

They therefore require:

* version control,
* compatibility testing,
* security review,
* license review,
* update policy.

---

# 8. Capability Classification

Every external capability should be classified as one or more of:

```text
SKILL
TOOL
PLUGIN
LIBRARY
PROVIDER
SERVICE
SCRIPT
MODEL
DATA SOURCE
```

Classification should be explicit.

---

# 9. Tool Registry

The project should maintain a capability registry.

Conceptually:

```yaml
capability:
  id:
  name:
  type:
  purpose:
  provider:
  version:
  status:
  capabilities:
  permissions:
  data_access:
  dependencies:
  cost:
  license:
  security_status:
  validation_status:
  owner:
  documentation:
```

---

# 10. Capability Lifecycle

Every capability follows:

```text
DISCOVERED
    ↓
EVALUATED
    ↓
APPROVED
    ↓
INSTALLED / ENABLED
    ↓
VALIDATED
    ↓
ACTIVE
    ↓
MONITORED
    ↓
UPDATED / REPLACED / SUSPENDED
    ↓
RETIRED
```

---

# 11. Discovery

When a task requires a capability, the AI or developer should first determine:

1. What capability is required?
2. Is it already available?
3. Is it already implemented?
4. Is there an approved internal abstraction?
5. Does an appropriate external capability exist?
6. Is installation permitted?
7. What are the risks?

---

# 12. Capability Discovery Rule

Do not immediately install a new tool.

Preferred sequence:

```text
Existing Project Capability
        ↓
Existing Approved Tool
        ↓
Existing Skill
        ↓
Existing Library
        ↓
Approved Provider
        ↓
New External Capability
        ↓
Build Internally
```

The final order may change when security, cost, or strategic requirements justify it.

---

# 13. When to Use an Existing Capability

Prefer an existing capability when it:

* solves the required problem adequately,
* is maintained,
* is compatible,
* is sufficiently secure,
* has acceptable cost,
* does not violate architecture,
* does not create unacceptable vendor lock-in.

---

# 14. When to Build Internally

Build internally when:

* the capability is strategically differentiating,
* external options are inadequate,
* integration complexity exceeds implementation cost,
* security requirements cannot be satisfied externally,
* provider independence requires a custom abstraction,
* the functionality is simple enough to own safely.

---

# 15. Strategic vs Commodity Capabilities

Examples of potentially strategic capabilities:

```text
SEO Knowledge Model
SEO Decision Engine
Topic/Page Mapping Logic
Business Relevance Scoring
SEO-specific Reasoning Rules
Living SEO Intelligence Model
```

Examples of commodity capabilities:

```text
HTTP Requests
Queue Infrastructure
Database Driver
Logging
Basic Validation
Generic Authentication Components
```

The project should avoid unnecessarily reinventing commodity infrastructure.

---

# 16. Tool Suitability Evaluation

Before adoption, evaluate:

```text
Functional Fit
Technical Fit
Security
Reliability
Maintenance
Performance
Cost
License
Data Handling
Privacy
Vendor Lock-in
Observability
Testing
Documentation
Community / Support
Migration Difficulty
```

---

# 17. Capability Evaluation Score

A capability may be evaluated using:

```yaml
evaluation:
  functional_fit:
  technical_fit:
  security:
  reliability:
  maintenance:
  performance:
  cost:
  licensing:
  privacy:
  vendor_lock_in:
  observability:
  testability:
  documentation:
  migration_risk:
  overall:
```

Exact scoring methodology may evolve.

Scores are decision-support signals, not automatic approval.

---

# 18. Permission Model

External capabilities must have explicit permission boundaries.

Suggested levels:

```text
LEVEL 0 — DISCOVERY ONLY
LEVEL 1 — READ
LEVEL 2 — ANALYSIS
LEVEL 3 — WRITE TO TEMPORARY STATE
LEVEL 4 — WRITE TO PROJECT STATE
LEVEL 5 — EXTERNAL ACTION
```

Higher levels require stronger authorization.

---

# 19. Least Privilege

A capability should receive only the permissions required for its task.

For example:

A SERP analysis tool may need:

```text
READ:
  search query
  SERP response
```

It should not automatically receive:

```text
WRITE:
  project configuration
  credentials
  production database
```

---

# 20. Installation Permission

Claude or another authorized AI coding agent may install and use required skills/tools when project policy permits it.

However:

```text
Permission to install
    ≠
Permission to execute unrestricted actions
```

Installation and runtime authorization are separate controls.

---

# 21. AI-Driven Skill Installation

When the AI identifies a missing capability:

```text
Task
 ↓
Capability Requirement
 ↓
Skill/Tool Discovery
 ↓
Security / Compatibility Evaluation
 ↓
Permission Check
 ↓
Installation
 ↓
Validation
 ↓
Registration
 ↓
Use
```

The AI must not silently install arbitrary software when project policy or environment permissions prohibit it.

---

# 22. Installation Record

Every installed capability should be recorded.

```yaml
installation:
  capability_id:
  package:
  version:
  source:
  installed_at:
  installer:
  reason:
  permissions:
  dependencies:
  validation:
  rollback:
```

---

# 23. Source Trust

Prefer capability sources in this general order:

```text
Official / Trusted Source
        ↓
Well-Maintained Open Source Repository
        ↓
Verified Package Registry
        ↓
Trusted Community Source
        ↓
Unknown Source
```

Unknown sources require heightened scrutiny.

---

# 24. Supply Chain Security

Before installing software, consider:

* package authenticity,
* repository trust,
* maintainer reputation,
* dependency tree,
* known vulnerabilities,
* suspicious install scripts,
* typosquatting,
* abandoned packages,
* malicious updates,
* license.

---

# 25. Dependency Security

Libraries and tools must be checked for known vulnerabilities where practical.

The project should support:

```text
Dependency Audit
Lock Files
Version Pinning / Ranges
Security Alerts
Update Review
Rollback
```

---

# 26. Version Policy

Dependencies should not be updated blindly.

Updates should consider:

```text
Security
Bug Fixes
Compatibility
Performance
Breaking Changes
Transitive Dependencies
Test Results
```

---

# 27. Locking and Reproducibility

Production-critical dependencies should have reproducible versions.

The project should maintain appropriate lock files and version metadata.

A development environment should be reproducible from project configuration.

---

# 28. Tool Configuration

Configuration should be separated from source code where appropriate.

Examples:

```text
API Keys
Provider URLs
Model Names
Rate Limits
Feature Flags
Environment Settings
```

Secrets must never be committed to source control.

---

# 29. Secret Management

Secrets should be stored using approved secret-management mechanisms.

Never:

* hardcode API keys,
* place credentials in prompts,
* commit `.env` secrets,
* expose tokens in logs,
* include secrets in AI context unnecessarily.

---

# 30. Tool Data Boundaries

Every tool should define:

```yaml
data_access:
  reads:
  writes:
  sends_externally:
  stores:
  retains:
```

This is particularly important for AI tools and external providers.

---

# 31. External Data Transmission

Before sending project data to an external provider, determine:

* what data is sent,
* why it is needed,
* whether it contains sensitive information,
* where it is processed,
* how long it may be retained,
* whether the provider is approved.

---

# 32. AI Provider Policy

LLM providers must be accessed through an abstraction where practical.

Application code should not be tightly coupled to one vendor-specific implementation.

Conceptually:

```text
Application
    ↓
LLM Interface
    ↓
Model Router
    ↓
Provider Adapter
    ↓
External Model
```

---

# 33. Model Selection

Model selection should consider:

```text
Task Complexity
Quality Requirements
Latency
Cost
Context Capacity
Structured Output Support
Tool Calling
Language Support
Privacy
Reliability
```

The most powerful model is not automatically the correct model.

---

# 34. Search and SERP Tools

Search tools should be abstracted behind provider interfaces.

Example:

```text
SearchProvider
SERPProvider
KeywordDataProvider
TrendProvider
```

This supports:

* provider replacement,
* testing with mocks,
* fallback providers,
* cost optimization.

---

# 35. Tool Output Contracts

Tool outputs must be structured.

Conceptually:

```yaml
tool_result:
  tool_id:
  version:
  status:
  data:
  metadata:
  evidence:
  warnings:
  errors:
  retrieved_at:
```

Tool outputs must not bypass output validation.

---

# 36. Tool Failure

External tools can fail because of:

```text
Timeout
Rate Limit
Authentication
Quota
Provider Outage
Malformed Response
Schema Change
Network Failure
Partial Response
Stale Data
```

The system must represent these explicitly.

---

# 37. No Fabricated Tool Results

If a tool fails:

```text
TOOL_FAILED
```

must not become:

```text
TOOL_SUCCEEDED
```

through AI inference.

The AI may provide an estimate only if explicitly allowed by the relevant contract and must label it accordingly.

---

# 38. Tool Fallbacks

Fallbacks may be used when:

* an approved alternative exists,
* the fallback satisfies quality requirements,
* provenance remains intact,
* the user/project policy permits it.

Example:

```text
Primary SERP Provider
        ↓ failure
Approved Secondary Provider
        ↓ failure
Partial / Unknown
```

---

# 39. Tool Timeouts and Budgets

Every external capability should have reasonable:

* timeout,
* retry count,
* concurrency limit,
* cost budget,
* rate limit.

These values should be configurable.

---

# 40. Retry Policy

Retries should distinguish:

```text
TRANSIENT
PERMANENT
UNKNOWN
```

Retry:

```text
Timeout
Temporary network error
Rate limit with retry-after
```

Do not blindly retry:

```text
Invalid API key
Invalid request
Permission denied
Unsupported operation
```

---

# 41. Idempotency

Write-capable tools must support idempotency where practical.

Repeated execution should not accidentally create duplicate:

* records,
* payments,
* external actions,
* jobs,
* artifacts.

---

# 42. Tool Authorization

The Orchestrator should authorize tool execution.

Conceptually:

```text
Task
 ↓
Agent
 ↓
Required Capability
 ↓
Permission Check
 ↓
Tool Invocation
```

Agents should not arbitrarily acquire new permissions during execution.

---

# 43. Tool Selection

The Orchestrator may select tools based on:

```text
Capability Match
Permission
Availability
Cost
Latency
Quality
Reliability
Provider Health
Task Requirements
```

---

# 44. Skill Selection

Similarly:

```text
Task
 ↓
Required Capability
 ↓
Skill Registry
 ↓
Compatible Skills
 ↓
Permission / Security
 ↓
Selected Skill
```

---

# 45. Skill Composition

Skills may compose.

Example:

```text
Business Research
      ↓
Entity Extraction
      ↓
Topic Discovery
      ↓
SERP Intelligence
      ↓
Decision Support
```

Composition must happen through explicit workflow or orchestration boundaries.

---

# 46. No Hidden Skill Behavior

A skill must clearly declare:

* what it does,
* what it requires,
* what tools it uses,
* what data it accesses,
* what it produces,
* what permissions it needs,
* what failures it can produce.

---

# 47. Skill Versioning

Skills must be versioned.

Changes may affect:

* prompts,
* retrieval,
* tool usage,
* output quality,
* behavior,
* cost.

Therefore skill versions should be traceable in AI execution metadata.

---

# 48. Prompt and Skill Versioning

For important AI executions, record:

```text
Skill Version
Prompt Version
Model Version
Tool Versions
Output Contract Version
Context Package Version
```

This enables evaluation and debugging.

---

# 49. Tool and Skill Testing

Every important capability should have appropriate tests.

### Unit

Internal deterministic logic.

### Contract

Input/output structure.

### Integration

Actual provider communication.

### Mock

Offline provider behavior.

### Security

Permissions and data boundaries.

### Failure

Timeouts, malformed responses, provider errors.

### Regression

Behavior after upgrades.

---

# 50. Capability Validation

Before production use:

```text
Installed
    ↓
Configured
    ↓
Smoke Tested
    ↓
Contract Validated
    ↓
Security Checked
    ↓
Performance Checked
    ↓
Approved
```

---

# 51. Smoke Test

A smoke test should verify that the capability:

* starts,
* authenticates where required,
* performs its basic function,
* returns expected structure,
* respects basic permissions.

A smoke test is not sufficient proof of production readiness.

---

# 52. Provider Contract Testing

Provider integrations should have contract tests for:

* request shape,
* response shape,
* required fields,
* error responses,
* pagination,
* rate-limit behavior,
* authentication failures.

---

# 53. Mock Providers

The project should provide mock implementations for important external dependencies.

Examples:

```text
MockLLMProvider
MockSearchProvider
MockSERPProvider
MockEmbeddingProvider
MockAnalyticsProvider
```

This enables deterministic development and testing.

---

# 54. Real Provider Verification

Mocks cannot prove real integration correctness.

Production readiness requires appropriate runtime verification against real providers in an authorized environment.

The project must distinguish:

```text
MOCK VERIFIED
```

from:

```text
REAL PROVIDER VERIFIED
```

---

# 55. Tool Observability

Important tool calls should capture:

```text
Tool ID
Version
Execution ID
Task ID
Agent ID
Start Time
Duration
Status
Retry Count
Cost
Provider
Error Type
```

Sensitive payloads should not be logged unnecessarily.

---

# 56. Tool Health

The system may track:

```text
Availability
Latency
Error Rate
Rate Limits
Quota
Cost
Quality
Schema Stability
```

Provider health can influence tool selection.

---

# 57. Tool Cost Management

Tool selection should consider cost.

Example:

```text
Cheap deterministic operation
        ↓
Preferred

Expensive AI operation
        ↓
Used when justified
```

Cost must not override required quality or evidence.

---

# 58. Tool Rate Limits

The system should respect provider limits.

Possible controls:

* token buckets,
* concurrency limits,
* queueing,
* exponential backoff,
* retry-after handling,
* request batching.

---

# 59. Tool Caching

Cache safe, repeatable results where appropriate.

Examples:

```text
SERP snapshots
Search metrics
Embedding results
Static metadata
Provider capability information
```

Cache must preserve freshness metadata.

---

# 60. Tool Data Freshness

Every external data result should record when it was retrieved.

```yaml
freshness:
  retrieved_at:
  source_updated_at:
  expires_at:
  freshness_policy:
```

Freshness requirements depend on the task.

---

# 61. Tool Result Provenance

Tool results should preserve:

```text
Provider
Endpoint / Capability
Request Context
Retrieval Time
Provider Version
Tool Version
Raw Reference
Normalized Result
```

This supports evidence-backed SEO decisions.

---

# 62. Web Research Tools

When web research is used, the system should distinguish:

```text
Source Discovery
Source Retrieval
Source Extraction
Source Validation
Source Citation
```

The AI must not treat every web result as equally authoritative.

---

# 63. Crawling Tools

Crawlers must respect:

* authorization,
* robots policies where applicable,
* rate limits,
* site stability,
* legal requirements,
* crawl scope,
* privacy boundaries.

Crawler configuration should be explicit.

---

# 64. Browser Automation

Browser automation is higher-risk than read-only API access because it may perform external actions.

It should require explicit authorization for consequential operations.

Examples:

```text
Read public page
```

is fundamentally different from:

```text
Submit form
Publish content
Delete resource
Change account setting
```

---

# 65. External Actions

External actions should use:

```text
Explicit Authorization
+
Strong Validation
+
Idempotency
+
Audit Trail
+
Rollback Where Possible
```

The AI must not silently perform consequential actions.

---

# 66. Human Approval

Human approval should normally be required for high-impact external actions such as:

* publishing,
* deleting,
* changing production configuration,
* changing billing,
* modifying important project state,
* sending consequential communications.

Exact policy may be refined per capability.

---

# 67. Capability Risk Levels

Suggested:

```text
R0 — READ-ONLY / LOW RISK
R1 — ANALYSIS
R2 — INTERNAL WRITE
R3 — EXTERNAL WRITE
R4 — HIGH-IMPACT EXTERNAL ACTION
```

Higher risk requires stronger controls.

---

# 68. Risk-Based Controls

| Risk | Typical Control                                         |
| ---- | ------------------------------------------------------- |
| R0   | Basic permission                                        |
| R1   | Tool authorization                                      |
| R2   | Validation + audit                                      |
| R3   | Explicit authorization + idempotency                    |
| R4   | Human approval + strong audit + rollback where possible |

---

# 69. Tool Isolation

Where practical, risky tools should execute in isolated environments.

Examples:

```text
Sandbox
Restricted Worker
Container
Separate Process
Read-only Environment
```

The exact implementation depends on deployment architecture.

---

# 70. Tool Execution Context

Every tool execution should know:

```text
Tenant
Project
User / Actor
Task
Workflow
Agent
Permissions
Environment
```

This supports isolation and auditability.

---

# 71. Plugin Security

Plugins must be treated as potentially privileged extensions.

Before enabling:

```text
Review Permissions
Review Network Access
Review File Access
Review Data Access
Review Dependencies
Review Maintenance
Review Update Mechanism
```

---

# 72. Plugin Removal

Plugins should be removable without corrupting core project state.

The architecture should avoid making the entire application dependent on one optional plugin.

---

# 73. Provider Independence

Provider-specific code should remain at integration boundaries.

Preferred:

```text
Domain Logic
      ↓
Application Interface
      ↓
Provider Adapter
      ↓
External Provider
```

Avoid:

```text
Domain Logic
      ↓
Provider-Specific SDK Everywhere
```

---

# 74. Vendor Lock-In

The project should actively monitor lock-in risk.

Risk increases when:

* provider-specific data models leak into the domain,
* prompts depend on one model's undocumented behavior,
* application logic depends on one API,
* migration becomes prohibitively expensive.

---

# 75. Migration Readiness

Critical providers should have:

* adapters,
* normalized internal contracts,
* provider metadata,
* mock implementations,
* integration tests,
* migration notes.

---

# 76. Tool Deprecation

A capability may be deprecated because of:

* security issues,
* maintenance failure,
* excessive cost,
* poor quality,
* provider shutdown,
* incompatibility,
* superior alternative.

Deprecation should be documented.

---

# 77. Tool Replacement

Replacement procedure:

```text
Evaluate Replacement
      ↓
Implement Adapter
      ↓
Run Contract Tests
      ↓
Run Regression Tests
      ↓
Compare Quality
      ↓
Shadow / Staged Validation
      ↓
Switch
      ↓
Monitor
      ↓
Retire Old Provider
```

---

# 78. Skills and Context Management

Skills should declare their context requirements.

Example:

```yaml
skill:
  id: serp-intelligence

  required_context:
    - search_context
    - query
    - topic
    - entity_context

  optional_context:
    - historical_serp
```

The Context Management system should assemble the minimum sufficient context.

---

# 79. Skills and Output Contracts

Every skill producing structured results should use an appropriate output contract.

```text
Skill
 ↓
Structured Result
 ↓
Output Contract Validation
 ↓
Evidence Validation
 ↓
Canonical State
```

A skill must not directly bypass the validation pipeline.

---

# 80. Skills and Human-in-the-Loop

Skills may produce:

```text
Observation
Inference
Recommendation
```

but strategic decisions remain governed by the Human-in-the-Loop model.

---

# 81. Skills and Agents

Skills are capabilities.

Agents are task-oriented execution units.

A single agent may use multiple skills.

```text
Agent
 ├── Skill A
 ├── Skill B
 └── Tool C
```

The Orchestrator controls composition.

---

# 82. Skills and Workflows

Workflows may invoke skills explicitly.

Example:

```text
Research Workflow
    ↓
Business Research Skill
    ↓
Entity Skill
    ↓
Topic Discovery Skill
    ↓
SERP Skill
```

Skill dependencies should be explicit.

---

# 83. Skills and Decision Engine

Skills provide analysis.

The Decision Engine combines:

```text
Business Context
+
Search Reality
+
Knowledge
+
Evidence
+
Constraints
+
AI Analysis
```

into decision support.

Skills must not independently override strategic decisions.

---

# 84. Skill Discovery by AI

The AI may determine:

> This task requires capability X.

It may then search the approved capability ecosystem.

The AI should compare alternatives rather than blindly selecting the first result.

---

# 85. Automatic Installation Boundaries

Automatic installation may be allowed when:

* the capability is explicitly permitted,
* the source is trusted,
* security checks pass,
* compatibility is acceptable,
* installation does not modify protected systems unexpectedly.

Otherwise the AI must stop and request authorization.

---

# 86. Environment Constraints

Tool installation must respect:

```text
Operating System
Python Version
Node Version
Package Manager
Database Version
Runtime
CI Environment
Deployment Environment
```

A tool that works locally but cannot run in production is not automatically acceptable.

---

# 87. Environment Parity

Where practical:

```text
Development
≈
CI
≈
Staging
≈
Production
```

Differences must be documented.

---

# 88. Documentation Requirement

Every important capability should have documentation covering:

* purpose,
* installation,
* configuration,
* permissions,
* usage,
* inputs,
* outputs,
* errors,
* limits,
* security,
* testing,
* maintenance,
* removal.

---

# 89. Capability Registry Documentation

The registry should answer:

> What capabilities are available right now?

At minimum:

```text
Capability
Version
Purpose
Status
Permissions
Provider
Dependencies
Validation
Owner
Documentation
```

---

# 90. Capability Status

Recommended statuses:

```text
DISCOVERED
EVALUATING
APPROVED
INSTALLING
INSTALLED
VALIDATING
ACTIVE
DEGRADED
SUSPENDED
DEPRECATED
RETIRED
REJECTED
```

---

# 91. Tool Governance

The project should periodically review:

* unused tools,
* duplicate capabilities,
* outdated dependencies,
* excessive provider costs,
* security findings,
* tool failures,
* capability overlap.

The goal is a lean capability ecosystem.

---

# 92. Duplicate Capability Policy

Avoid unnecessary duplicates.

For example, if five tools perform essentially the same task, maintain only those justified by:

* fallback,
* quality,
* cost,
* regional availability,
* specialization,
* resilience.

---

# 93. Capability Ownership

Every production-critical capability should have an owner or responsible module.

Ownership includes:

* maintenance,
* versioning,
* validation,
* incident handling,
* deprecation.

---

# 94. Tool Incident Management

A tool incident should record:

```text
Capability
Time
Environment
Failure
Impact
Provider
Affected Workflows
Mitigation
Root Cause
Resolution
Regression Prevention
```

---

# 95. Tool Quality Monitoring

Important capabilities should have quality metrics.

Examples:

```text
Success Rate
Error Rate
Latency
Cost per Execution
Data Completeness
Schema Validity
Semantic Accuracy
Provider Drift
User Correction Rate
```

---

# 96. Capability Drift

A provider may change behavior without changing its API.

Examples:

* SERP result composition changes,
* model behavior changes,
* output ranking changes,
* API semantics change.

Therefore capability validation must include behavioral monitoring, not only schema compatibility.

---

# 97. Model Drift

AI model changes can affect:

* classifications,
* clustering,
* recommendations,
* structured outputs,
* confidence.

Model changes require regression evaluation.

---

# 98. Prompt Drift

Prompt modifications are code-level behavioral changes.

Important prompt changes require:

```text
Version
Evaluation
Regression
Documentation
```

---

# 99. Tool Output Drift

If a provider changes output:

```text
Provider
 ↓
Adapter
 ↓
Contract Validation
 ↓
Failure / Compatibility Handling
```

The application must not silently accept structurally or semantically invalid data.

---

# 100. Capability Testing Matrix

| Capability Type | Required Testing                         |
| --------------- | ---------------------------------------- |
| Skill           | Contract + behavioral + regression       |
| Tool            | Integration + failure + security         |
| Plugin          | Security + integration + compatibility   |
| Library         | Unit + integration + security            |
| Provider        | Contract + integration + failure         |
| Model           | Golden dataset + evaluation + regression |
| Data Source     | Schema + freshness + provenance          |

---

# 101. Development Workflow

When implementing a task:

```text
Task
 ↓
Identify Required Capabilities
 ↓
Check Registry
 ↓
Reuse Existing Capability
 ↓
Install / Configure Missing Capability if Authorized
 ↓
Implement
 ↓
Test
 ↓
Validate
 ↓
Document
```

---

# 102. Debugging Workflow

When a tool-related failure occurs:

```text
Detect
 ↓
Reproduce
 ↓
Collect Evidence
 ↓
Classify
 ↓
Determine Whether Failure Is:
   - Application
   - Tool
   - Provider
   - Configuration
   - Network
   - Permission
   - Data
   - Contract
 ↓
Identify Root Cause
 ↓
Fix
 ↓
Targeted Test
 ↓
Regression Test
 ↓
Verify
 ↓
Document
```

---

# 103. Do Not Blame the Tool Automatically

An external tool failure does not prove that the tool is defective.

Investigate:

```text
Input
Configuration
Credentials
Permissions
Network
Provider
Adapter
Application Logic
Output Validation
```

---

# 104. Do Not Blame the AI Automatically

AI output problems may originate from:

* insufficient context,
* poor retrieval,
* incorrect tool data,
* invalid contract,
* stale knowledge,
* ambiguous task,
* model limitations.

The entire pipeline must be evaluated.

---

# 105. Tool and Skill Evaluation Evidence

A capability should not be marked:

```text
VERIFIED
```

without evidence.

Evidence may include:

```text
Test Result
Contract Validation
Security Review
Runtime Verification
Benchmark
Provider Response
Human Review
```

---

# 106. Verification States

Use the project's verification vocabulary:

```text
IMPLEMENTED
TESTED
VALIDATED
RUNTIME_VERIFIED
PARTIALLY_VERIFIED
UNVERIFIED
BLOCKED
```

A tool can be installed but still be:

```text
INSTALLED + UNVERIFIED
```

---

# 107. No False Completion

Never claim:

* tool works,
* integration is production-ready,
* provider is available,
* skill is validated,

unless the corresponding evidence exists.

---

# 108. Tool and Skill Security Checklist

Before activation:

```text
[ ] Trusted source
[ ] Known package/version
[ ] Dependency review
[ ] Permissions reviewed
[ ] Network access reviewed
[ ] File access reviewed
[ ] Data transmission reviewed
[ ] Secrets protected
[ ] Vulnerability status reviewed
[ ] Isolation evaluated
[ ] Logging reviewed
[ ] Rollback/removal possible
```

---

# 109. Tool and Skill Performance Checklist

Where relevant:

```text
[ ] Latency measured
[ ] Concurrency behavior tested
[ ] Rate limits understood
[ ] Cost measured
[ ] Timeout configured
[ ] Retry policy configured
[ ] Cache strategy defined
[ ] Failure behavior validated
```

---

# 110. Capability Adoption Decision

Adopt when:

```text
Capability Need
+
Adequate Functional Fit
+
Acceptable Security
+
Acceptable Cost
+
Acceptable Maintenance
+
Architecture Compatibility
+
Validation Evidence
```

Reject or defer when critical requirements fail.

---

# 111. Capability Rejection

A capability should be rejected when:

* security risk is unacceptable,
* source trust is insufficient,
* licensing is incompatible,
* data handling is unacceptable,
* architecture is violated,
* maintenance is unreliable,
* quality is inadequate,
* migration risk is excessive.

---

# 112. Temporary Capabilities

A capability may be used temporarily for research or experimentation.

Temporary capabilities must be marked:

```text
EXPERIMENTAL
```

and must not silently become production dependencies.

---

# 113. Experimental Isolation

Experimental tools should preferably be isolated from:

* production data,
* production credentials,
* canonical state,
* high-impact actions.

---

# 114. Capability Sunset

Retirement should include:

```text
Disable
 ↓
Migrate
 ↓
Remove Configuration
 ↓
Remove Dependencies
 ↓
Remove Permissions
 ↓
Archive Documentation
 ↓
Record Decision
```

---

# 115. Skills and Project Continuity

Installed capabilities must be recorded in persistent project documentation or registry.

A future AI session must not have to rediscover:

> Which tools were installed and why?

---

# 116. Skills and Context Continuity

The context package may include:

```text
Required Skill
Skill Version
Required Tools
Tool Versions
Permissions
Known Limitations
```

Only relevant capability information should be included.

---

# 117. Skills and Project Control

The Project Control Center should know:

```text
Active Capabilities
Blocked Capabilities
Pending Installations
Capability Risks
Capability Dependencies
Verification Status
```

---

# 118. Skills and Roadmap

A roadmap task may have capability dependencies.

Example:

```yaml
task:
  id:
  capability_dependencies:
    - serp-provider
    - llm-provider
    - browser-tool
```

A task should not begin if a mandatory capability is unavailable and no approved fallback exists.

---

# 119. Skills and Architecture

Capability integration must respect:

* system architecture,
* agent architecture,
* data architecture,
* technical architecture,
* output contracts,
* context management.

A tool must not introduce an architectural shortcut that bypasses established boundaries.

---

# 120. Skills and Testing Architecture

Every production-critical external capability should have an appropriate test strategy.

The test environment should support mocks so that most tests do not depend on:

* network access,
* paid APIs,
* unstable providers,
* external availability.

---

# 121. Skills and SEO Domain Integrity

Generic AI or SEO tools must not automatically define the project's SEO methodology.

The project's domain model remains authoritative.

External tools provide:

```text
Data
Capability
Evidence
Computation
```

The project's SEO Decision Engine determines how those inputs are interpreted within the product model.

---

# 122. Skills and Strategic Independence

The project must not become dependent on one tool for strategic reasoning.

For example:

```text
One Keyword API
≠
SEO Truth
```

and:

```text
One LLM
≠
SEO Strategy
```

The system should preserve internal domain representations.

---

# 123. Skills and Search Reality

External SEO tools provide observations.

The system must distinguish:

```text
Observed by Provider
        ↓
Normalized by System
        ↓
Analyzed by AI
        ↓
Interpreted by Decision Engine
        ↓
Validated by Human
```

---

# 124. Capability Decision Records

Significant capability decisions should produce an ADR or equivalent decision record.

Examples:

```text
Why Provider A was selected
Why Library B was rejected
Why Skill C was installed
Why Provider D was replaced
```

---

# 125. Capability Governance Board

The project does not require a separate organizational committee for MVP.

Instead, governance may be handled through:

```text
Project Control Center
+
Master Rules
+
Architecture
+
Capability Registry
+
Human Approval
```

Future organizational governance can be added if required.

---

# 126. MVP Capability Ecosystem

MVP should support at minimum:

```text
LLM Provider Abstraction
Search Provider Abstraction
SERP Provider Abstraction
Embedding Provider
Web Research
Database Tools
File / Repository Tools
Testing Tools
Observability Tools
Git / Version Control
```

The exact providers are implementation decisions.

---

# 127. MVP Installation Policy

For MVP:

1. Prefer existing approved capabilities.
2. Permit installation of missing capabilities when authorized.
3. Validate before production use.
4. Record versions.
5. Protect secrets.
6. Use mocks for external dependencies.
7. Preserve provider abstraction.
8. Never bypass output validation.
9. Never bypass authorization.
10. Never claim unverified integration success.

---

# 128. Future Capability Ecosystem

Future versions may add:

* capability marketplace,
* automatic capability recommendation,
* capability benchmarking,
* dynamic provider routing,
* automated provider health scoring,
* advanced sandboxing,
* capability policy engine,
* automated dependency remediation,
* capability cost optimization,
* capability A/B evaluation.

---

# 129. Anti-Patterns

### 129.1 Install Everything

Creates unnecessary attack surface.

### 129.2 Build Everything

Creates unnecessary engineering cost.

### 129.3 Trust the First Tool Found

Discovery is not validation.

### 129.4 Give Tools Full Access

Violates least privilege.

### 129.5 Put Provider SDKs Everywhere

Creates vendor coupling.

### 129.6 Treat Tool Output as Truth

Tool output is evidence/data, not automatically validated truth.

### 129.7 Skip Runtime Verification

Installation does not prove integration.

### 129.8 Use Production Credentials During Experiments

Creates unnecessary risk.

### 129.9 Hide Tool Usage

Important tool dependencies must be observable.

### 129.10 Let AI Install Arbitrary Software

Installation requires policy compliance and permission.

### 129.11 Let Tools Bypass Contracts

All important outputs must pass appropriate validation.

### 129.12 Treat One Provider as the SEO Authority

The product must remain methodologically independent.

---

# 130. Definition of Done

The Skills & Tooling system is complete when the project can:

* identify required capabilities,
* discover existing capabilities,
* evaluate alternatives,
* check installation permission,
* install authorized capabilities,
* record installations,
* version skills/tools/providers,
* define permissions,
* enforce least privilege,
* protect secrets,
* evaluate supply-chain risks,
* abstract providers,
* validate tool outputs,
* test integrations,
* use mock providers,
* verify real providers when required,
* monitor capability health,
* track cost,
* track freshness,
* detect provider drift,
* handle failures,
* retry safely,
* enforce idempotency,
* support fallback providers,
* record provenance,
* support capability replacement,
* retire capabilities safely,
* preserve project continuity,
* integrate with agents,
* integrate with workflows,
* integrate with context management,
* integrate with output contracts,
* integrate with testing,
* integrate with Project Control Center.

---

# 131. Final Skills & Tooling Operating Model

```text
TASK
  ↓
CAPABILITY REQUIREMENT
  ↓
DISCOVER EXISTING CAPABILITY
  ↓
CHECK REGISTRY
  ↓
EVALUATE OPTIONS
  ↓
SECURITY / COMPATIBILITY / COST REVIEW
  ↓
PERMISSION CHECK
  ↓
INSTALL / ENABLE
  ↓
REGISTER
  ↓
CONFIGURE
  ↓
SMOKE TEST
  ↓
CONTRACT VALIDATION
  ↓
SECURITY VALIDATION
  ↓
RUNTIME VALIDATION
  ↓
ACTIVE USE
  ↓
OBSERVABILITY
  ↓
QUALITY / COST / HEALTH MONITORING
  ↓
UPDATE / REPLACE / SUSPEND / RETIRE
```

---

# 132. Final Capability Principle

The project should neither:

```text
Build Everything
```

nor:

```text
Trust Everything
```

It should:

```text
Discover
→ Evaluate
→ Authorize
→ Integrate
→ Validate
→ Observe
→ Govern
```

External capabilities accelerate the project, but **the architecture, domain model, evidence standards, security boundaries, output contracts, and strategic decisions remain under project governance.**

---

# 133. Document Control

```yaml
document:
  id: "26"
  filename: "26_SKILLS_AND_TOOLING_POLICY.md"
  status: "APPROVED_AS_BASELINE_SKILLS_AND_TOOLING_POLICY"
  authority: "baseline_skills_tools_plugins_providers_libraries_and_external_capability_governance"

product:
  name: "SEO Research & Strategy Copilot / SEO Decision Engine"

capability_types:
  - skill
  - tool
  - plugin
  - library
  - provider
  - service
  - script
  - model
  - data_source

lifecycle:
  - discovered
  - evaluating
  - approved
  - installing
  - installed
  - validating
  - active
  - degraded
  - suspended
  - deprecated
  - retired
  - rejected

permission_levels:
  - "LEVEL_0_DISCOVERY_ONLY"
  - "LEVEL_1_READ"
  - "LEVEL_2_ANALYSIS"
  - "LEVEL_3_TEMPORARY_WRITE"
  - "LEVEL_4_PROJECT_STATE_WRITE"
  - "LEVEL_5_EXTERNAL_ACTION"

risk_levels:
  - "R0_READ_ONLY"
  - "R1_ANALYSIS"
  - "R2_INTERNAL_WRITE"
  - "R3_EXTERNAL_WRITE"
  - "R4_HIGH_IMPACT_EXTERNAL_ACTION"

core_principles:
  - "build_what_is_strategic"
  - "use_what_is_commodity"
  - "integrate_what_is_specialized"
  - "verify_everything"
  - "least_privilege"
  - "provider_independence"
  - "no_fabricated_tool_results"
  - "explicit_authorization"
  - "output_contract_validation"
  - "runtime_verification"
  - "persistent_capability_registry"
  - "security_first"
  - "reproducibility"

ai_installation:
  allowed_when_authorized: true
  permission_required: true
  trusted_source_required: true
  compatibility_check_required: true
  validation_required: true
  installation_record_required: true

security:
  least_privilege: true
  secret_protection: true
  supply_chain_review: true
  dependency_review: true
  data_boundary_review: true
  external_content_untrusted_by_default: true
  production_credential_protection: true

provider_architecture:
  abstraction_required: true
  provider_specific_logic_isolated: true
  normalized_application_contracts: true
  mock_provider_support: true
  migration_readiness: true

validation:
  smoke_test: true
  contract_test: true
  security_test: true
  integration_test: true
  failure_test: true
  regression_test: true
  runtime_verification: true

observability:
  execution_tracking: true
  latency_tracking: true
  failure_tracking: true
  cost_tracking: true
  provider_health_tracking: true
  quality_tracking: true
  capability_drift_detection: true

core_integrations:
  - "05_AI_AGENT_ARCHITECTURE.md"
  - "06_DATA_ARCHITECTURE.md"
  - "07_TECHNICAL_ARCHITECTURE.md"
  - "13_AGENT_SPECIFICATIONS.md"
  - "14_AGENT_WORKFLOW.md"
  - "15_HUMAN_IN_THE_LOOP.md"
  - "16_OUTPUT_CONTRACTS.md"
  - "21_DEVELOPMENT_AND_DEBUG.md"
  - "22_TESTING_AND_VALIDATION.md"
  - "23_PROJECT_CONTROL_CENTER.md"
  - "24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md"
  - "25_CONTEXT_MANAGEMENT.md"

governance:
  project_control_center: true
  capability_registry: true
  human_authority: true
  architecture_compliance: true
  change_management: true
  decision_records: true

mvp:
  capability_discovery: true
  capability_registry: true
  authorized_installation: true
  provider_abstraction: true
  mock_providers: true
  tool_contracts: true
  security_controls: true
  runtime_verification: true
  observability: true

strategic_boundary:
  seo_domain_methodology: "project_owned"
  seo_decision_engine: "project_owned"
  strategic_decisions: "human_authority"
  external_tools: "evidence_and_capability_sources"
  provider_truth: false

final_rule:
  statement: "External capabilities may accelerate execution, but no external skill, tool, plugin, provider, model, or library may silently override project architecture, domain knowledge, evidence standards, security boundaries, output contracts, or human strategic authority."
```

---

# 134. Final Status

```yaml
status:
  document: "26_SKILLS_AND_TOOLING_POLICY.md"
  state: "APPROVED_AS_BASELINE_SKILLS_AND_TOOLING_POLICY"
  capability_model: "discover_evaluate_authorize_integrate_validate_observe_govern"
  installation_policy: "authorized_ai_installation_allowed"
  security_model: "least_privilege_and_supply_chain_aware"
  provider_strategy: "abstracted_and_replaceable"
  tool_validation: "required"
  runtime_verification: "required_when_integration_claimed"
  capability_registry: "required"
  output_contract_bypass: false
  fabricated_tool_results: false
  unrestricted_ai_installation: false
  provider_lock_in_as_architecture: false
  strategic_authority: "human"
  project_domain_authority: "project_owned"
  documentation_set_complete: true
  next_action: "AUDIT_ALL_26_DOCUMENTS_AND_DERIVE_GLOBAL_DEPENDENCY_GRAPH"
```
