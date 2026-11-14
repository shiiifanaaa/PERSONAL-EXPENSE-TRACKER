
# Personal Expense Tracker


expense_names = []
expense_amounts = []

while True:

    name = input("\nEnter expense name: ")
    amount = float(input("Enter expense amount: "))

    if amount <= 0:
        print("Invalid amount! Enter a positive amount.")
        continue

    expense_names.append(name)
    expense_amounts.append(amount)

    choice = input("Do you want to add another expense? (yes/no): ")

    if choice.lower() == "no":
        break

# Calculate total
total = 0

for amount in expense_amounts:
    total = total + amount

# Display expense report
print("\n===== EXPENSE REPORT =====")

if len(expense_names) == 0:
    print("You have not added any expenses")

else:
    for i in range(len(expense_names)):
        print(expense_names[i], ":", expense_amounts[i])

    print("--------------------------")
    print("Total Expenses:", len(expense_names))
    print("Total Amount: Rs.", total)

    # Highest expense
    highest = max(expense_amounts)
    print("Highest Expense: Rs.", highest)

    # Lowest expense
    lowest = min(expense_amounts)
    print("Lowest Expense: Rs.", lowest)

print("==========================")

