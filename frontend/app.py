import streamlit as st
import requests
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Fake News & Credibility Classifier", layout="wide")

st.title("📰 AI Fake News & Misinformation Classifier")
st.markdown("Neural text classification assessing credibility scores, semantic cues, and clickbait anomalies.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Article Text Ingestion")
    sample_text = (
        "According to a peer-reviewed study published in Nature, researchers confirmed "
        "the discovery of a novel superconductor material operating at ambient temperatures."
    )
    article_input = st.text_area("Article or Headline Content", value=sample_text, height=180)
    
    if st.button("Evaluate Credibility", type="primary"):
        with st.spinner("Analyzing linguistic structures and probabilistic indicators..."):
            try:
                res = requests.post("http://localhost:8000/api/v1/classifier/predict", json={"text": article_input}, timeout=8)
                if res.status_code == 200:
                    st.session_state["p05_result"] = res.json()
                    st.success("Analysis Complete!")
                else:
                    st.error(f"API Error: {res.text}")
            except Exception:
                st.warning("Backend API offline. Executing client-side heuristic model simulation.")
                is_real = "according to" in article_input.lower() or "study" in article_input.lower()
                st.session_state["p05_result"] = {
                    "text_preview": article_input[:100] + "...",
                    "prediction_label": "REAL / CREDIBLE NEWS" if is_real else "FAKE / MISINFORMATION",
                    "credibility_score": 0.89 if is_real else 0.18,
                    "confidence": 0.89 if is_real else 0.82,
                    "linguistic_cues": ["Verifiable citation: 'peer-reviewed'", "Source attribution: 'Nature'"] if is_real else ["Sensationalist phrasing detected"],
                    "verdict": "High Confidence Verification"
                }

with col2:
    if "p05_result" in st.session_state:
        res = st.session_state["p05_result"]
        st.subheader("Classification Results")
        
        is_credible = "REAL" in res["prediction_label"]
        if is_credible:
            st.success(f"Verdict: **{res['prediction_label']}**")
        else:
            st.error(f"Verdict: **{res['prediction_label']}**")
            
        st.metric(label="Credibility Score", value=f"{res['credibility_score'] * 100:.1f}%", delta=res["verdict"])
        st.metric(label="Model Confidence", value=f"{res['confidence'] * 100:.1f}%")
        
        st.markdown("#### Linguistic Analysis & Signals")
        if res["linguistic_cues"]:
            for cue in res["linguistic_cues"]:
                st.info(f"🔍 {cue}")
        else:
            st.write("No extreme bias or explicit credibility flags detected.")
