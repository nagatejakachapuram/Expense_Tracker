import sqlite3
import matplotlib.pyplot as plt
from export_csv import export_to_csv


# Database setup
def setup_database():
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE,
        category TEXT,
        amount FLOAT,
        description TEXT
    )
    """)
    conn.commit()
    conn.close()

# Add an expense
def add_expense(date, category, amount, description=""):
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO expenses (date, category, amount, description)
    VALUES (?, ?, ?, ?)
    """, (date, category, amount, description))
    conn.commit()
    conn.close()
    print("\nExpense added successfully!")

# View all expenses
def view_expenses():
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    print("\n--- All Expenses ---")
    print(f"{'ID':<5}{'Date':<12}{'Category':<15}{'Amount':<10}{'Description':<20}")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]:<5}{row[1]:<12}{row[2]:<15}{row[3]:<10}{row[4]:<20}")

# Analyze expenses by category
def analyze_expenses_by_category():
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """)
    rows = cursor.fetchall()
    conn.close()

    print("\n--- Expenses by Category ---")
    for row in rows:
        print(f"Category: {row[0]}, Total: {row[1]:.2f}")

# Visualize expenses
def visualize_expenses():
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """)
    rows = cursor.fetchall()
    conn.close()

    categories = [row[0] for row in rows]
    amounts = [row[1] for row in rows]

    if len(categories) == 0:
        print("\nNo expenses to visualize!")
        return

    plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
    plt.title("Expenses by Category")
    plt.show()

# Command-line interface
def main():
    setup_database()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses by Category")
        print("4. Visualize Expenses")
        print("5. Export to CSV")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description (optional): ")
            add_expense(date, category, amount, description)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            analyze_expenses_by_category()
        elif choice == "4":
            visualize_expenses()
        elif choice == "5":
            export_to_csv()
        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")
