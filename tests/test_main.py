import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from actions import main, cardParse
from test_actions import DummyInput, DummyTime
import random

class dummyInput:
    """Simulate user input for testing program flow (safe default)"""
    def __init__(self, responses):
        self.responses = list(responses)

    def __call__(self, prompt=""):
        if self.responses:
            return self.responses.pop(0)
        # default: stop the session gracefully
        return "n"

class dummyTime:
    """Simulate time.time() sequence"""
    def __init__(self, times):
        self.times = list(times)
    def time(self):
        return self.times.pop(0)

def test_actions_main_runs(monkeypatch):
    """Test actions.main() runs correctly and updates Leitner boxes"""

    test_cards = [
        {"Question": "Q1", "Answer": "A1", "LeitnerBox": "1"},
        {"Question": "Q2", "Answer": "A2", "LeitnerBox": "2"},
    ]

    monkeypatch.setattr(cardParse, "load_cards", lambda filename: test_cards)
    monkeypatch.setattr(cardParse, "save_cards", lambda filename, cards: None)
    monkeypatch.setattr(random, "shuffle", lambda x: None)

    user_inputs = [
        "", "", "y",  # card 1: show, think, correct
        "y",          # continue after card 1
        "", "", "y",  # card 2: show, think, correct
        "n"           # continue after card 2 -> stop
    ]
    monkeypatch.setattr("builtins.input", dummyInput(user_inputs))

    times = [0, 8, 0, 35]  
    monkeypatch.setattr("time.time", dummyTime(times).time)

    # Run program
    main()

    # assert test_cards objects updated
    assert test_cards[0]["LeitnerBox"] == "5"  # 8s -> Box 5
    assert test_cards[1]["LeitnerBox"] == "3"  # 35s -> Box 3
