from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import classifier

app = FastAPI(
    title="AI Fake News Classifier API",
    version="1.0.0",
    description="API for analyzing and classifying news articles for credibility."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(classifier.router)

@app.get("/")
def read_root():
    return {"message": "Fake News Classifier Backend is running successfully!"}