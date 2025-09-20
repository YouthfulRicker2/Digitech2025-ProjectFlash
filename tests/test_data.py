import sys, os
import csv
import tempfile
sys.path.append(os.path.dirname(os.path.dirname(__file__))) 
from data import fileManagement

def test_add_and_remove_card():
    """Tests the data program by creating a program, adding a card, checking the card, removing the card, and checking the lack of that card... Wahoo."""

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        name = tmp.name
    fileManagement.create_csv(name)

    fileManagement.add_card("Q1", "A1", name)

    with open(name, newline='', encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        assert len(reader) == 1
        assert reader[0]["Question"] == "Q1"

    fileManagement.remove_card("Q1", name)

    with open(name, newline='', encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        assert len(reader) == 0

    os.remove(name)
