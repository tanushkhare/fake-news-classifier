import streamlit as st
import requests

st.title("📰 AI Fake News Classifier")
st.write("Analyze articles or text snippets to check for potential misinformation and sensationalism.")

news_text = st.text_area("Paste News Article Text Here:", height=150)

if st.button("Classify News"):
    if news_text.strip():
        try:
            response = requests.post("http://127.0.0.1:8000/api/classify", json={"text": news_text})
            if response.status_code == 200:
                data = response.json()
                
                prediction = data["prediction"]
                if prediction == "FAKE":
                    st.error(f"🚨 Prediction: **{prediction}**")
                else:
                    st.success(f"✅ Prediction: **{prediction}**")
                    
                st.write(f"**Confidence Score:** {data['confidence_score'] * 100}%")
                st.info(f"**Reasoning:** {data['reasoning']}")
            else:
                st.error("Error communicating with the backend API.")
        except Exception as e:
            st.error(f"Could not connect to FastAPI server: {e}")
    else:
      st.warning("Please enter some text to analyze.")