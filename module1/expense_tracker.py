import json
from datetime import date
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"

class Expense:
    def __init__(self,amount,category,note = "",when=None):
        self.amount = amount
        self.category = category
        self.note = note
        self.when = when or date.today().isoformat()

    def to_dict(self):
        return{
            "amount":self.amount,
            "category":self.category,
            "note":self.note,
            "when":self.when,
        }

    def __str__(self):
        return f"{self.when} | {self.category:<10} | {self.amount:>8.2f} | {self.note}"

class ExpenseTracker:
    def __init__(self, path = DATA_FILE):
        self.path = path
        self.expenses = []
        self.load()

    def load(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return
        except json.JSONDecodeError:
            print("Data File is damaged: starting empty.")
            return
        self.expenses = [Expense(**item) for item in data]

    def save(self):
        with open(self.path,"w",encoding="utf-8") as f:
            json.dump([e.to_dict() for e in self.expenses], f, indent=2)

    def add(self,amount,category,note=""):
        self.expenses.append(Expense(amount,category,note))
        self.save()

    def total(self):
        return sum(e.amount for e in self.expenses)

    def total_by_category(self):
        totals = {}
        for e in self.expenses:
            totals[e.category]= totals.get(e.category,0)+e.amount
        return totals

    def ask_amount(self):
        while True:
            text = input("Amount: ").strip()
            try:
                amount = float(text)
            except ValueError:
                print("Enter a whole number like 20.5")
                continue
            if amount <= 0:
                print("Amount should be positive.")
                continue
            return amount


def main():
        tracker = ExpenseTracker()
        while True:
           print("\n1. Add  2. List  3. Totals  4. Quit")
           choice = input("Choose: ").strip()
           if choice == "1":
               amount = tracker.ask_amount()
               category = input("Category: ").strip().lower() or "other"
               note = input("Note (optional): ").strip()
               tracker.add(amount, category, note)
               print("Saved.")
           elif choice == "2":
               if not tracker.expenses:
                   print("No expenses yet.")
               for e in tracker.expenses:
                   print(e)
           elif choice == "3":
               for cat, amt in sorted(tracker.total_by_category().items()):
                   print(f"{cat:<10} {amt:>8.2f}")
               print(f"{'TOTAL':<10} {tracker.total():>8.2f}")
           elif choice == "4":
               print("Goodbye!")
               break
           else:
               print("Invalid choice.")


if __name__ == "__main__":
    main()





        
        