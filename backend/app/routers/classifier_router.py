from fastapi import APIRouter, HTTPException
from backend.app.schemas.classifier_schema import ClassificationRequest, ClassificationResponse
from backend.app.services.classifier_service import classifier_engine

router = APIRouter(prefix="/api/v1/classifier", tags=["News Credibility Classifier"])

@router.post("/predict", response_model=ClassificationResponse)
async def classify_news(payload: ClassificationRequest):
    if len(payload.text.strip()) < 15:
        raise HTTPException(status_code=422, detail="Input text must contain at least 15 characters.")
    
    result = classifier_engine.predict_credibility(payload.text)
    
    return ClassificationResponse(
        text_preview=payload.text[:120] + ("..." if len(payload.text) > 120 else ""),
        prediction_label=result["prediction_label"],
        credibility_score=result["credibility_score"],
        confidence=result["confidence"],
        linguistic_cues=result["linguistic_cues"],
        verdict=result["verdict"]
    )
