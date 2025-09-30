import sys, os
import pytest # type: ignore
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
        (1,  "5", "y"),   # <=2s
        (4, "4", "y"),    # 3-5s
        (7, "3", "y"),    # 6-10s
        (12, "2", "y"),   # 11-15s
        (20,"1", "y"),    # >15s
        (10, "1", "n")    # wrong answer
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

def test_session_count(monkeypatch):
    """Test main() counts correct number of studied cards."""

    fake_cards = [
        {"Question": "Q1", "Answer": "A1", "LeitnerBox": "1"},
        {"Question": "Q2", "Answer": "A2", "LeitnerBox": "1"},
        {"Question": "Q3", "Answer": "A3", "LeitnerBox": "1"},
    ]

    monkeypatch.setattr("actions.cardParse.load_cards", lambda filename: fake_cards)
    monkeypatch.setattr("actions.cardParse.save_cards", lambda a, b: None)
    monkeypatch.setattr("actions.studyTime.ask_card", lambda card: None)

    inputs = dummyInput(["y", "y", "n"])
    monkeypatch.setattr("builtins.input", inputs)

    from actions import main
    result, card_count = main()
    assert result is fake_cards
    assert card_count is 3


