import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.concept_catalyst import generate_hypotheses, get_editable_templates, Hypothesis
import pytest

def test_generate_hypotheses():
    idea = "Improve customer engagement"
    hypotheses = generate_hypotheses(idea)
    assert len(hypotheses) > 0
    assert all(isinstance(h, Hypothesis) for h in hypotheses)

def test_generate_hypotheses_edge_case():
    idea = "a" * 501
    with pytest.raises(ValueError):
        generate_hypotheses(idea)

def test_get_editable_templates():
    templates = get_editable_templates()
    assert len(templates) == 3
    assert all(isinstance(t, str) for t in templates)
