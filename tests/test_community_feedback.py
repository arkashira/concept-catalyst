from community_feedback import CommunityFeedbackLoop, Feedback, Idea

def test_add_idea():
    cfl = CommunityFeedbackLoop()
    cfl.add_idea(1, "Test idea")
    assert len(cfl.ideas) == 1
    assert cfl.ideas[1].description == "Test idea"

def test_add_feedback():
    cfl = CommunityFeedbackLoop()
    cfl.add_idea(1, "Test idea")
    cfl.add_feedback(1, "Test feedback")
    assert len(cfl.ideas[1].feedback) == 1
    assert cfl.ideas[1].feedback[0].comment == "Test feedback"

def test_upvote_feedback():
    cfl = CommunityFeedbackLoop()
    cfl.add_idea(1, "Test idea")
    cfl.add_feedback(1, "Test feedback")
    cfl.upvote_feedback(1, 1)
    assert cfl.ideas[1].feedback[0].upvotes == 1

def test_downvote_feedback():
    cfl = CommunityFeedbackLoop()
    cfl.add_idea(1, "Test idea")
    cfl.add_feedback(1, "Test feedback")
    cfl.downvote_feedback(1, 1)
    assert cfl.ideas[1].feedback[0].downvotes == 1

def test_get_top_feedback():
    cfl = CommunityFeedbackLoop()
    cfl.add_idea(1, "Test idea")
    cfl.add_feedback(1, "Test feedback 1")
    cfl.add_feedback(1, "Test feedback 2")
    cfl.upvote_feedback(1, 1)
    cfl.upvote_feedback(1, 1)
    cfl.downvote_feedback(1, 2)
    top_feedback = cfl.get_top_feedback(1)
    assert top_feedback[0].comment == "Test feedback 1"

def test_auto_generate_summary():
    cfl = CommunityFeedbackLoop()
    cfl.add_idea(1, "Test idea")
    cfl.add_feedback(1, "Test feedback 1")
    cfl.add_feedback(1, "Test feedback 2")
    cfl.upvote_feedback(1, 1)
    cfl.upvote_feedback(1, 1)
    cfl.downvote_feedback(1, 2)
    summary = cfl.auto_generate_summary(1)
    assert "Test feedback 1" in summary

def test_private_share():
    cfl = CommunityFeedbackLoop()
    cfl.add_idea(1, "Test idea")
    idea = cfl.private_share(1, {})
    assert idea.description == "Test idea"

def test_community_voting():
    cfl = CommunityFeedbackLoop()
    cfl.add_idea(1, "Test idea")
    cfl.add_feedback(1, "Test feedback 1")
    cfl.add_feedback(1, "Test feedback 2")
    feedback = cfl.community_voting(1)
    assert len(feedback) == 2
