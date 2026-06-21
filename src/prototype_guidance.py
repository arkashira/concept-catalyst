import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class PrototypeGuidance:
    idea: str
    resources: List[str]
    tips: List[str]

class PrototypeDevelopmentGuidance:
    def __init__(self):
        self.guidance_data = {
            "idea1": {"resources": ["resource1", "resource2"], "tips": ["tip1", "tip2"]},
            "idea2": {"resources": ["resource3", "resource4"], "tips": ["tip3", "tip4"]},
        }

    def get_guidance(self, idea: str) -> PrototypeGuidance:
        if idea in self.guidance_data:
            return PrototypeGuidance(idea, self.guidance_data[idea]["resources"], self.guidance_data[idea]["tips"])
        else:
            return PrototypeGuidance(idea, [], [])

    def add_guidance(self, idea: str, resources: List[str], tips: List[str]) -> None:
        self.guidance_data[idea] = {"resources": resources, "tips": tips}

    def save_guidance(self, filename: str) -> None:
        with open(filename, "w") as f:
            json.dump(self.guidance_data, f)

    def load_guidance(self, filename: str) -> None:
        try:
            with open(filename, "r") as f:
                self.guidance_data = json.load(f)
        except FileNotFoundError:
            pass
