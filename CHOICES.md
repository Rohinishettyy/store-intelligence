# Store Intelligence System - CHOICES.md

# 1. Detection Model Choice

## Options Considered
- YOLOv8
- MediaPipe
- RT-DETR

## AI Suggestions
AI tools suggested YOLOv8 because of:
- Fast inference speed
- Lightweight deployment
- Strong real-time object detection performance
- Easy integration with Python pipelines

## Final Decision
YOLOv8 was selected because it balances:
- Accuracy
- Simplicity
- Speed
- Ease of deployment

The model works effectively for real-time person detection in CCTV-style retail environments.

---

# 2. Event Schema Design

## Design Goal
The event schema was designed to simulate production-style retail analytics systems.

Each event includes:
- event_id
- store_id
- visitor_id
- timestamp
- zone_id
- confidence score
- metadata

## AI Suggestions
AI tools suggested:
- Including metadata fields for extensibility
- Maintaining unique event identifiers
- Using JSON-compatible schemas for API communication

## Final Decision
A structured schema was implemented to support:
- Real-time analytics
- Dashboard visualization
- Future database integration
- Scalable event processing

---

# 3. API Architecture Choice

## Options Considered
- Flask
- FastAPI
- Monolithic script-based architecture

## AI Suggestions
AI tools recommended FastAPI because of:
- Built-in schema validation
- High performance
- Easy REST API creation
- Modern async support

## Final Decision
FastAPI was selected because it allows:
- Modular API development
- Clean routing structure
- Easy testing
- Production-style backend implementation

The architecture separates:
- ingestion
- metrics
- heatmap
- anomaly detection
- queue analytics

This modular design improves maintainability and scalability.

---

# Additional Engineering Decisions

## Why Streamlit?
Streamlit was selected for rapid dashboard prototyping and live analytics visualization.

## Why Rule-Based Anomaly Detection?
A rule-based system was implemented for:
- Simplicity
- Explainability
- Fast implementation during the hackathon timeline

Future versions may include ML-based anomaly detection models.