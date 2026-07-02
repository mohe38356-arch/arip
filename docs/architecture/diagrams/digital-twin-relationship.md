# ARIP Digital Twin Relationship Diagram

## Overview

This document provides the initial Digital Twin Relationship Diagram for ARIP — Autonomous Reliability Intelligence Platform.

The diagram shows how ARIP represents each industrial asset through multiple digital twin perspectives and how these twins are updated by condition monitoring, process data, reliability intelligence, industrial AI, and knowledge graph relationships.

---

## Digital Twin Relationship Model

```mermaid
flowchart TB
    A["Industrial Asset"]

    PT["Physical Twin"]
    FT["Functional Twin"]
    PRT["Process Twin"]
    RT["Reliability Twin"]
    ET["Energy Twin"]
    AIT["AI Twin"]

    CM["Condition Monitoring Data"]
    PD["Process Data"]
    MH["Maintenance History"]
    FH["Failure History"]
    KG["Knowledge Graph"]
    AI["Industrial AI"]
    RI["Reliability Intelligence"]

    A --> PT
    A --> FT
    A --> PRT
    A --> RT
    A --> ET
    A --> AIT

    CM --> PT
    CM --> RT
    CM --> AIT

    PD --> PRT
    PD --> FT
    PD --> ET

    MH --> RT
    FH --> RT

    KG --> RT
    KG --> AIT
    KG --> RI

    AI --> AIT
    AI --> RI

    RI --> RT
    RI --> AIT
```

---

## Six Digital Twin Perspectives

```mermaid
flowchart LR
    Asset["Asset Digital Twin"]

    Physical["Physical Twin<br/>Structure, Components, Location"]
    Functional["Functional Twin<br/>Function, Performance, Availability"]
    Process["Process Twin<br/>Operating Context, Process Variables"]
    Reliability["Reliability Twin<br/>Health, Risk, Failure Modes, RUL"]
    Energy["Energy Twin<br/>Power, Efficiency, Energy Deviation"]
    AI["AI Twin<br/>Predictions, Confidence, Explanations"]

    Asset --> Physical
    Asset --> Functional
    Asset --> Process
    Asset --> Reliability
    Asset --> Energy
    Asset --> AI
```

---

## Twin State Update Flow

```mermaid
flowchart TB
    A["New Data Event"]

    B["Validate Data"]
    C["Identify Asset Context"]
    D["Identify Affected Twin"]
    E["Update Twin State"]
    F["Recalculate Health or Risk"]
    G["Generate Insight"]
    H["Human Review if Needed"]
    I["Store Twin Update History"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
```

---

## Example: Raw Mill Fan Digital Twin

```mermaid
flowchart TB
    RMF["Asset: Raw Mill Fan"]

    P1["Physical Twin<br/>Motor, Fan Rotor, Bearings, Coupling"]
    F1["Functional Twin<br/>Airflow, Speed, Availability"]
    PR1["Process Twin<br/>Mill Pressure, Temperature, Production Rate"]
    R1["Reliability Twin<br/>Bearing Health, Vibration Trend, Risk Score"]
    E1["Energy Twin<br/>Motor Power, Energy Efficiency"]
    AI1["AI Twin<br/>Anomaly Score, Fault Classification, Explanation"]

    VIB["Vibration Record"]
    TEMP["Temperature Record"]
    PROC["Process Variables"]
    POWER["Motor Power Data"]
    KNOW["Failure Mode Knowledge"]
    PRED["AI Prediction"]

    RMF --> P1
    RMF --> F1
    RMF --> PR1
    RMF --> R1
    RMF --> E1
    RMF --> AI1

    VIB --> R1
    TEMP --> P1
    TEMP --> R1
    PROC --> PR1
    PROC --> F1
    POWER --> E1
    KNOW --> R1
    PRED --> AI1
```

---

## Digital Twin and Reliability Intelligence

```mermaid
flowchart LR
    CM["Condition Monitoring"]
    HS["Health Score"]
    RS["Risk Score"]
    FM["Failure Mode"]
    RUL["RUL Estimate"]
    REC["Maintenance Recommendation"]
    RT["Reliability Twin"]

    CM --> HS
    HS --> RS
    RS --> FM
    FM --> RUL
    RUL --> REC
    HS --> RT
    RS --> RT
    FM --> RT
    RUL --> RT
```

---

## Digital Twin and AI Twin

The AI Twin stores AI-related interpretation for an asset.

It may include:

* Anomaly score
* Fault classification
* RUL prediction
* Confidence level
* Model version
* Explanation record
* Human review status
* Feedback result
* Model drift indicator

```mermaid
flowchart TB
    DATA["Input Data"]
    MODEL["AI Model or Rule"]
    OUTPUT["AI Output"]
    EXPLAIN["Explanation"]
    REVIEW["Human Review"]
    STATE["AI Twin State"]

    DATA --> MODEL
    MODEL --> OUTPUT
    OUTPUT --> EXPLAIN
    EXPLAIN --> REVIEW
    REVIEW --> STATE
```

---

## Design Notes

ARIP treats digital twins as structured engineering state models, not only as 3D visualizations.

The first implementation should focus on:

* Asset state
* Component state
* Health state
* Risk state
* Process context
* Energy context
* AI interpretation
* Twin update history

Advanced simulation, 3D visualization, and physics-based modeling can be added after the core state model is stable.

---

## Relationship with ARIP Domains

The Digital Twin layer connects to:

* Asset hierarchy
* Condition monitoring
* Reliability intelligence
* Knowledge graph
* Industrial AI
* Offline-first inspection workflow
* Maintenance recommendation workflow
* Reporting and dashboards

---

## Related Documentation

* [Digital Twin Concept](../../digital-twin/digital-twin-concept.md)
* [Platform Architecture Diagram](platform-architecture.md)
* [C4 Container Diagram](c4-container.md)
* [Asset Hierarchy Diagram](asset-hierarchy.md)
* [Condition Monitoring Workflow Diagram](condition-monitoring-flow.md)
* [Reliability Intelligence Workflow Diagram](reliability-intelligence-flow.md)
* [Knowledge Graph Concept Diagram](knowledge-graph-concept.md)
* [Industrial AI Concept](../../ai/industrial-ai-concept.md)
