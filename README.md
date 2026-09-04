# ⚡ Fake News Classifier

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://fake-news-classifier-web.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)

🔗 **Production URL:** [https://fake-news-classifier-web.vercel.app](https://fake-news-classifier-web.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
Calibrated neural credibility classifier utilizing HuggingFace DistilBERT models to evaluate article veracity, sensationalism markers, and citation authenticity.

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** HuggingFace, DistilBERT, PyTorch, FastAPI
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🛡️ Production Standards
* **Neural Classification:** Replaced keyword heuristics with calibrated softmax logit probabilities.
* **Explainability Output:** Highlights textual cues and attribution factors driving the verdict.
* **Batch Ready:** Supports single-text evaluation and high-volume batch scoring.

---

## 🚀 API Contracts
```http
POST /api/v1/classifier/predict
Request:
{
  "text": "According to a peer-reviewed study published in Nature, researchers confirmed the discovery..."
}

Response (200 OK):
{
  "verdict": "CREDIBLE",
  "credibility_score": 0.912,
  "confidence": 0.940,
  "signals": [
    "Reputable academic citation pattern identified ('Nature')",
    "Low sensationalism score"
  ]
}

GET /health
Response: {"status": "healthy"}
💻 Local Quickstart

Bash

pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v