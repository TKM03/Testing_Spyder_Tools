import json
import os
from datetime import datetime
import matplotlib.pyplot as plt

# File to store expenses
DATA_FILE = "expenses.json"

# Load expenses from file
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []  # Return empty list if no file exists

# Save expenses to file
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    try:
        amount = float(input("Enter amount spent: "))
        category = input("Enter category (e.g., Food, Transport): ").capitalize()
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        else:
            datetime.strptime(date, "%Y-%m-%d")  # Validate date format
        
        expense = {"amount": amount, "category": category, "date": date}
        expenses.append(expense)
        print("Expense added successfully!")
    except ValueError as e:
        print(f"Invalid input: {e}")

# View total expenses by category
def analyze_expenses(expenses):
    if not expenses:
        print("No expenses to analyze.")
        return
    
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]
    
    print("\nTotal Expenses by Category:")
    for category, total in totals.items():
        print(f"{category}: ${total:.2f}")
    return totals

# Plot expenses
def plot_expenses(totals):
    categories = list(totals.keys())
    amounts = list(totals.values())
    
    plt.bar(categories, amounts, color='skyblue')
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main program loop
def main():
    expenses = load_expenses()
    
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Analysis")
        print("3. Plot Expenses")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            totals = analyze_expenses(expenses)
        elif choice == "3":
            totals = analyze_expenses(expenses)
            if totals:
                plot_expenses(totals)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()