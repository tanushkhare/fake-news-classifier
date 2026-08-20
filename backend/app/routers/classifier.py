from fastapi import APIRouter
from app.schemas.classifier import NewsRequest, NewsResponse
from app.services.classifier_service import classify_news_text

router = APIRouter(prefix="/api", tags=["Fake News Classifier"])

@router.post("/classify", response_model=NewsResponse)
def classify_news(payload: NewsRequest):
    return classify_news_text(payload.text)