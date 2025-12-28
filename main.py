import csv
import os

filename = "expenses.csv"

# Check if file exists, if not create with header
if not os.path.exists(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Description", "Amount"])

# Function to add expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Transport, Bills, Entertainment, Other): ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount! Must be a number.")
        return

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    
    print("Expense added successfully!\n")

# Function to show all expenses
def show_expenses():
    print("\n------ All Expenses ------")
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            print(f"Date: {row[0]}, Category: {row[1]}, Description: {row[2]}, Amount: {row[3]}")
    print("--------------------------\n")

# Function to calculate total expenses
def total_expenses():
    total = 0
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[3])
    print(f"Total Expenses: Rs. {total}\n")

# Function to delete an expense by description
def delete_expense():
    desc = input("Enter the description of the expense to delete: ")
    with open(filename, 'r') as file:
        rows = list(csv.reader(file))

    new_rows = [row for row in rows if row[2] != desc or row[0] == "Date"]  # Keep header
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_rows)
    
    print("Expense deleted successfully!\n")

# Main menu
def menu():
    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Delete Expense")
        print("4. Show Total Expenses")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            total_expenses()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run the program
menu()
