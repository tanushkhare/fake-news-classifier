from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class ClassificationRequest(BaseModel):
    text: str = Field(..., min_length=15, description="News article or headline to evaluate")
    metadata: Optional[Dict[str, str]] = Field(default_factory=dict, description="Source context")

class ClassificationResponse(BaseModel):
    text_preview: str
    prediction_label: str
    credibility_score: float
    confidence: float
    linguistic_cues: List[str]
    verdict: str
