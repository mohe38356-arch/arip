# ARIP Offline-First Architecture

## Overview

ARIP is designed for industrial environments where network connectivity may be limited, unreliable, restricted, or fully disconnected from the public internet.

Many industrial plants operate with strict cybersecurity policies, internal-only networks, limited Wi-Fi coverage, and restricted access to external cloud services. For this reason, ARIP follows an offline-first architecture.

Offline-first does not mean offline-only. It means the system should continue to support critical field workflows even when the user is temporarily disconnected from the central server.

---

## Purpose

The Offline-First Architecture helps ARIP support:

* Field inspections without continuous network access
* Mobile and tablet data entry inside industrial areas
* Local equipment information access
* Local checklist completion
* Offline condition monitoring records
* Attachment capture such as photos and notes
* Sync after reconnection to the internal plant network
* Reduced dependency on public internet services

---

## Core Design Principle

ARIP follows this offline-first principle:

> Critical industrial inspection workflows should not fail only because the network is unavailable.

A user should be able to:

* Open assigned inspection routes
* View cached asset information
* Record measurements
* Add observations
* Capture photos
* Save inspection drafts
* Continue working offline
* Synchronize changes later

---

## Target Offline Scenarios

ARIP should support the following offline or low-connectivity scenarios:

* Inspector enters a plant area without Wi-Fi coverage
* Tablet temporarily loses connection to the internal server
* Internal network is unstable during inspection
* Public internet access is blocked by plant policy
* Maintenance team needs access to cached asset information
* Inspection data must be collected during shutdown or field activity

---

## Offline-First Architecture Flow

```text
Central Server
    ↓
Initial Data Sync
    ↓
Local Device Cache
    ↓
Offline Inspection Work
    ↓
Local Change Queue
    ↓
Reconnect to Internal Network
    ↓
Sync Engine
    ↓
Conflict Detection
    ↓
Server Update
    ↓
Audit Log
```

---

## Main Components

### 1. Central Server

The central server is the source of truth for validated industrial data.

It may include:

* Backend API
* PostgreSQL database
* File storage
* Authentication service
* Audit log
* Sync API
* Reporting service

---

### 2. Local Device Cache

The local device cache stores the data needed for offline work.

It may include:

* Assigned inspection routes
* Equipment list
* Measurement points
* Recent condition history
* Thresholds
* Checklists
* Draft inspection records
* User permissions
* Reference data

In a web-based PWA, this can be implemented using IndexedDB.

---

### 3. Sync Queue

The sync queue stores changes created while offline.

Examples:

* New vibration records
* Temperature measurements
* Visual inspection observations
* Uploaded photos
* Updated checklist items
* Draft notes
* Maintenance recommendations
* Corrected equipment metadata

Each queued change should include:

* Local ID
* Entity type
* Operation type
* Payload
* Timestamp
* User ID
* Device ID
* Sync status
* Retry count
* Conflict status

---

### 4. Sync Engine

The sync engine sends local changes to the server when the device reconnects.

The sync engine should support:

* Retry logic
* Partial sync
* Ordered sync
* Error handling
* Conflict detection
* Conflict resolution
* User notification
* Audit logging

---

### 5. Conflict Detection

Conflicts may occur when two users modify the same data while disconnected.

Examples:

* Two inspectors edit the same checklist
* Equipment metadata changes while an inspector is offline
* A measurement point is renamed before offline data is synced
* A threshold is updated during offline work

Conflict detection should compare:

* Entity version
* Last modified timestamp
* User ID
* Operation type
* Server state
* Local state

---

### 6. Conflict Resolution

Conflict resolution can use different strategies depending on the data type.

Possible strategies:

* Server wins
* Client wins
* Last write wins
* Manual review
* Field-level merge
* Domain-specific rule

Recommended approach:

* Critical engineering data should require manual review.
* Simple draft notes may use last-write-wins.
* Measurement records should usually be appended, not overwritten.
* Audit history should never be deleted.

---

## Offline Data Categories

### Reference Data

Reference data can be cached locally.

Examples:

* Plants
* Areas
* Systems
* Equipment
* Components
* Measurement points
* Monitoring methods
* Thresholds
* Checklists

---

### Transactional Data

Transactional data is created by users during field work.

Examples:

* Inspection events
* Measurement records
* Visual observations
* Photos
* Notes
* Draft reports
* Maintenance follow-up records

---

### Attachment Data

Attachments may include:

* Photos
* Thermal images
* Audio files
* PDF reports
* Inspection evidence
* Measurement exports

Attachments should be stored locally until successfully uploaded.

---

## Data Integrity Requirements

Offline data must preserve integrity.

Important requirements:

* No silent data loss
* Clear sync status
* Local draft protection
* User-visible errors
* Retry after failure
* Audit trail after sync
* Timestamp preservation
* Device identity tracking
* User identity tracking

---

## Security Requirements

Offline-first systems require special security attention.

Important security requirements:

* Local data encryption where possible
* Secure authentication token handling
* Session expiration rules
* Role-based offline access
* Device-level access protection
* Attachment access control
* Sensitive data minimization
* Audit logging after sync

---

## Recommended PWA Approach

The first ARIP implementation can use a Progressive Web App approach.

Suggested client-side technologies:

* React
* TypeScript
* IndexedDB
* Dexie.js
* Service Worker
* Background Sync when available
* Local sync queue
* PWA install support

Suggested offline capabilities:

* Cache application shell
* Cache reference data
* Store inspection drafts locally
* Queue write operations
* Sync when connection returns
* Show sync status to user

---

## Example Offline Workflow

Example: vibration inspection route.

```text
User logs in while online
    ↓
Assigned route is downloaded
    ↓
Equipment and measurement points are cached
    ↓
User enters plant area without connection
    ↓
User records vibration values
    ↓
Records are stored in local queue
    ↓
User reconnects to internal network
    ↓
Sync engine uploads records
    ↓
Server validates and stores records
    ↓
Health status is recalculated
    ↓
Audit log is updated
```

---

## Sync Status Values

A local record may have one of the following sync states:

* Draft
* Pending Sync
* Syncing
* Synced
* Sync Failed
* Conflict
* Needs Review

These states should be visible to the user.

---

## Relationship with Asset Hierarchy

Offline data should remain connected to the asset hierarchy.

Cached records should preserve references to:

* Plant
* Area
* System
* Equipment
* Component
* Measurement point

This ensures that offline records remain meaningful after synchronization.

---

## Relationship with Condition Monitoring

Offline-first support is especially important for condition monitoring.

Examples:

* Manual vibration measurements
* Temperature readings
* Visual inspection observations
* Oil sampling notes
* Thermography route notes
* Ultrasound inspection notes

Condition monitoring records should be stored locally and synchronized safely.

---

## Relationship with Security

Offline data may remain on field devices.

Security considerations include:

* Which users can cache which assets
* How long offline data remains available
* Whether attachments are encrypted
* Whether logout clears local cache
* Whether failed sync data can be exported
* How device loss is handled

---

## Initial Implementation Recommendation

The first offline-first implementation should focus on:

* IndexedDB local storage
* Equipment cache
* Measurement point cache
* Inspection draft records
* Local sync queue
* Basic sync status
* Manual retry button
* Simple conflict detection
* Server-side validation after sync

This is practical and suitable for the early ARIP prototype.

---

## Future Extensions

Future extensions may include:

* Advanced conflict resolution
* CRDT-based collaborative offline editing
* Offline report generation
* Encrypted local database
* Offline technical document cache
* Offline AI inference
* Edge-server synchronization
* Multi-device sync
* Device management
* Offline role-based authorization
* Plant-local package updates
