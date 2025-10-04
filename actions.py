from data import fileManagement

import csv
import random
import time
import os


class cardParse:
    """Parses/modifies csv through internal dict"""

    @staticmethod
    def load_cards(filename):
        """Converts csv to internal dict"""
        if not os.path.exists(filename):
            fileManagement.create_csv(filename)
        with open(filename, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
        
    @staticmethod
    def save_cards(filename, cards):
        """Place new values back into csv"""
        with open(filename, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Question", "Answer", "LeitnerBox"], quoting=csv.QUOTE_ALL)
            writer.writeheader()
            writer.writerows(cards)
    
    def choose_file():
        """Show user a menu of CSV files and let them choose one or create a new one."""
        folder = "cards"

        if not os.path.exists(folder):
            os.makedirs(folder)

        print("\n📂 Available Study Sets:\n")

        csv_files = [f for f in os.listdir(folder) if f.lower().endswith(".csv")]

        if not csv_files:
            print("No CSV files found in the 'cards/' folder.")
            print("You'll need to create a new one.\n")
            new_name = input("Enter a name for your new CSV file (without extension): ").strip()
            if not new_name:
                new_name = "new_cards"
            if not new_name.lower().endswith(".csv"):
                new_name += ".csv"
            return os.path.join(folder, new_name)
        
        for i, f in enumerate(csv_files, start=1):
            print(f"{i}. {f}")

        print(f"{len(csv_files) + 1}. ➕ Create a new study file")

        while True:
            choice = input("\nSelect a file by number: ").strip()

            if not choice.isdigit():
                print("Please enter a number.")
                continue

            choice = int(choice)

            if 1 <= choice <= len(csv_files):
                return os.path.join(folder, csv_files[choice - 1])

            if choice == len(csv_files) + 1:
                new_name = input("Enter a name for your new CSV file (without extension): ").strip()
                if not new_name:
                    new_name = "new_cards"
                if not new_name.lower().endswith(".csv"):
                    new_name += ".csv"
                return os.path.join(folder, new_name)

            print("Invalid option. Try again.")

    

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
                if elapsed <= 2:
                    card["LeitnerBox"] = "5"
                    print(f"✅ Correct! You took {elapsed:.2f}s. Card moved to Box {card['LeitnerBox']}")
                elif elapsed <= 5:
                    card["LeitnerBox"] = "4"
                    print(f"✅ Correct! You took {elapsed:.2f}s. Card moved to Box {card['LeitnerBox']}")
                elif elapsed <= 10:
                    card["LeitnerBox"] = "3"
                    print(f"✅ Correct! You took {elapsed:.2f}s. Card moved to Box {card['LeitnerBox']}")
                elif elapsed <= 15:
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
    file = cardParse.choose_file()
    cards = cardParse.load_cards(file)
    session_count = 0
    affirmations = [
        "🌟 Nice work! You're doing great!",
        "🔥 Keep going — you'll have this in no time!",
        "💪 You're smashing it! Stay sharp!"
    ]
    next_affirmation = random.randint(1, 3)
    since_affirmation = 0

    if len(cards) == 0:
        print("\nThis csv does not contain any cards, please refer to 'template.csv' for an example and information.")
        card_add = input("Would you like to add one card now (y/n)? ")
        while not card_add.lower() == "y" and not card_add.lower() == "n":
            card_add = input("Please enter 'y' or 'n': ")
        if card_add.lower() == "y":
            question = input("Please enter a question: ")
            answer = input("Please enter an answer: ")
            happy = input("\nAre you happy with these being your card's question and answer (y/n)? ")
            while not happy.lower() == "y" and not happy.lower() == "n":
                happy = input("Please enter 'y' or 'n': ")
            if happy.lower() == "n":
                question = input("\nPlease re-enter a question: ")
                answer = input("Please re-enter an answer: ")
            else:
                fileManagement.add_card(question, answer, file)

        return cards, session_count

    print(f"\nYou are studying '{file}'!")

    for card in studyTime.randomized_play(cards):
        session_count += 1
        since_affirmation += 1

        if since_affirmation >= next_affirmation:
            print("\n" + random.choice(affirmations) + "\n")
            since_affirmation = 0
            next_affirmation = random.randint(1, 3)

        cont = input("Continue? (y/n): ").lower()
        if cont.lower() != "y":
            print(f"\n📚 Session complete! You studied {session_count} cards.")
            #print(cards)
            break
    else:
        print(f"\n📚 Session complete! You studied all {session_count} cards.")

    cardParse.save_cards(file, cards)
    return cards, session_count


def tutorial():
    """Explain to user the nature of the program."""

    print("In this, you will first be asked to press 'enter' to begin learning your cards.")
    print("You will immediately be presented with a card, and are meant to recall mentally what the answer is.")
    print("Once you recall the answer, you press 'enter' and get presented with the card's new leitner value (explanation below).")
    print("")
    time.sleep(7)

    print("This app uses a system of card management called the leitner system. Put simply, the more you know a card, the less often you will revisit it.")
    print("A card being at level 5 means you know it very well and can recall it near immediately, good on you!")
    print("A card being at level 1 means you have newly added the card and/or can't recall it well, don't worry though, this very program shall remedy that.\n")
    time.sleep(7)

    print("Now go forth, and LEARN!!")
    cont = input("Would you like to proceed with your cards (y/n)? ")
    return cont