import array

# === Step 1: Integers - Initial Expense Data and Basic Calculations ===
expenses = [120, 85, 240, 60, 150]
print("Initial Expenses:", expenses)

total_expense = sum(expenses)
average_expense = total_expense / len(expenses)
min_expense = min(expenses)
max_expense = max(expenses)

print(f"Total Expense: ${total_expense}")
print(f"Average Expense: ${average_expense:.2f}")
print(f"Minimum Expense: ${min_expense}")
print(f"Maximum Expense: ${max_expense}")

# === Step 2: Strings - Formatted Expense Report ===
report = f"""
===== Expense Report =====
Total Expenses: ${total_expense}
Average Expense: ${average_expense:.2f}
Highest Expense: ${max_expense}
Lowest Expense: ${min_expense}
==========================
"""
print(report)

# === Step 3: Booleans - Threshold Check with Compound Condition ===
threshold = 100
high_spender = average_expense > threshold
many_expenses = len(expenses) > 4

if high_spender and many_expenses:
    print("Status: Above Standard – High spender with many transactions.")
else:
    print("Status: Below Standard – Keep monitoring your spending.")

# === Step 4: Lists - Modify Expense List ===
# Add a new expense
new_expense = 95
expenses.append(new_expense)
print("\nAfter Adding New Expense:", expenses)

# Remove first expense below $80
for exp in expenses:
    if exp < 80:
        expenses.remove(exp)
        print(f"Removed Expense Below $80: {exp}")
        break

print("After Removal:", expenses)

# Sort the list
expenses.sort()
print("Sorted Expenses:", expenses)

# === Step 5: Arrays - Use array module for fixed-size subset ===
expense_array = array.array('i', expenses[:4])  # First 4 expenses
array_sum = sum(expense_array)
print("\nArray Subset (First 4 Expenses):", expense_array.tolist())
print("Array Sum:", array_sum)
print("List Total (for comparison):", sum(expenses))

# === Step 6: Dictionaries - Manage Detailed Expense Records ===
expense_records = [
    {'id': 1, 'name': 'Groceries', 'value': 120},
    {'id': 2, 'name': 'Transport', 'value': 85},
    {'id': 3, 'name': 'Dining', 'value': 240},
]

print("\nInitial Records:")
for rec in expense_records:
    print(rec)

# Update value of id=2
for record in expense_records:
    if record['id'] == 2:
        record['value'] = 95
        print("\nUpdated Record (id=2):", record)

# Delete record with id=1
expense_records = [rec for rec in expense_records if rec['id'] != 1]
print("\nAfter Deletion (id=1):")
for rec in expense_records:
    print(rec)

# Compute total of 'value' fields
total_recorded_expense = sum(rec['value'] for rec in expense_records)
print(f"\nTotal Value from Records: ${total_recorded_expense}")

# === End of Project ===
print("\n✅ Personal Expense Tracker Completed Successfully.")
