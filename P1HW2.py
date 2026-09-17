# Derick Bailey
# 9/17/2026
# P1HW2
# This program calculates and displays travel expenses.

# Pseudocode:
# Ask the user to enter their budget.
# Ask the user to enter their travel destination.
# Ask the user how much they will spend on gas.
# Ask the user how much they will spend on accommodation/hotel.
# Ask the user how much they will spend on food.
# Add all three expenses together.
# Subtract the total expenses from the initial budget.
# Display the travel expenses and remaining balance.

print("This program calculates and displays travel expenses")
print()

# Get user's budget
budget = float(input("Enter Budget: "))
print()

# Get travel destination
destination = input("Enter your travel destination: ")
print()

# Get travel expenses
gas = float(input("How much do you think you will spend on gas? "))
print()

accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()

food = float(input("Last, how much do you need for food? "))
print()

# Calculate total expenses
total_expenses = gas + accommodation + food

# Calculate remaining balance
remaining_balance = budget - total_expenses

# Display travel expenses
print("-------------Travel Expenses-------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget:g}")
print()
print(f"Fuel: {gas:g}")
print(f"Accomodation: {accommodation:g}")
print(f"Food: {food:g}")
print()
print(f"Remaining Balance: {remaining_balance:g}")