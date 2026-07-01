# ARIP Asset Hierarchy Model

## Overview

The asset hierarchy is the foundation of ARIP.

ARIP is designed as an asset-centric industrial platform. Every inspection, condition monitoring record, failure mode, maintenance action, digital twin, AI prediction, and reliability decision must be connected to an asset structure.

The asset hierarchy provides the structural model that connects the physical industrial world to software, data, analytics, and decision-making.

---

## Core Design Principle

ARIP follows an asset-centric design principle:

> No data without asset context.
> No diagnosis without asset context.
> No maintenance recommendation without asset context.

This means that all data must be connected to:

* Site
* Plant
* Area
* System
* Equipment
* Component
* Measurement Point

---

## Initial Asset Hierarchy

The initial implementation uses the following practical hierarchy:

```text
Site
└── Plant
    └── Area
        └── System
            └── Equipment
                └── Component
                    └── Measurement Point
```

This hierarchy is simple enough for the first implementation phase and strong enough to support real industrial equipment structures.

---

## Extended Enterprise Asset Hierarchy

The long-term enterprise model can be extended as follows:

```text
Enterprise
└── Site
    └── Plant
        └── Area
            └── Process Unit
                └── System
                    └── Equipment
                        └── Sub-Equipment
                            └── Component
                                └── Failure Location
                                    └── Measurement Point
                                        └── Sensor
```

---

## Entity Definitions

### Enterprise

Represents a company, group, or industrial organization.

Examples:

* Cement group
* Mining company
* Steel company
* Petrochemical company

---

### Site

Represents a physical industrial site.

Examples:

* Shahrekord Cement Site
* Steel Production Site
* Mine Processing Site

---

### Plant

Represents a production plant or major facility inside a site.

Examples:

* Cement Plant
* Clinker Production Plant
* Raw Material Preparation Plant

---

### Area

Represents a major plant area or department.

Examples in cement industry:

* Crusher Area
* Raw Mill Area
* Pyroprocessing Area
* Cement Mill Area
* Packing Area
* Utilities Area

---

### Process Unit

Represents a process-based functional unit.

Examples:

* Raw Grinding Unit
* Kiln Line
* Cooler Unit
* Cement Grinding Unit
* Air Compression Unit

---

### System

Represents a group of equipment working together to perform a function.

Examples:

* Raw Mill Fan System
* Kiln Drive System
* Cooler Fan System
* Compressor System
* Conveyor System
* Separator System

---

### Equipment

Represents a maintainable industrial asset.

Examples:

* Fan
* Motor
* Gearbox
* Pump
* Compressor
* Conveyor
* Elevator
* Separator
* Mill
* Kiln Drive

---

### Sub-Equipment

Represents a major sub-assembly of equipment.

Examples:

* Motor
* Gearbox
* Fan Rotor
* Coupling
* Hydraulic Unit
* Lubrication Unit

---

### Component

Represents a physical component that can fail, be inspected, or be replaced.

Examples:

* Bearing
* Shaft
* Coupling
* Impeller
* Gear
* Pulley
* Belt
* Seal
* Roller
* Housing

---

### Failure Location

Represents the exact location where a failure may occur.

Examples:

* Motor Drive End
* Motor Non-Drive End
* Gearbox Input Shaft
* Gearbox Output Shaft
* Fan Drive End Bearing
* Fan Non-Drive End Bearing

---

### Measurement Point

Represents a defined inspection or measurement location.

Examples:

* Motor DE Horizontal
* Motor DE Vertical
* Motor DE Axial
* Motor NDE Horizontal
* Fan DE Horizontal
* Gearbox Input Vertical
* Bearing Temperature Point
* Oil Sampling Point

---

### Sensor

Represents a physical or virtual sensor.

Examples:

* Vibration sensor
* Temperature sensor
* Pressure sensor
* Flow sensor
* Current sensor
* Manual inspection point
* Portable measurement point

---

## Cement Industry Example

Example hierarchy for a raw mill fan system:

```text
Site: Shahrekord Cement
└── Plant: Cement Plant
    └── Area: Raw Mill Area
        └── System: Raw Mill Fan System
            └── Equipment: Raw Mill Fan
                ├── Component: Motor
                │   ├── Measurement Point: Motor DE Horizontal
                │   ├── Measurement Point: Motor DE Vertical
                │   ├── Measurement Point: Motor DE Axial
                │   ├── Measurement Point: Motor NDE Horizontal
                │   └── Measurement Point: Motor NDE Vertical
                ├── Component: Fan Rotor
                │   ├── Measurement Point: Fan DE Horizontal
                │   ├── Measurement Point: Fan DE Vertical
                │   └── Measurement Point: Fan NDE Horizontal
                ├── Component: Coupling
                └── Component: Bearings
```

---

## Required Metadata

Each asset hierarchy entity should support the following metadata where applicable:

* Unique identifier
* Business code
* Name
* Description
* Parent entity
* Status
* Criticality
* Location
* Manufacturer
* Model
* Serial number
* Installation date
* Commissioning date
* Technical specifications
* Maintenance responsibility
* Inspection responsibility
* Documentation links
* Photos or drawings
* Health score
* Risk score
* Last inspection date
* Last maintenance date

---

## Business Code and UUID

ARIP should use two types of identifiers:

### UUID

A globally unique technical identifier used internally by the software.

### Business Code

A human-readable industrial code used by engineers and plant personnel.

Examples:

* RM-FN-431
* KILN-DRV-01
* CM-MTR-102
* COMP-AIR-01

Both identifiers are important.

The UUID ensures software-level uniqueness.

The business code ensures usability for industrial teams.

---

## Measurement Point Model

Measurement points are critical for condition monitoring.

A measurement point should include:

* Asset reference
* Component reference
* Point name
* Direction
* Monitoring method
* Unit
* Alarm threshold
* Danger threshold
* Measurement interval
* Location description
* Sensor type
* Portable or online measurement type

Example directions:

* Horizontal
* Vertical
* Axial
* Radial
* Temperature
* Oil sample
* Visual

Example monitoring methods:

* Vibration
* Temperature
* Thermography
* Oil analysis
* Ultrasound
* Visual inspection
* Process data

---

## Relationship to Reliability Intelligence

The asset hierarchy connects directly to reliability intelligence.

Example:

```text
Equipment
└── Component
    └── Failure Mode
        └── Symptom
            └── Measurement Point
                └── Condition Monitoring Record
```

This allows ARIP to answer questions such as:

* Which equipment has the highest risk?
* Which components fail most often?
* Which measurement points show abnormal trends?
* Which failure modes are most probable?
* Which maintenance actions were effective?
* Which assets need priority inspection?

---

## Relationship to Digital Twin

Each asset may have one or more digital twin perspectives:

* Physical Twin
* Functional Twin
* Process Twin
* Reliability Twin
* Energy Twin
* AI Twin

The asset hierarchy provides the structural context for these twins.

---

## Relationship to Knowledge Graph

The asset hierarchy is also a foundation for the ARIP industrial knowledge graph.

Example graph relationships:

```text
Asset -> has_component -> Component
Component -> has_failure_mode -> Failure Mode
Failure Mode -> has_symptom -> Symptom
Symptom -> measured_at -> Measurement Point
Failure Mode -> mitigated_by -> Maintenance Action
Asset -> located_in -> Area
System -> contains -> Equipment
Equipment -> connected_to -> Equipment
```

---

## Initial Implementation Recommendation

For the first implementation phase, ARIP should start with this structure:

```text
Plant
└── Area
    └── System
        └── Equipment
            └── Component
                └── Measurement Point
```

This keeps the implementation practical while allowing later extension to the full enterprise model.

---

## Future Extensions

Future extensions may include:

* Enterprise-level multi-site hierarchy
* ISO 14224 equipment class taxonomy
* ISA-95 integration
* KKS-like coding system
* Process flow relationships
* Equipment dependency graph
* Reliability block diagrams
* Functional location hierarchy
* Spare parts hierarchy
* Maintenance strategy hierarchy
