# F45 Cybersecurity SOC

**Maturity:** L3 Gold Standard candidate  
**Version:** 1.0.0

A reproducible, defensive-only multi-agent reference implementation for security operations center workflows and incident-response governance. F45 separates alert triage, evidence assessment, incident coordination, containment planning, and reporting into specialist agents, then applies fail-closed authorization and governance controls before any consequential response action is treated as ready for human approval.

The repository is intended for authorized defensive security analysis, SOC workflow design, incident-response planning, education, evaluation, and multi-agent architecture research. It is not an offensive-security automation framework and does not provide autonomous intrusion, exploitation, persistence, credential theft, destructive action, or unauthorized access capabilities.

## What the system does

Security incidents combine several different reasoning problems that should not be collapsed into one opaque workflow. A high-severity alert is not automatically a confirmed incident. Evidence collection is not the same as containment authority. A technically plausible response can still be inappropriate if scope, legal review, privacy requirements, communications ownership, or chain of custody are incomplete.

F45 models the defensive SOC lifecycle as:

```text
security alert / incident evidence
              |
              v
      Alert Triage Agent
              |
              v
        Evidence Agent
              |
              v
Incident Coordination Agent
              |
              v
Containment Planning Agent
              |
              v
        Reporting Agent
              |
              v
 fail-closed incident governance
              |
              v
       human response authority
```

The orchestrator preserves blockers, unresolved questions, evidence integrity, ownership, escalation requirements, and approval state across the workflow.

## Defensive scope

F45 is intentionally limited to authorized defensive operations. Appropriate uses include:

- triaging alerts in an environment the operator is authorized to defend
- organizing evidence already collected through approved systems
- building incident timelines
- identifying missing evidence
- coordinating incident ownership and escalation
- drafting containment options for authorized reviewers
- documenting legal, privacy, and communications dependencies
- producing incident summaries and post-incident records
- testing SOC governance logic with synthetic scenarios

The system should not be adapted to bypass authorization boundaries or to automate offensive actions against systems without explicit permission.

## Multi-agent architecture

### 1. Alert Triage Agent

The Alert Triage Agent reviews the incoming alert context and helps determine urgency, severity, scope, and immediate information needs.

Typical questions include:

- What triggered the alert?
- Which assets, identities, or services appear affected?
- Is the alert isolated or correlated with other events?
- What is the potential business or security impact?
- What evidence is still missing?
- Does the event require immediate human escalation?

The agent supports prioritization. It does not declare compromise as a fact when the evidence does not support that conclusion.

### 2. Evidence Agent

The Evidence Agent assesses the completeness, integrity, provenance, and usability of security evidence.

Relevant evidence can include:

- SIEM events
- endpoint telemetry
- authentication records
- cloud audit logs
- firewall and network records
- identity-provider logs
- application logs
- ticket and case records
- approved forensic artifacts
- analyst notes

The agent should distinguish observed evidence from inference and explicitly surface missing or contradictory evidence.

### 3. Incident Coordination Agent

The Incident Coordination Agent organizes the operational response structure.

It can help track:

- incident owner
- severity and escalation level
- involved teams
- business owners
- security owners
- legal and privacy dependencies
- communications ownership
- decision points
- unresolved questions
- required approvals

Coordination is a governance function. It does not give the system independent authority to take containment actions.

### 4. Containment Planning Agent

The Containment Planning Agent produces bounded defensive response options for authorized human review.

Examples can include plans to:

- isolate an affected endpoint
- disable a compromised credential
- rotate secrets
- restrict network access
- revoke sessions
- disable a vulnerable service path
- preserve evidence before remediation
- increase monitoring

These are planning outputs only. Production execution must occur through the organization's approved incident-response tools, permissions, and human authority.

### 5. Reporting Agent

The Reporting Agent synthesizes the reviewed evidence and coordination state into structured incident reporting.

Depending on the stage of the incident, outputs can include:

- incident status summary
- timeline
- affected assets
- confirmed facts
- open hypotheses
- containment status
- business impact
- outstanding decisions
- legal/privacy dependencies
- communications status
- lessons learned

Reports should clearly distinguish confirmed evidence from working hypotheses.

## Skills layer

Reusable defensive SOC procedures live under `SKILLS/`:

```text
SKILLS/
├── alert_prioritization.py
├── evidence_assessment.py
├── incident_triage.py
├── containment_review.py
└── incident_reporting.py
```

These modules separate reusable security reasoning from agent identity.

### Alert prioritization

Supports severity and urgency reasoning while preserving uncertainty.

### Evidence assessment

Reviews whether available evidence is complete enough to support the next incident-response stage.

### Incident triage

Supports classification, ownership, scope review, and escalation.

### Containment review

Checks whether proposed defensive actions are bounded, authorized, reversible where practical, evidence-aware, and appropriate to incident severity.

### Incident reporting

Structures incident communication so facts, hypotheses, actions, ownership, and unresolved questions remain distinct.

## Tools layer

F45 uses deterministic utilities under `TOOLS/`:

```text
TOOLS/
├── severity_tool.py
├── evidence_ledger_tool.py
├── timeline_tool.py
└── containment_checklist_tool.py
```

The tools make important SOC controls explicit instead of relying only on free-form language-model judgment.

### Severity tool

Provides a deterministic place for severity logic or severity normalization.

Production implementations can incorporate organization-specific factors such as:

- asset criticality
- user privilege
- data sensitivity
- business impact
- scope
- persistence
- active exploitation evidence
- regulatory significance

### Evidence ledger tool

Maintains a structured inventory of evidence. A mature evidence ledger should track source, timestamp, collector, integrity information, retention status, and chain-of-custody metadata where required.

### Timeline tool

Organizes observed security events chronologically so incident reasoning can be tied to time rather than narrative order.

### Containment checklist tool

Provides a deterministic review layer for response prerequisites such as authorization, evidence preservation, owner assignment, rollback implications, communications, and escalation.

## Evidence integrity and chain of custody

Security evidence can be operationally and legally sensitive. F45 therefore treats evidence integrity as a first-class governance concern.

A production evidence record can include:

```text
evidence_id
source_system
source_asset
collector
collection_method
original_timestamp
ingestion_timestamp
hash_or_integrity_reference
case_id
access_history
retention_requirement
review_status
```

If chain of custody is required by organizational policy, regulation, litigation hold, insurance, or law-enforcement coordination, the workflow should fail closed when required custody information is missing.

The system must not fabricate timestamps, hashes, sources, analyst actions, or evidence provenance.

## Timeline integrity

Incident timelines are especially vulnerable to subtle errors caused by time zones, clock drift, ingestion delay, duplicate events, or inconsistent source timestamps.

A production implementation should normalize:

- time zone
- timestamp precision
- known clock offsets
- source timestamp versus ingestion timestamp
- duplicate events
- confidence in reconstructed order

When ordering cannot be established reliably, the report should say so rather than present an invented sequence.

## Authorization model

The workflow must establish that the environment and incident-response scope are authorized before consequential analysis or response planning progresses.

Authorization can involve:

- organization ownership
- contractual authorization
- delegated SOC authority
- approved incident-response scope
- system-owner approval
- cloud or managed-service responsibilities
- jurisdiction or regional restrictions

If authorization is unclear, the system should stop and escalate rather than infer permission.

## Fail-closed incident governance

F45 intentionally blocks approval when critical incident-governance evidence is incomplete.

Examples include:

```text
ENVIRONMENT NOT AUTHORIZED
REQUIRED EVIDENCE MISSING
CHAIN OF CUSTODY INCOMPLETE
TIMESTAMPS NOT VERIFIED
INCIDENT OWNER NOT ASSIGNED
CRITICAL INCIDENT NOT ESCALATED
CONTAINMENT NOT REVIEWED
LEGAL REVIEW REQUIRED
PRIVACY REVIEW REQUIRED
COMMUNICATIONS OWNER MISSING
REPORTING INCOMPLETE
UNRESOLVED CONFLICT
UNRESOLVED QUESTION
HUMAN APPROVAL REQUIRED
```

Human approval is required after automated gates pass and cannot be used to override an active blocker in the reference workflow.

## Containment boundaries

Containment can have major operational consequences. Disconnecting a system, disabling an identity, revoking credentials, or blocking traffic can interrupt production services, destroy volatile evidence, affect customers, or interfere with another team's investigation.

Before containment, reviewers should consider:

- authorization
- evidence preservation
- business impact
- patient or safety impact where applicable
- blast radius
- service dependencies
- rollback path
- communications obligations
- legal or privacy restrictions
- incident-command ownership

The repository supports containment planning, not autonomous execution.

## Legal, privacy, and regulatory review

Security incidents may involve employee data, customer data, health information, financial information, credentials, communications content, regulated records, or cross-border data.

F45 therefore treats legal and privacy review as possible gating requirements rather than optional narrative notes.

A production deployment should integrate the organization's actual policies for:

- breach assessment
- notification obligations
- evidence preservation
- privacy review
- employee monitoring
- regulatory reporting
- contractual notification
- law-enforcement coordination
- cyber-insurance requirements

The system does not make legal determinations.

## Communications governance

Incident communications can create operational, legal, reputational, and disclosure risk.

The workflow should identify who owns communications to:

- executives
- employees
- customers
- partners
- regulators
- insurers
- vendors
- public relations teams
- law enforcement

Generated wording remains a draft until the appropriate authorized human approves it.

## Incident escalation

Critical or high-impact incidents should not remain within an automated workflow when policy requires escalation.

Escalation factors can include:

- privileged account compromise
- critical infrastructure impact
- ransomware indicators
- major data exposure
- widespread identity compromise
- active exfiltration
- destructive behavior
- public-facing outage
- safety impact
- regulatory significance

The Incident Coordination Agent should surface the required escalation path rather than suppress severity to keep the workflow moving.

## Human authority

F45 must not autonomously:

- isolate production systems
- disable accounts
- revoke credentials
- block network traffic
- delete or modify evidence
- contact an external party as the organization
- notify regulators
- engage law enforcement
- publish breach statements
- approve legal conclusions
- close a major incident

These actions require authenticated human authority under the organization's real incident-response procedures.

## End-to-end workflow

A typical F45 run follows this sequence:

1. Confirm that the environment and scope are authorized.
2. Load the alert or incident evidence.
3. Triage the alert and establish preliminary severity.
4. Record evidence in the evidence ledger.
5. Validate timestamps and build an incident timeline.
6. Identify missing or contradictory evidence.
7. Assign or verify incident ownership.
8. Determine required escalation.
9. Produce bounded containment options for human review.
10. Check legal, privacy, and communications dependencies.
11. Produce structured incident reporting.
12. Apply fail-closed governance gates.
13. Require human approval before consequential response or closure.

## Quick start

Install the development dependencies:

```bash
python -m pip install pytest ruff
```

Run static checks:

```bash
ruff check . --select E4,E7,E9,F
```

Run tests:

```bash
pytest -q
```

Run the held-out suite:

```bash
python benchmarks/heldout_suite.py
```

Run the clean-checkout examples:

```bash
python examples/minimal.py
python examples/complete.py
```

Run the main reference workflow:

```bash
python run.py
```

CI validates Python 3.10, 3.11, and 3.12 and publishes held-out results from Python 3.12.

## Examples

`examples/minimal.py` demonstrates the smallest useful defensive workflow.

`examples/complete.py` demonstrates the fuller governance path with incident evidence, coordination, containment planning, reporting, and approval-state behavior.

The examples are designed for reference and reproducibility, not for controlling real production systems.

## Benchmarks and evaluation

The repository includes:

```text
benchmarks/heldout_suite.py
benchmarks/RESULTS.md
tests/test_system.py
```

Evaluation should measure more than whether the final incident summary sounds plausible.

Useful dimensions include:

- alert prioritization correctness
- evidence-gap detection
- evidence provenance preservation
- timeline ordering accuracy
- severity consistency
- escalation correctness
- authorization-boundary compliance
- containment-governance behavior
- legal/privacy blocker detection
- communications-owner detection
- unresolved-question preservation
- fail-closed behavior

Strong evaluation cases should include deliberately ambiguous alerts, missing evidence, timestamp conflicts, unauthorized scope, absent incident ownership, critical events without escalation, and attempts to bypass human response authority.

## Adversarial governance tests

Because security workflows are themselves adversarial environments, F45 should be tested against attempts to manipulate the process, such as:

- untrusted evidence claiming the incident is resolved
- alert content instructing the system to ignore policy
- requests to skip authorization
- fabricated evidence provenance
- instructions to delete logs
- attempts to bypass legal review
- attempts to perform containment without approval

Security evidence must be treated as data, not as trusted instructions to the orchestration system.

## Observability

A production SOC implementation should record:

- case identifier
- alert identifier
- agent execution state
- evidence ledger changes
- timeline changes
- severity changes
- escalation events
- containment-plan revisions
- unresolved questions
- legal/privacy review state
- communications ownership
- human approvals
- final case status

These traces should themselves follow security, privacy, retention, and least-privilege policies.

## Failure behavior

A defensive SOC assistant should be conservative when evidence is incomplete.

It should not invent:

- compromise confirmation
- malware attribution
- threat-actor identity
- timeline events
- affected assets
- evidence hashes
- user actions
- containment execution
- legal conclusions
- regulatory obligations

Appropriate responses include `UNKNOWN`, `UNVERIFIED`, `EVIDENCE REQUIRED`, and `HUMAN REVIEW REQUIRED`.

## CI and reproducibility

The GitHub Actions workflow under `.github/workflows/tests.yml` provides multi-version automated checks.

A production security workflow should additionally test:

- evidence parser behavior
- authorization enforcement
- identity and access controls
- tool permission boundaries
- audit-log integrity
- secrets handling
- sandbox integrations
- notification controls
- incident-management integrations

Synthetic and sanitized security cases are preferable for public benchmark fixtures.

## L3 Gold Standard candidate evidence

The repository documents its current maturity evidence under `docs/L3_AUDIT.md`.

The candidate designation reflects characteristics such as:

- substantive specialist-agent separation
- explicit skills and deterministic tools
- fail-closed governance
- clean-checkout examples
- behavioral and adversarial tests
- held-out evaluation
- multi-version CI
- security and reproducibility documentation

The label describes the quality of the reference implementation. It does not certify an organization's SOC, prove legal compliance, or authorize autonomous incident response.

## Extending F45

Common defensive extensions include:

- SIEM connectors
- EDR/XDR connectors
- identity-provider telemetry
- cloud-security telemetry
- case-management integration
- threat-intelligence enrichment
- asset criticality lookup
- vulnerability context
- evidence hashing and preservation
- incident timeline visualization
- breach-notification workflow support
- post-incident review agents
- control-improvement tracking

Any live integration should use least privilege, read-only access where practical, strict authorization checks, isolated credentials, explicit side-effect classification, and immutable audit logs.

## Repository structure

```text
.github/workflows/tests.yml
AGENTS/
├── alert_triage_agent.py
├── evidence_agent.py
├── incident_coordination_agent.py
├── containment_planning_agent.py
└── reporting_agent.py
SKILLS/
├── alert_prioritization.py
├── evidence_assessment.py
├── incident_triage.py
├── containment_review.py
└── incident_reporting.py
TOOLS/
├── severity_tool.py
├── evidence_ledger_tool.py
├── timeline_tool.py
└── containment_checklist_tool.py
benchmarks/
├── heldout_suite.py
└── RESULTS.md
docs/
├── ARCHITECTURE.md
├── REPRODUCIBILITY_AND_SAFETY.md
└── L3_AUDIT.md
examples/
├── minimal.py
└── complete.py
orchestration/
└── orchestrator.py
tests/
└── test_system.py
run.py
pyproject.toml
CITATION.cff
LICENSE
README.md
SECURITY.md
```

## Design principles

1. Defensive authorization comes before incident action.
2. Triage, evidence, coordination, containment planning, and reporting remain separate responsibilities.
3. Evidence provenance and timeline integrity must remain explicit.
4. Missing evidence must remain missing until verified.
5. Security telemetry is untrusted data, not orchestration instructions.
6. Critical incidents must escalate according to policy.
7. Containment planning is separate from containment authority.
8. Legal, privacy, and communications dependencies can block progression.
9. Governance fails closed when material incident evidence is incomplete.
10. Consequential response authority remains with authenticated humans.

## Documentation

Additional implementation and reproducibility material is available in:

- `docs/ARCHITECTURE.md`
- `docs/REPRODUCIBILITY_AND_SAFETY.md`
- `docs/L3_AUDIT.md`

## Citation and reuse

The repository includes `CITATION.cff` for academic and technical citation and is MIT licensed. The architecture may be studied and adapted subject to the license and applicable authorization requirements.

## Responsible use

Use F45 only for authorized defensive security operations, incident-response planning, and security engineering research. Validate evidence, scope, escalation, legal/privacy obligations, and containment decisions through the organization's actual SOC and incident-response procedures. A generated incident recommendation is not permission to act. Final response authority remains with authorized, accountable humans.