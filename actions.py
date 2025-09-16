import csv
import random
import time

CSV_FILE = "cards.csv"

class cardParse:
    """Parses/modifies csv through internal dict"""

    @staticmethod
    def load_cards(filename):
        """Converts csv to internal dict"""
        with open(filename, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
        
    @staticmethod
    def save_cards(filename, cards):
        """Place new values back into csv"""
        with open(filename, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Question", "Answer", "LeitnerBox"])
            writer.writeheader()
            writer.writerows(cards)
    
class studyTime:
    """Run the player's study session"""

    @staticmethod
    def ask_card(card):
        """Ask the user a question and update LeitnerBox (flowchart style)."""

        correct = ""
        input("\nPress Enter to see the card...")
        print(f"\nQ: {card['Question']}")

        start_time = time.time()
        input("Press Enter once you've thought of your answer...")
        elapsed = time.time() - start_time

        print(f"\nA: {card['Answer']}")

        while correct.lower() not in ["y","n"]:
            correct = input("Did you get it right? (y/n): ").strip().lower()
            if correct.lower() == "y":
                if elapsed <= 10:
                    card["LeitnerBox"] = "5"
                    print(f"✅ Correct! You took {elapsed:.2f}s. Card moved to Box {card['LeitnerBox']}")
                elif elapsed <= 30:
                    card["LeitnerBox"] = "4"
                    print(f"✅ Correct! You took {elapsed:.2f}s. Card moved to Box {card['LeitnerBox']}")
                elif elapsed <= 60:
                    card["LeitnerBox"] = "3"
                    print(f"✅ Correct! You took {elapsed:.2f}s. Card moved to Box {card['LeitnerBox']}")
                elif elapsed <= 120:
                    card["LeitnerBox"] = "2"
                    print(f"✅ Correct! You took {elapsed:.2f}s. Card moved to Box {card['LeitnerBox']}")
                else:
                    card["LeitnerBox"] = "1"
                    print(f"✅ Correct! You took {elapsed:.2f}s though, card moved to Box {card['LeitnerBox']}")      
            elif correct.lower() == "n":
                card["LeitnerBox"] = "1"
                print("❌ Wrong. Reset to Box 1.")
            else:
                print("Please enter 'y' or 'n' appropriate to your answer.\n")

    @staticmethod
    def randomized_play(cards):
        """Randomize csv by studyvalue & play"""

        priority = [c for c in cards if int(c["LeitnerBox"]) <= 3]
        secondary = [c for c in cards if int(c["LeitnerBox"]) > 3]

        random.shuffle(priority)
        random.shuffle(secondary)

        study_queue = priority + secondary

        while study_queue:
            card = study_queue.pop(0)  
            studyTime.ask_card(card)  
            yield card  


def main():
    """Runs the program"""
    cards = cardParse.load_cards(CSV_FILE)

    for card in studyTime.randomized_play(cards):
        cardParse.save_cards(CSV_FILE, cards)
        print("Card progress saved.\n")

        cont = input("Continue? (y/n): ").lower()
        if cont.lower() != "y":
            print("Baiii!!")
            break