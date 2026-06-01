# 🛒 Store Intelligence Dashboard

## 📌 Overview

Store Intelligence Dashboard is an AI-powered retail analytics system that processes CCTV/store surveillance footage using YOLOv8-based real-time person detection.

The system generates intelligent retail insights such as:

* Visitor Analytics
* Queue Monitoring
* Heatmap Analytics
* Anomaly Detection
* Live Dashboard Visualization

The project uses a FastAPI backend and Streamlit dashboard for real-time monitoring and analytics.

---

# 🚀 Features

✅ Real-time person detection using YOLOv8
✅ Event ingestion pipeline
✅ Visitor analytics
✅ Queue monitoring
✅ Heatmap analytics
✅ Anomaly detection
✅ FastAPI backend APIs
✅ Streamlit interactive dashboard

---

# 🧠 Tech Stack

## Backend

* FastAPI
* Python

## AI / Computer Vision

* YOLOv8
* OpenCV

## Frontend Dashboard

* Streamlit

## Data Handling

* Pandas

---

# 📂 Project Structure

```bash
store-intelligence/
│
├── app/
│   ├── anomaly.py
│   ├── heatmap.py
│   ├── ingestion.py
│   ├── main.py
│   ├── metrics.py
│   ├── models.py
│   └── queue.py
│
├── dashboard/
│   └── dashboard.py
│
├── pipeline/
│   └── detect.py
│
├── sample_videos/
│   └── store.mp4
│
├── outputs/
│
├── requirements.txt
│
├── README.md
│
└── yolov8n.pt
```

---

# 🔌 API Endpoints

## Event Ingestion

* `POST /events/ingest`

## Metrics

* `GET /stores/{store_id}/metrics`

## Queue Analytics

* `GET /stores/{store_id}/queue`

## Heatmap Analytics

* `GET /stores/{store_id}/heatmap`

## Anomaly Detection

* `GET /stores/{store_id}/anomalies`

---

# ⚙️ Setup Instructions

## 1️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

## 2️⃣ Run FastAPI Backend

```bash
uvicorn app.main:app --reload
```

## 3️⃣ Run Detection Pipeline

```bash
python pipeline/detect.py
```

## 4️⃣ Run Streamlit Dashboard

```bash
streamlit run dashboard/dashboard.py
```

---

# 📊 Dashboard Features

The dashboard displays:

* Unique Visitors
* Entries / Exits
* Queue Status
* Heatmap Analytics
* Anomaly Detection

---

# 📸 Outputs

Project screenshots and demo outputs are available inside the `outputs/` folder.

---

# 🔮 Future Improvements

* Multi-camera support
* Face recognition integration
* Advanced customer tracking
* Cloud deployment
* Advanced heatmap visualization

---

# 👩‍💻 Author

## Bukka Rohini

