import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Store Intelligence Dashboard",
    layout="wide"
)

st.title("🛒 Store Intelligence Dashboard")

BASE_URL = "http://localhost:8000"
try:
    metrics = requests.get(f"{BASE_URL}/stores/STORE_101/metrics").json()
    queue = requests.get(f"{BASE_URL}/stores/STORE_101/queue").json()
    heatmap = requests.get(f"{BASE_URL}/stores/STORE_101/heatmap").json()
    anomalies = requests.get(f"{BASE_URL}/stores/STORE_101/anomalies").json()
except:
    st.error("⚠️ Backend not running. Please start FastAPI server.")
    st.stop()


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Unique Visitors",
    metrics.get("unique_visitors", 0)
)

col2.metric(
    "Entries",
    metrics.get("entries", 0)
)

col3.metric(
    "Exits",
    metrics.get("exits", 0)
)

col4.metric(
    "Total Events",
    metrics.get("total_events", 0)
)

st.divider()

st.subheader("📌 Queue Status")

st.write(queue)

st.divider()

st.subheader("🔥 Heatmap Analytics")

heatmap_data = heatmap.get("heatmap", {})

if heatmap_data:

    heatmap_df = pd.DataFrame(
        heatmap_data.items(),
        columns=["Zone", "Activity"]
    )

    st.bar_chart(
        heatmap_df.set_index("Zone")
    )

else:

    st.warning("No heatmap data available")

st.divider()

st.subheader("⚠️ Anomalies")

anomalies_data = anomalies.get("anomalies", [])

if anomalies_data:

    st.error(anomalies_data)

else:

    st.success("No anomalies detected")