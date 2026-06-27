import json
from dataclasses import dataclass
from typing import List

@dataclass
class Feedback:
    id: int
    comment: str
    upvotes: int
    downvotes: int

@dataclass
class Idea:
    id: int
    description: str
    feedback: List[Feedback]

class CommunityFeedbackLoop:
    def __init__(self):
        self.ideas = {}

    def add_idea(self, idea_id: int, description: str):
        self.ideas[idea_id] = Idea(id=idea_id, description=description, feedback=[])

    def add_feedback(self, idea_id: int, comment: str):
        if idea_id not in self.ideas:
            raise ValueError("Idea not found")
        feedback_id = len(self.ideas[idea_id].feedback) + 1
        self.ideas[idea_id].feedback.append(Feedback(id=feedback_id, comment=comment, upvotes=0, downvotes=0))

    def upvote_feedback(self, idea_id: int, feedback_id: int):
        if idea_id not in self.ideas:
            raise ValueError("Idea not found")
        for feedback in self.ideas[idea_id].feedback:
            if feedback.id == feedback_id:
                feedback.upvotes += 1
                return
        raise ValueError("Feedback not found")

    def downvote_feedback(self, idea_id: int, feedback_id: int):
        if idea_id not in self.ideas:
            raise ValueError("Idea not found")
        for feedback in self.ideas[idea_id].feedback:
            if feedback.id == feedback_id:
                feedback.downvotes += 1
                return
        raise ValueError("Feedback not found")

    def get_top_feedback(self, idea_id: int):
        if idea_id not in self.ideas:
            raise ValueError("Idea not found")
        return sorted(self.ideas[idea_id].feedback, key=lambda x: x.upvotes - x.downvotes, reverse=True)

    def auto_generate_summary(self, idea_id: int):
        if idea_id not in self.ideas:
            raise ValueError("Idea not found")
        top_feedback = self.get_top_feedback(idea_id)
        summary = ""
        for feedback in top_feedback[:5]:
            summary += f"{feedback.comment} (Upvotes: {feedback.upvotes}, Downvotes: {feedback.downvotes})\n"
        return summary

    def private_share(self, idea_id: int, access_control: dict):
        if idea_id not in self.ideas:
            raise ValueError("Idea not found")
        # Implement access control logic here
        return self.ideas[idea_id]

    def community_voting(self, idea_id: int):
        if idea_id not in self.ideas:
            raise ValueError("Idea not found")
        return self.ideas[idea_id].feedback
