from pydantic import BaseModel

class NewsRequest(BaseModel):
    text: str

class NewsResponse(BaseModel):
    text_snippet: str
    prediction: str
    confidence_score: float
    reasoning: str