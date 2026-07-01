# ARIP Condition Monitoring Domain Model

## Overview

Condition Monitoring is one of the core domains of ARIP.

The goal of this domain is to collect, structure, analyze, and interpret equipment condition data in order to detect early signs of failure, support reliability decisions, and improve maintenance planning.

ARIP is designed to support multimodal condition monitoring, meaning that different inspection and monitoring methods can be connected to the same asset, component, failure mode, and maintenance decision.

---

## Domain Purpose

The Condition Monitoring domain helps answer questions such as:

* What is the current condition of an equipment item?
* Which measurement points are abnormal?
* Which components show early signs of degradation?
* Which failure modes are most likely?
* Which assets require urgent inspection?
* How is equipment condition changing over time?
* Which maintenance action should be recommended?

---

## Core Design Principle

Condition monitoring data must always be connected to asset context.

In ARIP, a condition monitoring record should not exist as isolated data.

Each record should be connected to:

* Plant
* Area
* System
* Equipment
* Component
* Measurement Point
* Monitoring Method
* Inspection Event
* Measurement Value
* Threshold or Baseline
* Health Assessment

---

## Supported Monitoring Methods

ARIP is designed to support multiple monitoring methods.

Initial methods include:

* Vibration monitoring
* Temperature monitoring
* Thermography
* Oil analysis
* Ultrasound
* Visual inspection
* Process data analysis

Future methods may include:

* Acoustic emission
* Motor current signature analysis
* Electrical signature analysis
* Power quality analysis
* Drone inspection
* Robotic inspection
* Computer vision-based inspection

---

## Core Entities

### Monitoring Method

Represents the type of condition monitoring technique.

Examples:

* Vibration
* Temperature
* Thermography
* Oil Analysis
* Ultrasound
* Visual Inspection
* Process Data

---

### Measurement Point

Represents the physical or logical location where data is collected.

Examples:

* Motor DE Horizontal
* Motor DE Vertical
* Motor NDE Horizontal
* Fan DE Axial
* Gearbox Input Vertical
* Bearing Temperature Point
* Oil Sampling Point

A measurement point should include:

* Equipment reference
* Component reference
* Point name
* Direction
* Method
* Unit
* Alarm threshold
* Danger threshold
* Baseline value
* Measurement interval
* Portable or online measurement type

---

### Inspection Event

Represents a specific inspection activity.

Examples:

* Monthly vibration inspection
* Weekly temperature inspection
* Oil sample collection
* Thermography route
* Visual inspection round

An inspection event may include:

* Inspector
* Date and time
* Asset
* Measurement points
* Instrument used
* Environmental condition
* Operating condition
* Notes
* Attachments

---

### Measurement Record

Represents a measured condition value.

Examples:

* Vibration velocity
* Vibration acceleration
* Bearing temperature
* Oil viscosity
* Particle count
* Thermography hotspot temperature
* Ultrasound dB value

A measurement record may include:

* Measurement point
* Timestamp
* Method
* Value
* Unit
* Direction
* Instrument
* Operating condition
* Alarm status
* Data quality status
* Notes

---

### Trend

Represents the historical behavior of a measurement over time.

Trend analysis can help detect:

* Gradual degradation
* Sudden change
* Repeated abnormal behavior
* Seasonal or operating-related variation
* Early warning indicators

---

### Threshold

Represents alarm and danger limits.

Thresholds may be defined by:

* ISO standards
* OEM manuals
* Historical baseline
* Engineering judgment
* Statistical analysis
* Equipment criticality

Common threshold levels:

* Normal
* Alert
* Alarm
* Danger
* Critical

---

### Baseline

Represents the expected normal behavior of a measurement point.

A baseline may be created from:

* Commissioning data
* Historical healthy operation
* OEM reference values
* Statistical normal behavior
* Similar equipment comparison

---

### Health Assessment

Represents the interpretation of condition monitoring data.

Possible outputs:

* Normal
* Watch
* Warning
* Critical
* Unknown

A health assessment may include:

* Health score
* Severity level
* Confidence level
* Detected symptom
* Possible failure mode
* Recommended action

---

## Vibration Monitoring Model

Vibration monitoring is one of the first target domains in ARIP.

Supported measurement types may include:

* Velocity
* Acceleration
* Displacement
* Bearing condition unit
* Spectrum
* Time waveform
* Envelope spectrum
* Phase
* 1X / 2X / 3X components

Common vibration directions:

* Horizontal
* Vertical
* Axial

Common fault patterns:

* Unbalance
* Misalignment
* Mechanical looseness
* Bearing defect
* Gear mesh problem
* Resonance
* Belt defect
* Soft foot
* Structural weakness

---

## Temperature Monitoring Model

Temperature monitoring can be used for:

* Bearing condition
* Motor condition
* Gearbox condition
* Lubrication condition
* Electrical connection condition
* Process abnormality

Temperature records may include:

* Absolute temperature
* Delta temperature
* Ambient temperature
* Operating load
* Measurement distance
* Emissivity setting for infrared measurements

---

## Thermography Model

Thermography records may include:

* Thermal image
* Visual image
* Hotspot temperature
* Reference temperature
* Delta temperature
* Emissivity
* Reflected temperature
* Distance
* Equipment load condition
* Interpretation notes

Thermography can help detect:

* Electrical hotspots
* Bearing overheating
* Coupling problems
* Insulation problems
* Refractory defects
* Process leakage
* Mechanical friction

---

## Oil Analysis Model

Oil analysis records may include:

* Oil sample point
* Oil type
* Sampling date
* Operating hours
* Viscosity
* Water content
* TAN
* TBN
* Particle count
* ISO cleanliness code
* Wear metals
* Additives
* Contaminants
* Laboratory interpretation

Oil analysis can help detect:

* Lubricant degradation
* Wear particles
* Contamination
* Water ingress
* Oxidation
* Incorrect lubricant
* Filtration problems

---

## Ultrasound Model

Ultrasound records may include:

* dB level
* Frequency setting
* Audio file
* Measurement point
* Operating condition
* Lubrication condition
* Leak location
* Electrical discharge indication

Ultrasound can help detect:

* Air leaks
* Steam leaks
* Bearing lubrication problems
* Electrical arcing
* Cavitation
* Early friction

---

## Visual Inspection Model

Visual inspection records may include:

* Inspection checklist
* Photos
* Videos
* Observations
* Defect category
* Severity
* Recommended action
* Inspector notes

Visual inspection can help detect:

* Cracks
* Corrosion
* Leakage
* Loose bolts
* Belt damage
* Oil leakage
* Abnormal noise
* Abnormal vibration
* Misalignment signs
* Structural damage

---

## Process Data Model

Process data can provide operating context for condition monitoring.

Examples:

* Motor current
* Equipment load
* Flow rate
* Pressure
* Temperature
* Production rate
* Fan damper position
* Mill feed rate
* Kiln speed
* Differential pressure

Process data helps distinguish between:

* Real equipment degradation
* Load-related changes
* Process-related disturbances
* Operating condition effects

---

## Condition Monitoring Workflow

A typical ARIP condition monitoring workflow:

```text
Asset Selection
    ↓
Measurement Point Selection
    ↓
Inspection or Data Collection
    ↓
Data Validation
    ↓
Threshold Comparison
    ↓
Trend Analysis
    ↓
Health Assessment
    ↓
Possible Failure Mode Mapping
    ↓
Recommendation
    ↓
Maintenance Follow-up
```

---

## Relationship with Reliability Intelligence

Condition monitoring data should connect to reliability intelligence.

Example relationship:

```text
Measurement Record
    → indicates Symptom
        → related to Failure Mode
            → caused by Root Cause
                → mitigated by Maintenance Action
```

This allows ARIP to support:

* Fault detection
* Fault classification
* Root cause analysis
* Risk prioritization
* Remaining useful life estimation
* Maintenance recommendation

---

## Relationship with Knowledge Graph

Condition monitoring entities can be connected through the ARIP knowledge graph.

Example:

```text
Equipment -> has_component -> Component
Component -> has_measurement_point -> Measurement Point
Measurement Point -> has_record -> Measurement Record
Measurement Record -> indicates -> Symptom
Symptom -> suggests -> Failure Mode
Failure Mode -> caused_by -> Root Cause
Failure Mode -> mitigated_by -> Maintenance Action
```

---

## Relationship with Digital Twin

Condition monitoring data updates the digital twin state of an asset.

Examples:

* Vibration data updates Reliability Twin
* Temperature data updates Physical Twin
* Process data updates Process Twin
* Energy data updates Energy Twin
* AI predictions update AI Twin

---

## Data Quality Considerations

Condition monitoring data quality is critical.

Important data quality dimensions:

* Completeness
* Accuracy
* Timestamp correctness
* Unit consistency
* Measurement point correctness
* Instrument calibration status
* Operating condition context
* Inspector notes
* Attachment quality

Poor data quality should reduce confidence in health assessment and AI prediction.

---

## Initial Implementation Recommendation

The first implementation should focus on:

* Equipment registry
* Measurement point registry
* Manual vibration records
* Temperature records
* Visual inspection records
* Basic thresholds
* Trend view
* Simple health status

This creates a practical foundation before adding advanced AI, digital twins, and knowledge graph reasoning.

---

## Future Extensions

Future extensions may include:

* Automated vibration spectrum analysis
* AI-based fault classification
* Oil analysis interpretation engine
* Thermography image analysis
* Ultrasound audio analysis
* Online sensor integration
* SCADA integration
* Mobile offline inspection routes
* Automatic work order recommendation
* RUL prediction
* Cross-asset learning
