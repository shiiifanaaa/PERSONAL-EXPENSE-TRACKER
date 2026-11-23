
# ==========================================
# PERSONAL EXPENSE TRACKER
# ==========================================

# Lists to store expenses
expense_names = []
expense_amounts = []
expense_categories = []


# Function to add expenses
def add_expense(names, amounts, categories):

    name = input("\nEnter expense name: ")
    amount = float(input("Enter expense amount: "))

    if amount <= 0:
        print("Invalid amount! Enter a positive amount.")
        return

    category = input("Enter expense category: ")

    # Store expense details
    names.append(name)
    amounts.append(amount)
    categories.append(category)

    print("Expense added successfully!")


# Function to calculate total expenditure
def calculate_total(amounts, index=0):

    if index == len(amounts):
        return 0

    return amounts[index] + calculate_total(amounts, index + 1)


# Function to display all expenses
def display_expenses(names, amounts, categories):

    if len(names) == 0:
        print("\nYou have not added any expenses.")
        return

    print("\n========== EXPENSE REPORT ==========")

    # Display individual expenses
    for i in range(len(names)):

        # Store expense details in a tuple
        expense = (names[i], amounts[i], categories[i])

        name, amount, category = expense

        print("\nExpense Name:", name)
        print("Amount: Rs.", amount)
        print("Category:", category)

    # Calculate total expenditure
    total = calculate_total(amounts)

    print("\n------------------------------------")
    print("Total Expenses:", len(names))
    print("Total Amount: Rs.", total)

    # Find highest and lowest expenses
    highest = max(amounts)
    lowest = min(amounts)

    print("Highest Expense: Rs.", highest)
    print("Lowest Expense: Rs.", lowest)

    print("====================================")


# Function to calculate category-wise expenditure
def category_expenses(names, amounts, categories):

    if len(names) == 0:
        print("\nNo expenses available.")
        return

    unique_categories = []

    # Identify different categories
    for category in categories:

        if category not in unique_categories:
            unique_categories.append(category)

    print("\n======= CATEGORY-WISE REPORT =======")

    # Calculate expenditure for each category
    for category in unique_categories:

        category_total = 0

        for i in range(len(categories)):

            if categories[i] == category:
                category_total += amounts[i]

        print(category, ": Rs.", category_total)


# Main program
while True:

    print("\n========== PERSONAL EXPENSE TRACKER ==========")

    print("1. Add Expense")
    print("2. Display Expense Report")
    print("3. Calculate Total Expenditure")
    print("4. Category-wise Expense Report")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        add_expense(expense_names, expense_amounts,
                    expense_categories)

        # Ask whether to add another expense
        while True:

            again = input("\nDo you want to add another expense? (yes/no): ")

            if again.lower() == "yes":

                add_expense(expense_names, expense_amounts,
                            expense_categories)

            elif again.lower() == "no":
                break

            else:
                print("Invalid choice! Enter yes or no.")

    elif choice == "2":

        display_expenses(expense_names, expense_amounts,
                         expense_categories)

    elif choice == "3":

        total = calculate_total(expense_amounts)

        print("\nTotal Expenditure: Rs.", total)

    elif choice == "4":

        category_expenses(expense_names, expense_amounts,
                          expense_categories)

    elif choice == "5":

        print("\nThank you for using Personal Expense Tracker!")
        break

    else:

        print("Invalid choice! Please try again.")

