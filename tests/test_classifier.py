import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_credible_news_prediction():
    payload = {
        "text": "According to official reports published in the journal, the spokesperson confirmed the findings."
    }
    res = client.post("/api/v1/classifier/predict", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "REAL" in data["prediction_label"]
    assert data["credibility_score"] >= 0.5

def test_fake_news_prediction():
    payload = {
        "text": "SHOCKING SECRET REVEALED! YOU WON'T BELIEVE THIS MIRACLE CURE THEY HID FROM YOU!"
    }
    res = client.post("/api/v1/classifier/predict", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "FAKE" in data["prediction_label"]
    assert data["credibility_score"] < 0.5
