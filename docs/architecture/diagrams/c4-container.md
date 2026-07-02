# ARIP C4 Container Diagram

## Overview

This document provides the initial C4 Container Diagram for ARIP — Autonomous Reliability Intelligence Platform.

The C4 Container Diagram shows the major deployable and logical containers that make up the ARIP platform.

---

## Container Diagram

```mermaid
flowchart TB
    subgraph Users["Users"]
        U1["Reliability Engineer"]
        U2["Condition Monitoring Inspector"]
        U3["Maintenance Engineer"]
        U4["Plant Manager"]
        U5["System Administrator"]
    end

    subgraph ClientLayer["Client Layer"]
        C1["Web Frontend<br/>React + TypeScript + MUI"]
        C2["Offline-First PWA<br/>IndexedDB + Sync Queue"]
    end

    subgraph BackendLayer["Backend Layer"]
        B1["API Gateway / Backend API<br/>FastAPI"]
        B2["Asset Service"]
        B3["Condition Monitoring Service"]
        B4["Reliability Intelligence Service"]
        B5["Digital Twin Service"]
        B6["Reporting Service"]
        B7["Authentication and Authorization"]
    end

    subgraph IntelligenceLayer["Intelligence Layer"]
        I1["Industrial AI Service"]
        I2["Knowledge Graph Service"]
        I3["Rule Engine"]
        I4["Recommendation Engine"]
    end

    subgraph DataLayer["Data Layer"]
        D1["PostgreSQL<br/>Transactional Data"]
        D2["Time-Series Storage<br/>Trends and Sensor Data"]
        D3["Object Storage<br/>Files, Images, Reports"]
        D4["Graph Database<br/>Knowledge Graph"]
        D5["Local Device Storage<br/>IndexedDB"]
    end

    subgraph IntegrationLayer["Integration Layer"]
        X1["SCADA / DCS Connector"]
        X2["OPC UA / MQTT / Modbus Gateway"]
        X3["CMMS / EAM Connector"]
        X4["Document Import Pipeline"]
        X5["Lab Report Import Pipeline"]
    end

    U1 --> C1
    U2 --> C2
    U3 --> C1
    U4 --> C1
    U5 --> C1

    C1 --> B1
    C2 --> B1
    C2 --> D5

    B1 --> B2
    B1 --> B3
    B1 --> B4
    B1 --> B5
    B1 --> B6
    B1 --> B7

    B2 --> D1
    B3 --> D1
    B3 --> D2
    B3 --> D3
    B4 --> D1
    B5 --> D1
    B6 --> D3
    B7 --> D1

    B4 --> I3
    B4 --> I4
    B4 --> I2
    B5 --> I1
    B3 --> I1
    I2 --> D4
    I1 --> D1
    I1 --> D2
    I4 --> D1

    X1 --> D2
    X2 --> D2
    X3 <--> B1
    X4 --> D3
    X5 --> D3
    X5 --> B3
```

---

## Container Responsibilities

### Web Frontend

The Web Frontend provides the main user interface for engineers, managers, administrators, and contributors.

It includes:

* Dashboard views
* Asset registry views
* Condition monitoring views
* Reliability intelligence views
* Digital twin views
* Reports
* Settings and administration

Recommended technologies:

* React
* TypeScript
* Material UI
* React Router
* API client layer

---

### Offline-First PWA

The Offline-First PWA supports field inspection and condition monitoring workflows in low-connectivity industrial environments.

It includes:

* Local equipment cache
* Local measurement point cache
* Inspection drafts
* Local sync queue
* Sync status
* Offline form entry

Recommended technologies:

* React
* TypeScript
* IndexedDB
* Dexie.js
* Service Worker
* PWA manifest

---

### Backend API

The Backend API is the main server-side entry point for ARIP.

It exposes REST or future event-based APIs for:

* Assets
* Equipment hierarchy
* Measurement points
* Inspection records
* Condition monitoring data
* Reliability intelligence
* Digital twin state
* Reports
* Authentication and authorization

Recommended technologies:

* FastAPI
* Pydantic
* SQLAlchemy
* Alembic
* PostgreSQL

---

### Asset Service

The Asset Service manages the industrial asset hierarchy.

It is responsible for:

* Plants
* Areas
* Systems
* Equipment
* Components
* Measurement points
* Asset metadata
* Equipment criticality
* Asset status

---

### Condition Monitoring Service

The Condition Monitoring Service manages inspection and monitoring records.

It is responsible for:

* Vibration records
* Temperature records
* Thermography metadata
* Oil analysis records
* Ultrasound records
* Visual inspection records
* Thresholds
* Baselines
* Health assessments

---

### Reliability Intelligence Service

The Reliability Intelligence Service transforms asset and condition data into engineering decisions.

It is responsible for:

* Failure modes
* Symptoms
* Root causes
* Risk scores
* Health scores
* RCA support
* Maintenance recommendations
* Historical case comparison

---

### Digital Twin Service

The Digital Twin Service manages asset state representations.

It is responsible for:

* Physical Twin state
* Functional Twin state
* Process Twin state
* Reliability Twin state
* Energy Twin state
* AI Twin state
* Twin update events

---

### Industrial AI Service

The Industrial AI Service supports explainable diagnostics and decision support.

It may include:

* Anomaly detection
* Fault classification
* RUL estimation
* Similar case search
* AI-assisted reporting
* Explainable diagnostics
* Human-in-the-loop feedback

---

### Knowledge Graph Service

The Knowledge Graph Service manages industrial reliability relationships.

It connects:

* Assets
* Components
* Measurement points
* Symptoms
* Failure modes
* Root causes
* Maintenance actions
* Spare parts
* Historical cases

---

### Data Stores

ARIP may use different data stores for different types of data:

* PostgreSQL for transactional and relational data
* Time-series storage for sensor and trend data
* Object storage for files, reports, and images
* Graph database for industrial knowledge relationships
* IndexedDB for local offline-first field workflows

---

## Deployment Notes

The first implementation may run as a Docker Compose-based system for local development.

A future production deployment may use:

* Docker
* Kubernetes or K3s
* PostgreSQL
* Object storage
* Graph database
* Reverse proxy
* Monitoring and logging stack

---

## Related Documentation

* [Platform Architecture Diagram](platform-architecture.md)
* [C4 Context Diagram](c4-context.md)
* [Architecture Overview](../architecture-overview.md)
* [Asset Hierarchy Model](../asset-hierarchy-model.md)
* [Offline-First Architecture](../offline-first-architecture.md)
* [Condition Monitoring Domain Model](../../condition-monitoring/condition-monitoring-domain-model.md)
* [Reliability Intelligence Domain Model](../../reliability/reliability-intelligence-domain-model.md)
* [Knowledge Graph Concept](../../knowledge-graph/knowledge-graph-concept.md)
* [Digital Twin Concept](../../digital-twin/digital-twin-concept.md)
* [Industrial AI Concept](../../ai/industrial-ai-concept.md)
