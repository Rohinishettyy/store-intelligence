import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Store Intelligence Dashboard",
    layout="wide"
)

st.title("🛒 Store Intelligence Dashboard")

metrics = {
    "unique_visitors": 12,
    "entries": 25,
    "exits": 18,
    "total_events": 40
}

queue = {
    "store_id": "STORE_101",
    "queue_count": 5,
    "queue_status": "NORMAL"
}

heatmap = {
    "heatmap": {
        "ENTRY": 20,
        "BILLING": 10,
        "EXIT": 15
    }
}

anomalies = {
    "anomalies": ["No anomalies detected"]
}

# ---------------- UI ---------------- #

col1, col2, col3, col4 = st.columns(4)

col1.metric("Unique Visitors", metrics["unique_visitors"])
col2.metric("Entries", metrics["entries"])
col3.metric("Exits", metrics["exits"])
col4.metric("Total Events", metrics["total_events"])

st.divider()

st.subheader("📌 Queue Status")
st.write(queue)

st.divider()

st.subheader("🔥 Heatmap Analytics")

heatmap_data = heatmap["heatmap"]

df = pd.DataFrame(
    list(heatmap_data.items()),
    columns=["Zone", "Activity"]
)

st.bar_chart(df.set_index("Zone"))

st.divider()

st.subheader("⚠️ Anomalies")
st.success(anomalies["anomalies"][0])