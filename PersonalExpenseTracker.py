import csv
from datetime import datetime
import os

class PersonalExpenseTracker:
    def __init__(self, filename='expenses.csv'):
        self.expenses = []
        self.monthly_budget = 0
        self.filename = filename
        self.load_expenses()

    def add_expense(self):
        try:
            while True:
                date_str = input("Enter expense date (DD-MM-YYYY): ")
                try:
                    datetime.strptime(date_str, '%d-%m-%Y')
                    break
                except ValueError:
                    print("Invalid date format. Please use DD-MM-YYYY.")

            category = input("Enter expense category (e.g., Food, Travel): ").strip()
            
            while True:
                try:
                    amount = float(input("Enter expense amount: "))
                    break
                except ValueError:
                    print("Please enter a valid number.")

            description = input("Enter expense description: ").strip()

            expense = {
                'date': date_str,
                'category': category,
                'amount': amount,
                'description': description
            }

            self.expenses.append(expense)
            print("Expense added successfully!")
        except Exception as e:
            print(f"Error adding expense: {e}")

    def view_expenses(self):
        # Display all stored expenses
        if not self.expenses:
            print("No expenses recorded.")
            return

        print("\n--- Expense List ---")
        for idx, expense in enumerate(self.expenses, 1):
            print(f"{idx}. Date: {expense['date']}, "
                  f"Category: {expense['category']}, "
                  f"Amount: ${expense['amount']:.2f}, "
                  f"Description: {expense['description']}")

    def set_budget(self):
       # Set monthly budget
        while True:
            try:
                self.monthly_budget = float(input("Enter monthly budget amount: $"))
                if self.monthly_budget <= 0:
                    print("Budget must be a positive number.")
                    continue
                print(f"Monthly budget set to ${self.monthly_budget:.2f}")
                break
            except ValueError:
                print("Please enter a valid number.")

    def track_budget(self):
        # Calculate and display budget status
        if self.monthly_budget == 0:
            print("No budget set. Please set a budget first.")
            return

        total_expenses = sum(expense['amount'] for expense in self.expenses)
        remaining_balance = self.monthly_budget - total_expenses

        print(f"\nMonthly Budget: ${self.monthly_budget:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        
        if total_expenses > self.monthly_budget:
            print("❌ You have exceeded your budget!")
            print(f"Overspent by: ${abs(remaining_balance):.2f}")
        else:
            print(f"✅ You have ${remaining_balance:.2f} left for the month")

    def save_expenses(self):
        # Save expenses to a CSV file
        try:
            with open(self.filename, 'w', newline='') as csvfile:
                fieldnames = ['date', 'category', 'amount', 'description']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                csvfile.write(f"Monthly Budget,{self.monthly_budget}\n")
                writer.writeheader()
                writer.writerows(self.expenses)
            print(f"Expenses saved to {self.filename}")
        except Exception as e:
            print(f"Error saving expenses: {e}")

    def load_expenses(self):
        # Load expenses from CSV file
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, 'r') as csvfile:
                budget_line = csvfile.readline().strip().split(',')
                if len(budget_line) == 2:
                    try:
                        self.monthly_budget = float(budget_line[1])
                    except ValueError:
                        pass

                reader = csv.DictReader(csvfile)
                self.expenses = []
                for row in reader:
                    row['amount'] = float(row['amount'])
                    self.expenses.append(row)
            
            print(f"Loaded {len(self.expenses)} expenses from {self.filename}")
        except Exception as e:
            print(f"Error loading expenses: {e}")

    def run(self):
        # Main menu and program loop
        while True:
            print("\n--- Personal Expense Tracker ---")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. set Budget")
            print("4. Track Budget")
            print("5. Save Expenses")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.set_budget()
            elif choice == '4':
                self.track_budget()
            elif choice == '5':
                self.save_expenses()
            elif choice == '6':
                self.save_expenses()
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

def main():
    tracker = PersonalExpenseTracker()
    tracker.run()

if __name__ == "__main__":
    main()