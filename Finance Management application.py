import datetime

# The main data structure to store transactions
# Format: { 'type': str, 'amount': float, 'description': str, 'date': str }
transactions = []

def add_transaction(transaction_type):
    """Adds a new expense or income transaction."""
    print(f"\n--- Add {transaction_type.capitalize()} ---")
    while True:
        try:
            # Get the amount
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be positive. Please try again.")
                continue

            # Get the description
            description = input("Enter description (e.g., Groceries, Salary): ").strip()
            if not description:
                print("Description cannot be empty. Please try again.")
                continue

            # Get the date (default to today)
            date_input = input(f"Enter date (YYYY-MM-DD, press Enter for today: {datetime.date.today()}): ").strip()
            date_str = date_input if date_input else str(datetime.date.today())

            # Validate the date format
            try:
                datetime.datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue

            # Create and append the transaction
            new_transaction = {
                'type': transaction_type,
                'amount': amount,
                'description': description,
                'date': date_str
            }
            transactions.append(new_transaction)
            print(f"\n {transaction_type.capitalize()} of ${amount:.2f} added successfully.")
            break
        except ValueError:
            print("Invalid input for amount. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

def view_transactions():
    """Displays all recorded transactions."""
    if not transactions:
        print("\n--- No transactions recorded yet. ---")
        return

    print("\n--- Transaction History ---")
    print(f"{'Date':<10} {'Type':<8} {'Amount':<10} {'Description':<30}")
    print("-" * 60)

    # Sort transactions by date for better readability
    sorted_transactions = sorted(transactions, key=lambda x: x['date'], reverse=True)

    for i, t in enumerate(sorted_transactions):
        # Determine the sign for amount based on type
        sign = "+" if t['type'] == 'income' else "-"
        amount_str = f"{sign}{t['amount']:.2f}"

        print(f"{t['date']:<10} {t['type'].capitalize():<8} {amount_str:<10} {t['description']:<30}")
    print("-" * 60)

def calculate_balance():
    """Calculates the current account balance."""
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    current_balance = total_income - total_expense

    print("\n--- Financial Summary ---")
    print(f" Total Income: ${total_income:.2f}")
    print(f" Total Expenses: ${total_expense:.2f}")
    print(f" **Current Balance: ${current_balance:.2f}**")
    print("-" * 30)
    return current_balance

def main_menu():
    """The main application loop."""
    print("--- Personal Finance Manager ---")
    while True:
        print("\nSelect an option:")
        print("1. Add Income ➕")
        print("2. Add Expense ➖")
        print("3. View All Transactions ")
        print("4. Calculate Balance ")
        print("5. Exit ")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_transaction('income')
        elif choice == '2':
            add_transaction('expense')
        elif choice == '3':
            view_transactions()
        elif choice == '4':
            calculate_balance()
        elif choice == '5':
            print("\n Thank you for using the Finance Manager. Goodbye!")
            break
        else:
            print("\n Invalid choice. Please enter a number between 1 and 5.")

# Run the application
if __name__ == "__main__":
    main_menu()