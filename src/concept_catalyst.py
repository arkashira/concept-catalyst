import json
from dataclasses import dataclass
from typing import List

@dataclass
class Hypothesis:
    description: str
    success_metrics: str

def generate_hypotheses(idea: str) -> List[Hypothesis]:
    if not idea or len(idea) > 500:
        raise ValueError("Idea must be between 1 and 500 characters")
    # Simple natural language processing to generate hypotheses
    keywords = idea.split()
    hypotheses = []
    for keyword in keywords:
        hypothesis = Hypothesis(
            description=f"Test if {keyword} is a key factor",
            success_metrics=f"Measure the impact of {keyword} on the outcome"
        )
        hypotheses.append(hypothesis)
    # Limit to 3-5 hypotheses
    return hypotheses[:5]

def get_editable_templates() -> List[str]:
    return [
        "Customer Segment: _______________",
        "Target Problem: _______________",
        "Success Metrics: _______________"
    ]
