# Personal-Expense-Tracker

Overview 
The Personal Expense Tracker is a Python-based application designed to help users manage their expenses and track their monthly budget. It allows users to add, view, and save expenses, set a monthly budget, and track their spending against the budget. The application also saves data to a CSV file to ensure persistence across sessions.

Features 
1. Add Expense: 
          Record an expense with details like date, category, amount, and description. 
          Validates user input for date and amount. 
2. View Expenses: 
          Display a list of all recorded expenses in a structured format. 
3. Set Budget: 
          Define a monthly budget for tracking expenses. 
          Ensures the budget value is positive. 
4. Track Budget: 
          Calculate total expenses and remaining balance for the month. 
          Alerts the user if they have exceeded their budget. 
5. Save Expenses: 
          Save all recorded expenses and the monthly budget to a CSV file. 
6. Load Expenses: 
          Load previously saved expenses and budget data from a CSV file. 
7. Menu-Based Navigation: 
          Provides a user-friendly interface with options to perform all functionalities.

How to Run the Application 
1. Requirements: 
          Python 3.x 
          No external libraries are required as the code uses Python's built-in modules (csv, datetime, os). 
2. Steps to Execute: 
          Save the script as expense_tracker.py. 
          Open a terminal or command prompt. 
          Navigate to the directory containing the script. 
          Run the script using the command: 
                               python expense_tracker.py 
3. Interacting with the Application: 
         Follow the on-screen instructions to navigate through the menu. 
         Enter appropriate inputs as prompted.
   
CSV File Details 
         The application saves and loads data from a CSV file named expenses.csv by default. 
         File Structure: 
               The first line contains the monthly budget in the format: Monthly Budget,<budget_value> 
               Subsequent rows contain expense details with the following columns: 
                                 date (DD-MM-YYYY) 
                                 category (e.g., Food, Travel) 
                                 amount (numeric value) 
                                 description (short text) 
