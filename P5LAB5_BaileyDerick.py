
# Derick Bailey
# 11/20/2026
# P5LAB
# This program simulates a self-checkout machine and calculates the change owed to a customer.

import random

# Pseudocode:
# Generate a random purchase total.
# Ask the customer how much cash they are paying.
# Calculate the change owed.
# Use a function to calculate the dollars and coins needed.
# Display the amount of each denomination.

def disperse_change(change):

    # Convert change into whole cents to avoid decimal issues
    change = round(change * 100)

    dollars = change // 100
    change = change % 100

    quarters = change // 25
    change = change % 25

    dimes = change // 10
    change = change % 10

    nickels = change // 5
    change = change % 5

    pennies = change

    print(f"\nChange due:")
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")


def main():

    # Generate a random purchase amount
    amount_owed = round(random.uniform(0.01, 100.00), 2)

    print(f"Your total is: ${amount_owed:.2f}")

    # Ask customer for payment
    cash = float(input("Enter the amount of cash you will put into the machine: $"))

    # Calculate change
    change = cash - amount_owed

    # Display change or remaining balance
    if change >= 0:
        print(f"Change owed: ${change:.2f}")
        disperse_change(change)
    else:
        print(f"Not enough money. You still owe: ${abs(change):.2f}")


# Call the main function
if __name__ == "__main__":
    main()
