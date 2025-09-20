import sys, os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(__file__))) 
from actions import studyTime

class dummyInput:
    """Simulate user input"""
    def __init__(self, responses):
        """responses: a list of strings returned sequentially for input() calls"""
        self.responses = responses

    def __call__(self, prompt=""):
        return self.responses.pop(0)

class dummyTime:
    """Simulate time.time() calls for testing timing logic"""
    def __init__(self, times):
        """times: list of sequential times to return"""
        self.times = times

    def time(self):
        """Return next time in list"""
        return self.times.pop(0)

def test_ask_card_leitner_timing(monkeypatch):
    """Test timing thresholds and wrong answer behavior"""
    
    # Test cases as tuples: (elapsed_time, expected_box, user_answer)
    test_cases = [
        (8,  "5", "y"),    # <=10s
        (15, "4", "y"),    # 11-30s
        (45, "3", "y"),    # 31-60s
        (90, "2", "y"),    # 61-120s
        (150,"1", "y"),    # >120s
        (50, "1", "n")     # wrong answer
    ]

    for elapsed, expected_box, user_answer in test_cases:
        card = {"Question": "Q1", "Answer": "A1", "LeitnerBox": "1"}
        
        monkeypatch.setattr("builtins.input", dummyInput(["", "", user_answer]))
        
        # Simulate time: start=0, end=elapsed
        times = [0, elapsed]
        monkeypatch.setattr("time.time", dummyTime(times).time)
        
        studyTime.ask_card(card)
        assert card["LeitnerBox"] == expected_box, f"Failed for elapsed={elapsed}s, answer={user_answer}"

def test_randomized_play_yields(monkeypatch):
    """Test randomized_play yields all cards in proper order and priority"""
    
    cards = [
        {"Question": "Q1", "Answer": "A1", "LeitnerBox": "1"},  # priority
        {"Question": "Q2", "Answer": "A2", "LeitnerBox": "2"},  # priority
        {"Question": "Q3", "Answer": "A3", "LeitnerBox": "4"},  # secondary
        {"Question": "Q4", "Answer": "A4", "LeitnerBox": "5"}   # secondary
    ]

    # Simulate user answering correctly very fast
    monkeypatch.setattr("builtins.input", dummyInput(["", "", "y"]*len(cards)))
    monkeypatch.setattr("time.time", lambda: 0)  # all fast

    seen_questions = []
    for card in studyTime.randomized_play(cards):
        seen_questions.append(card["Question"])

    # Ensure all cards were yielded
    assert set(seen_questions) == {"Q1","Q2","Q3","Q4"}
