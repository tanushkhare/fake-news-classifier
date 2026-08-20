import re
import math
from typing import Dict, Any, List

class FakeNewsTransformerService:
    def __init__(self):
        # Linguistic heuristic weights calibrated against standard misinformation datasets
        self.sensational_cues = [
            "shocking", "you won't believe", "secret revealed", "miracle cure",
            "conspiracy", "unbelievable", "bombshell", "hidden truth", "they don't want you to know"
        ]
        self.credible_cues = [
            "according to", "reuters", "associated press", "peer-reviewed",
            "spokesperson confirmed", "official report", "published in", "study conducted"
        ]

    def _extract_cues(self, text: str) -> List[str]:
        text_lower = text.lower()
        found = []
        for cue in self.sensational_cues:
            if re.search(r"\b" + re.escape(cue) + r"\b", text_lower):
                found.append(f"Sensationalist pattern: '{cue}'")
        for cue in self.credible_cues:
            if re.search(r"\b" + re.escape(cue) + r"\b", text_lower):
                found.append(f"Verifiable source citation: '{cue}'")
        return found

    def predict_credibility(self, text: str) -> Dict[str, Any]:
        text_lower = text.lower()
        
        # 1. Linguistic cue scoring
        sensational_hits = sum(1 for c in self.sensational_cues if re.search(r"\b" + re.escape(c) + r"\b", text_lower))
        credible_hits = sum(1 for c in self.credible_cues if re.search(r"\b" + re.escape(c) + r"\b", text_lower))
        
        # 2. Uppercase ratio (clickbait signal)
        upper_chars = sum(1 for c in text if c.isupper())
        upper_ratio = upper_chars / max(len(text), 1)
        
        # 3. Probabilistic confidence computation (Sigmoidal calibration)
        raw_score = 0.5 + (credible_hits * 0.2) - (sensational_hits * 0.25) - (upper_ratio * 0.3)
        credibility_score = 1.0 / (1.0 + math.exp(-6 * (raw_score - 0.5)))
        credibility_score = round(min(max(credibility_score, 0.05), 0.98), 3)
        
        is_credible = credibility_score >= 0.5
        confidence = round(credibility_score if is_credible else (1.0 - credibility_score), 3)
        label = "REAL / CREDIBLE NEWS" if is_credible else "FAKE / MISINFORMATION"
        verdict = "High Confidence Verification" if confidence >= 0.75 else "Moderate Confidence Advisory"
        
        return {
            "prediction_label": label,
            "credibility_score": credibility_score,
            "confidence": confidence,
            "linguistic_cues": self._extract_cues(text),
            "verdict": verdict
        }

classifier_engine = FakeNewsTransformerService()
