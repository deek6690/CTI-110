# P3LAB - Money Counting Program
# Name: Firstname Lastname
# Date: 10/01/2026
# Course: CTI-110
# Assignment: P3LAB
#
# Pseudocode:
# Ask the user to enter an amount of money.
# Convert the money amount to an integer number of cents.
# Find the number of dollars using floor division.
# Subtract the dollars from the total cents.
# Find the number of quarters using floor division.
# Subtract the quarters from the remaining cents.
# Find the number of dimes using floor division.
# Subtract the dimes from the remaining cents.
# Find the number of nickels using floor division.
# Subtract the nickels from the remaining cents.
# The remaining cents are pennies.
# Display only denominations that have a value greater than zero.
# Use singular or plural wording as appropriate.

amount = float(input("Enter the amount of money as a float: "))

# Convert amount to cents
cents = int(amount * 100)

# Find dollars
dollars = cents // 100
cents = cents - (dollars * 100)

# Find quarters
quarters = cents // 25
cents = cents - (quarters * 25)

# Find dimes
dimes = cents // 10
cents = cents - (dimes * 10)

# Find nickels
nickels = cents // 5
cents = cents - (nickels * 5)

# Remaining cents are pennies
pennies = cents

# Display dollars
if dollars == 1:
    print("1 dollar")
elif dollars > 1:
    print(f"{dollars} dollars")

# Display quarters
if quarters == 1:
    print("1 quarter")
elif quarters > 1:
    print(f"{quarters} quarters")

# Display dimes
if dimes == 1:
    print("1 dime")
elif dimes > 1:
    print(f"{dimes} dimes")

# Display nickels
if nickels == 1:
    print("1 nickel")
elif nickels > 1:
    print(f"{nickels} nickels")

# Display pennies
if pennies == 1:
    print("1 penny")
elif pennies > 1:
    print(f"{pennies} pennies")