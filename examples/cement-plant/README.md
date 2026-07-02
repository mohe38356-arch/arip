# Example Cement Plant Dataset

This directory contains a small synthetic example dataset for ARIP — Autonomous Reliability Intelligence Platform.

The purpose of this dataset is to support documentation, development, testing, demonstrations, and early prototyping of ARIP asset hierarchy, condition monitoring, reliability intelligence, digital twin, and industrial AI workflows.

---

## Important Notice

This dataset is synthetic and generic.

It does not contain confidential plant data, real maintenance history, private company information, proprietary vendor documents, or sensitive industrial information.

The dataset is intended only for open-source development and demonstration purposes.

---

## Dataset Scope

The dataset represents a simplified cement plant asset hierarchy.

It may include:

* Plants
* Areas
* Systems
* Equipment
* Components
* Measurement points
* Monitoring methods
* Example thresholds
* Example inspection records

---

## Example Cement Plant Areas

The initial example dataset may include:

* Crusher Area
* Raw Mill Area
* Pyroprocessing Area
* Cement Mill Area
* Packing Area
* Utilities Area

---

## Example Equipment

The dataset may include equipment such as:

* Raw Mill Fan
* Kiln Main Drive
* Cooler Fan
* Cement Mill Gearbox
* Air Compressor
* Bucket Elevator
* Belt Conveyor
* Separator
* Pump
* Motor

---

## Example Measurement Points

Example measurement points may include:

* Motor DE Horizontal
* Motor DE Vertical
* Motor DE Axial
* Motor NDE Horizontal
* Motor NDE Vertical
* Fan DE Horizontal
* Fan DE Vertical
* Fan DE Axial
* Fan NDE Horizontal
* Gearbox Input Horizontal
* Gearbox Output Vertical
* Bearing Temperature Point
* Oil Sampling Point

---

## Example Monitoring Methods

The dataset may support examples for:

* Vibration
* Temperature
* Thermography
* Oil Analysis
* Ultrasound
* Visual Inspection
* Process Data

---

## Planned Files

The initial dataset may include:

```text
examples/cement-plant/
├── README.md
├── plants.csv
├── areas.csv
├── systems.csv
├── equipment.csv
├── components.csv
├── measurement-points.csv
├── monitoring-methods.csv
├── thresholds.csv
└── inspection-records.csv
```

---

## Data Privacy Rules

The dataset must not include:

* Real confidential plant data
* Real employee data
* Private company documents
* Real network information
* Sensitive maintenance records
* Proprietary vendor documents
* Security-sensitive OT / ICS information

All data should be synthetic, generic, anonymized, or created specifically for demonstration.

---

## Relationship with ARIP Documentation

This dataset supports the following ARIP documentation:

* Asset Hierarchy Model
* Condition Monitoring Domain Model
* Reliability Intelligence Domain Model
* Digital Twin Concept
* Industrial AI Concept
* Architecture Diagrams

---

## Intended Use

This dataset can be used for:

* Local development
* Backend seed data
* Frontend demos
* API testing
* Documentation examples
* Synthetic condition monitoring workflows
* Open-source demonstrations
