# ARIP Asset Hierarchy Diagram

## Overview

This document provides the initial Asset Hierarchy Diagram for ARIP — Autonomous Reliability Intelligence Platform.

The asset hierarchy is the foundation of ARIP. Every inspection record, measurement point, failure mode, condition monitoring value, reliability assessment, digital twin state, and AI recommendation should be connected to asset context.

---

## Practical Initial Asset Hierarchy

The first implementation of ARIP uses a practical industrial hierarchy:

```mermaid
flowchart TB
    P["Plant"]
    A["Area"]
    S["System"]
    E["Equipment"]
    C["Component"]
    MP["Measurement Point"]

    P --> A
    A --> S
    S --> E
    E --> C
    C --> MP
```

---

## Extended Enterprise Asset Hierarchy

The long-term ARIP hierarchy can be extended to support multi-site and multi-industry use cases.

```mermaid
flowchart TB
    ENT["Enterprise"]
    SITE["Site"]
    PLANT["Plant"]
    AREA["Area"]
    PU["Process Unit"]
    SYS["System"]
    EQ["Equipment"]
    SUB["Sub-Equipment"]
    COMP["Component"]
    FL["Failure Location"]
    MP["Measurement Point"]
    SEN["Sensor"]

    ENT --> SITE
    SITE --> PLANT
    PLANT --> AREA
    AREA --> PU
    PU --> SYS
    SYS --> EQ
    EQ --> SUB
    SUB --> COMP
    COMP --> FL
    FL --> MP
    MP --> SEN
```

---

## Cement Industry Example

Example hierarchy for a Raw Mill Fan System:

```mermaid
flowchart TB
    SITE["Site: Cement Plant"]
    PLANT["Plant: Main Production Plant"]
    AREA["Area: Raw Mill Area"]
    SYSTEM["System: Raw Mill Fan System"]
    EQUIP["Equipment: Raw Mill Fan"]

    MOTOR["Component: Motor"]
    FANROTOR["Component: Fan Rotor"]
    COUPLING["Component: Coupling"]
    BEARING["Component: Bearings"]

    MDEH["Measurement Point: Motor DE Horizontal"]
    MDEV["Measurement Point: Motor DE Vertical"]
    MDEA["Measurement Point: Motor DE Axial"]
    MNDEH["Measurement Point: Motor NDE Horizontal"]
    FNDEH["Measurement Point: Fan DE Horizontal"]
    FNDEV["Measurement Point: Fan DE Vertical"]
    FNDEA["Measurement Point: Fan DE Axial"]
    TEMP["Measurement Point: Bearing Temperature"]
    OIL["Measurement Point: Oil Sampling Point"]

    SITE --> PLANT
    PLANT --> AREA
    AREA --> SYSTEM
    SYSTEM --> EQUIP

    EQUIP --> MOTOR
    EQUIP --> FANROTOR
    EQUIP --> COUPLING
    EQUIP --> BEARING

    MOTOR --> MDEH
    MOTOR --> MDEV
    MOTOR --> MDEA
    MOTOR --> MNDEH

    FANROTOR --> FNDEH
    FANROTOR --> FNDEV
    FANROTOR --> FNDEA

    BEARING --> TEMP
    BEARING --> OIL
```

---

## Asset Context for Condition Monitoring

Condition monitoring records should always be connected to measurement points.

```mermaid
flowchart LR
    EQ["Equipment"]
    COMP["Component"]
    MP["Measurement Point"]
    MR["Measurement Record"]
    HA["Health Assessment"]
    FM["Possible Failure Mode"]
    REC["Maintenance Recommendation"]

    EQ --> COMP
    COMP --> MP
    MP --> MR
    MR --> HA
    HA --> FM
    FM --> REC
```

---

## Key Metadata

Each asset hierarchy entity may include:

* Unique identifier
* Business code
* Name
* Description
* Parent relationship
* Status
* Criticality
* Location
* Manufacturer
* Model
* Serial number
* Installation date
* Health score
* Risk score
* Last inspection date
* Last maintenance date

---

## Design Notes

ARIP should use both:

* A technical UUID for software-level uniqueness
* A business code for industrial users and plant teams

Example business codes:

```text
RM-FN-431
KILN-DRV-01
CM-GBX-102
COMP-AIR-01
```

---

## Related Documentation

* [Architecture Overview](../architecture-overview.md)
* [Asset Hierarchy Model](../asset-hierarchy-model.md)
* [Platform Architecture Diagram](platform-architecture.md)
* [C4 Context Diagram](c4-context.md)
* [C4 Container Diagram](c4-container.md)
* [Condition Monitoring Domain Model](../../condition-monitoring/condition-monitoring-domain-model.md)
