# Your Name
# 10/01/2026
# P2HW1 - Travel Expenses
# This program calculates the remaining travel budget after
# subtracting travel expenses from the user's budget.

# Pseudocode:
# Get the user's budget.
# Get the destination.
# Get the amount spent on gas.
# Get the amount spent on accommodation.
# Get the amount spent on food.
# Calculate the total expenses.
# Calculate the remaining budget.
# Display the travel information in aligned columns.
# Display all money amounts with a dollar sign and two decimals.

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("How much do you need for food? "))

total_expenses = gas + accommodation + food
remaining = budget - total_expenses

print()
print("------------Travel Expenses------------")
print(f"{'Location:':<25}{destination}")
print(f"{'Initial Budget:':<25}${budget:,.2f}")
print(f"{'Fuel:':<25}${gas:,.2f}")
print(f"{'Accommodation:':<25}${accommodation:,.2f}")
print(f"{'Food:':<25}${food:,.2f}")
print(f"{'Remaining Balance:':<25}${remaining:,.2f}")