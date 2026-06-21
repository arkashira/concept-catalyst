import json
from prototype_guidance import PrototypeDevelopmentGuidance, PrototypeGuidance

def test_get_guidance():
    guidance = PrototypeDevelopmentGuidance()
    result = guidance.get_guidance("idea1")
    assert result.idea == "idea1"
    assert result.resources == ["resource1", "resource2"]
    assert result.tips == ["tip1", "tip2"]

def test_get_guidance_unknown_idea():
    guidance = PrototypeDevelopmentGuidance()
    result = guidance.get_guidance("unknown_idea")
    assert result.idea == "unknown_idea"
    assert result.resources == []
    assert result.tips == []

def test_add_guidance():
    guidance = PrototypeDevelopmentGuidance()
    guidance.add_guidance("new_idea", ["new_resource1", "new_resource2"], ["new_tip1", "new_tip2"])
    result = guidance.get_guidance("new_idea")
    assert result.idea == "new_idea"
    assert result.resources == ["new_resource1", "new_resource2"]
    assert result.tips == ["new_tip1", "new_tip2"]

def test_save_guidance():
    guidance = PrototypeDevelopmentGuidance()
    guidance.add_guidance("new_idea", ["new_resource1", "new_resource2"], ["new_tip1", "new_tip2"])
    guidance.save_guidance("guidance.json")
    with open("guidance.json", "r") as f:
        data = json.load(f)
    assert data["new_idea"] == {"resources": ["new_resource1", "new_resource2"], "tips": ["new_tip1", "new_tip2"]}

def test_load_guidance():
    guidance = PrototypeDevelopmentGuidance()
    guidance.add_guidance("new_idea", ["new_resource1", "new_resource2"], ["new_tip1", "new_tip2"])
    guidance.save_guidance("guidance.json")
    guidance.load_guidance("guidance.json")
    result = guidance.get_guidance("new_idea")
    assert result.idea == "new_idea"
    assert result.resources == ["new_resource1", "new_resource2"]
    assert result.tips == ["new_tip1", "new_tip2"]
