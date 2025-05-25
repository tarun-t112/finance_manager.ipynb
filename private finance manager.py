users = {
    "alice": "pass123",
    "bob": "bob@456"
}

user_expenses = {
    "alice": {},
    "bob": {}
}

# --- Login ---
def login():
    print("Login to Private Finance Manager")
    username = input("Username: ").strip().lower()
    password = getpass("Password: ")
    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
        return username
    else:
        print("Invalid credentials.")
        return None

# --- Add Expense ---
def add_expense(username):
    print("Add Expense:")
    while True:
        category = input("Enter category (or 'done' to finish): ").strip()
        if category.lower() == 'done':
            break
        try:
            amount = float(input(f"Amount spent on {category}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if category in user_expenses[username]:
            user_expenses[username][category] += amount
        else:
            user_expenses[username][category] = amount
    print("Expenses saved!")

# --- View Summary ---
def view_summary(username):
    if not user_expenses[username]:
        print("No expenses to show.")
        return

    print("\nExpense Summary:")
    total = sum(user_expenses[username].values())
    for cat, amt in user_expenses[username].items():
        print(f"{cat}: ₹{amt:.2f}")
    print(f"Total Expenses: ₹{total:.2f}")
    
    # Pie Chart
    plt.figure(figsize=(6,6))
    plt.pie(user_expenses[username].values(), labels=user_expenses[username].keys(), autopct='%1.1f%%', startangle=90)
    plt.title(f"{username.title()}'s Expense Breakdown")
    plt.axis('equal')
    plt.show()

# --- Main Program ---
def main():
    user = None
    while user is None:
        user = login()

    while True:
        print("\nOptions:")
        print("1. Add Expenses")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ").strip()

        if choice == '1':
            add_expense(user)
        elif choice == '2':
            view_summary(user)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
