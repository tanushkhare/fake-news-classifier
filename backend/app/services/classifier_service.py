def classify_news_text(text: str):
    # Lightweight text analysis heuristic / NLP classification model pipeline placeholder
    sensational_keywords = ["shocking", "miracle", "secret", "they don't want you to know", "exposed", "unbelievable"]
    score = sum(1 for word in sensational_keywords if word in text.lower())
    
    is_fake = score > 0
    confidence = min(0.55 + (score * 0.15), 0.98) if is_fake else 0.88
    
    return {
        "text_snippet": text[:100] + "..." if len(text) > 100 else text,
        "prediction": "FAKE" if is_fake else "REAL",
        "confidence_score": round(confidence, 2),
        "reasoning": "Detected sensationalist or unverified phrasing patterns." if is_fake else "Tone appears objective and standard."
    }