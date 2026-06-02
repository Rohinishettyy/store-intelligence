# Store Intelligence System - DESIGN.md

## Overview

The Store Intelligence Dashboard is an AI-powered retail analytics system designed to simulate real-time smart retail monitoring using computer vision and event-driven APIs.

The system processes CCTV/store surveillance footage using YOLOv8-based person detection and converts raw detections into structured retail intelligence events. These events are processed through FastAPI services to generate analytics such as visitor metrics, queue monitoring, heatmap analytics, and anomaly detection.

The architecture is modular and designed to resemble production-style retail intelligence systems used in modern smart stores.

---

# Architecture Overview

CCTV Footage → YOLOv8 Detection Pipeline → Event Generation → FastAPI Analytics APIs → Streamlit Dashboard

---

# Components

## 1. Detection Pipeline

The detection pipeline uses YOLOv8 for real-time person detection from CCTV footage.

Responsibilities:
- Detect people in frames
- Generate visitor events
- Assign temporary visitor identifiers
- Emit structured JSON events

The pipeline generates events such as:
- ENTRY
- EXIT
- BILLING activity
- Zone movement events

---

## 2. Event Ingestion Layer

FastAPI APIs ingest generated events into an in-memory event store.

Responsibilities:
- Validate event schema
- Store events
- Provide analytics endpoints
- Serve real-time dashboard requests

---

## 3. Analytics Engine

The analytics layer computes:
- Unique visitors
- Entry/exit counts
- Queue congestion
- Heatmap activity
- Rule-based anomalies

---

## 4. Dashboard Layer

A Streamlit dashboard visualizes all analytics in real time.

Dashboard Features:
- Visitor analytics
- Queue monitoring
- Heatmap visualization
- Anomaly alerts

---

# AI-Assisted Decisions

AI tools such as ChatGPT were used during:
- API architecture planning
- Event schema refinement
- Streamlit dashboard structuring
- README and documentation improvements

Several AI-generated suggestions were evaluated and selectively implemented after manual review and modification.

For example:
- YOLOv8 was selected after comparing lightweight real-time detection models
- A modular FastAPI architecture was chosen instead of a monolithic script
- Rule-based anomaly detection was preferred for simplicity and interpretability

---

# Design Trade-offs

## Why YOLOv8?
YOLOv8 provides fast inference speed and lightweight deployment suitable for real-time retail analytics.

## Why FastAPI?
FastAPI provides fast API development with automatic schema validation and high-performance asynchronous support.

## Why Streamlit?
Streamlit allows rapid dashboard development with minimal frontend complexity.

---

# Future Improvements

- Multi-camera tracking
- Persistent database integration
- Advanced visitor re-identification
- Cloud-native deployment
- Real-time event streaming with Kafka