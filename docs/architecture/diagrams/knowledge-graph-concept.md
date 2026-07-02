# ARIP Knowledge Graph Concept Diagram

## Overview

This document provides the initial Knowledge Graph Concept Diagram for ARIP — Autonomous Reliability Intelligence Platform.

The ARIP Knowledge Graph connects industrial reliability entities such as assets, components, measurement points, symptoms, failure modes, root causes, maintenance actions, spare parts, and historical cases.

The goal is to support explainable diagnostics, reliability reasoning, root cause analysis, similar case search, and knowledge-based maintenance recommendations.

---

## Core Knowledge Graph Model

```mermaid
flowchart TB
    A["Asset"]
    C["Component"]
    MP["Measurement Point"]
    MR["Measurement Record"]
    S["Symptom"]
    FM["Failure Mode"]
    RC["Root Cause"]
    MA["Maintenance Action"]
    SP["Spare Part"]
    HC["Historical Case"]
    DOC["Technical Document"]
    REC["Recommendation"]

    A -->|"HAS_COMPONENT"| C
    C -->|"HAS_MEASUREMENT_POINT"| MP
    MP -->|"HAS_RECORD"| MR
    MR -->|"INDICATES"| S
    S -->|"SUGGESTS"| FM
    FM -->|"CAUSED_BY"| RC
    FM -->|"MITIGATED_BY"| MA
    MA -->|"REQUIRES"| SP
    HC -->|"INVOLVES"| A
    HC -->|"CONFIRMED"| RC
    HC -->|"RESOLVED_BY"| MA
    DOC -->|"DESCRIBES"| A
    DOC -->|"REFERENCES"| MA
    REC -->|"RECOMMENDS"| MA
    REC -->|"SUPPORTED_BY"| MR
    REC -->|"EXPLAINED_BY"| FM
```

---

## Diagnostic Reasoning Path

```mermaid
flowchart LR
    A["Measurement Record"]
    B["Detected Symptom"]
    C["Possible Failure Mode"]
    D["Possible Root Cause"]
    E["Recommended Action"]
    F["Required Spare Part"]
    G["Historical Case Evidence"]
    H["Human Review"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    G --> C
    G --> D
    E --> H
```

---

## Example: Fan Bearing Lubrication Problem

```mermaid
flowchart TB
    A["Asset: Raw Mill Fan"]
    C["Component: Fan DE Bearing"]
    MP["Measurement Point: Fan DE Horizontal"]
    MR["Measurement Record: High Frequency Vibration"]
    S["Symptom: Increased High-Frequency Vibration"]
    FM["Failure Mode: Bearing Lubrication Failure"]
    RC["Root Cause: Insufficient Lubrication"]
    MA["Maintenance Action: Inspect and Correct Lubrication"]
    SP["Spare Part / Material: Correct Lubricant"]
    HC["Historical Case: Similar Fan Bearing Case"]

    A -->|"HAS_COMPONENT"| C
    C -->|"HAS_MEASUREMENT_POINT"| MP
    MP -->|"HAS_RECORD"| MR
    MR -->|"INDICATES"| S
    S -->|"SUGGESTS"| FM
    FM -->|"CAUSED_BY"| RC
    FM -->|"MITIGATED_BY"| MA
    MA -->|"REQUIRES"| SP
    HC -->|"INVOLVES_SIMILAR_ASSET"| A
    HC -->|"CONFIRMED"| RC
    HC -->|"RESOLVED_BY"| MA
```

---

## Root Cause Analysis Support

```mermaid
flowchart TB
    EVENT["Failure or Abnormal Event"]
    SYM["Observed Symptoms"]
    DATA["Condition Monitoring Data"]
    HIST["Historical Cases"]
    PROC["Process Context"]
    MAINT["Maintenance History"]
    FM["Failure Mode Hypotheses"]
    RC["Root Cause Hypotheses"]
    EVID["Evidence"]
    ACTION["Corrective / Preventive Action"]
    LEARN["Lessons Learned"]

    EVENT --> SYM
    DATA --> SYM
    SYM --> FM
    HIST --> FM
    PROC --> RC
    MAINT --> RC
    FM --> RC
    RC --> EVID
    EVID --> ACTION
    ACTION --> LEARN
```

---

## Knowledge Graph and Explainable AI

The Knowledge Graph supports explainable AI by providing traceable reasoning paths.

Example:

```text
Input:
High vibration was recorded at Fan DE Horizontal measurement point.

Graph reasoning path:
Measurement Record -> indicates Symptom
Symptom -> suggests Failure Mode
Failure Mode -> caused by Root Cause
Root Cause -> mitigated by Maintenance Action

Output:
The system recommends lubrication inspection because the measured symptom is connected to bearing lubrication failure and similar historical cases.
```

---

## Core Node Types

The first version of the ARIP Knowledge Graph should include:

* Asset
* Component
* Measurement Point
* Measurement Record
* Symptom
* Failure Mode
* Root Cause
* Maintenance Action
* Spare Part
* Historical Case
* Technical Document
* Recommendation

---

## Core Relationship Types

Initial relationship types may include:

* HAS_COMPONENT
* HAS_MEASUREMENT_POINT
* HAS_RECORD
* INDICATES
* SUGGESTS
* CAUSED_BY
* MITIGATED_BY
* REQUIRES
* INVOLVES
* CONFIRMED
* RESOLVED_BY
* DESCRIBES
* REFERENCES
* SUPPORTED_BY
* EXPLAINED_BY

---

## Relationship with ARIP Domains

The Knowledge Graph connects to:

* Asset hierarchy
* Condition monitoring
* Reliability intelligence
* Root cause analysis
* Digital twin state
* Industrial AI
* Maintenance recommendation workflow
* Technical documentation search

---

## Related Documentation

* [Knowledge Graph Concept](../../knowledge-graph/knowledge-graph-concept.md)
* [Reliability Intelligence Workflow Diagram](reliability-intelligence-flow.md)
* [Condition Monitoring Workflow Diagram](condition-monitoring-flow.md)
* [Asset Hierarchy Diagram](asset-hierarchy.md)
* [Industrial AI Concept](../../ai/industrial-ai-concept.md)
* [Digital Twin Concept](../../digital-twin/digital-twin-concept.md)
