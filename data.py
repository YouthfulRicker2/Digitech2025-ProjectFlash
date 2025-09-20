import csv
import os

class fileManagement():
    """Handles file management relating to the csv"""

    @staticmethod
    def create_csv(CSV_FILE):
        """Create csv if doesn't exist"""

        print(f"⚠️ No file found: {CSV_FILE}. Creating new one...")
        with open(CSV_FILE, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Question", "Answer", "LeitnerBox"])
            writer.writeheader()
        return []
    
    @staticmethod
    def add_card(question, answer, CSV_FILE):
        """Add new flashcard"""

        if not os.path.exists(CSV_FILE):
            fileManagement.create_csv(CSV_FILE)

        new_card = {"Question": question, "Answer": answer, "LeitnerBox": "1"}

        with open(CSV_FILE, "a", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Question", "Answer", "LeitnerBox"])
            writer.writerow(new_card)

        print(f"✅ Added new card: '{question}'")

    @staticmethod
    def remove_card(question, CSV_FILE):
        """Remove a flashcard"""

        if not os.path.exists(CSV_FILE):
            print("⚠️ No CSV file found to edit.")
            return

        with open(CSV_FILE, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            cards = list(reader)

        original_count = len(cards)
        cards = [c for c in cards if c["Question"].strip().lower() != question.strip().lower()]

        if len(cards) == original_count:
            print(f"⚠️ No card found with question: '{question}'")
            return

        with open(CSV_FILE, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Question", "Answer", "LeitnerBox"])
            writer.writeheader()
            writer.writerows(cards)

        print(f"🗑️ Removed card: '{question}'")