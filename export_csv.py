import sqlite3
import csv

def export_to_csv():
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Date", "Category", "Amount", "Description"])  # Header
        writer.writerows(rows)

    conn.close()
    print("Data exported to expenses.csv")
