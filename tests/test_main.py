import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from actions import main, cardParse
from test_actions import dummyInput, dummyTime
import random

def test_actions_main_runs(monkeypatch):
    """Test actions.main() runs correctly and updates Leitner boxes"""

    test_cards = [
        {"Question": "Q1", "Answer": "A1", "LeitnerBox": "1"},
        {"Question": "Q2", "Answer": "A2", "LeitnerBox": "2"},
    ]

    monkeypatch.setattr(cardParse, "choose_file", lambda: "dummy.csv")
    monkeypatch.setattr(cardParse, "load_cards", lambda filename: test_cards)
    monkeypatch.setattr(cardParse, "save_cards", lambda filename, cards: None)
    monkeypatch.setattr(random, "shuffle", lambda x: None)

    user_inputs = [
        "", "", "y",  # card 1
        "y",          # continue
        "", "", "y",  # card 2
        "n"           # stop
    ]
    monkeypatch.setattr("builtins.input", dummyInput(user_inputs))
    monkeypatch.setattr("time.time", dummyTime([0, 1, 0, 8]).time)

    main()

    # Assert Leitner boxes updated correctly
    assert test_cards[0]["LeitnerBox"] == "5"  # 1s -> Box 5
    assert test_cards[1]["LeitnerBox"] == "3"  # 8s -> Box 3
