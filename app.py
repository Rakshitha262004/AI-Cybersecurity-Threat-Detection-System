import streamlit as st
import pandas as pd

from src.preprocessing import preprocess_data
from src.model import train_model
from src.detection import detect_threats

st.set_page_config(page_title="Cyber Threat Detection", layout="wide")

# Title
st.title("🔐 AI-Powered Cybersecurity Threat Detection System")

st.markdown("Detect network intrusions using Machine Learning")

# Upload file
uploaded_file = st.file_uploader("📂 Upload Dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.success("✅ Dataset loaded successfully!")

else:
    st.warning("⚠️ No file uploaded. Using default dataset...")
    data = pd.read_csv("data/dataset.csv")

# Show data preview
if st.checkbox("Show Dataset"):
    st.dataframe(data.head())

# Run detection
if st.button("🚀 Run Threat Detection"):

    st.info("🔄 Preprocessing data...")
    X_train, X_test, y_train, y_test = preprocess_data(data)

    st.info("🤖 Training model...")
    model = train_model(X_train, y_train)

    st.info("🔍 Detecting threats...")
    predictions = model.predict(X_test)

    results = pd.DataFrame({
        "Prediction": predictions
    })

    results["Prediction"] = results["Prediction"].map({
        0: "Normal",
        1: "Attack"
    })

    st.success("✅ Detection Completed!")

    # Show results
    st.subheader("📊 Prediction Results")
    st.dataframe(results.head(20))

    # Show alerts
    st.subheader("🚨 Alerts")

    for i, pred in enumerate(predictions[:20]):
        if pred == 1:
            st.error(f"⚠️ Threat detected at index {i}")
        else:
            st.success(f"✅ Normal activity at index {i}")

    # Summary
    st.subheader("📈 Summary")

    attack_count = sum(predictions)
    normal_count = len(predictions) - attack_count

    st.write(f"🔴 Attacks Detected: {attack_count}")
    st.write(f"🟢 Normal Traffic: {normal_count}")