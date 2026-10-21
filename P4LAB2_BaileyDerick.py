# Derick Bailey
# October 21, 2026
# P4LAB2 - Multiplication Table
# This program displays a multiplication table for a non-negative
# integer and allows the user to run the program again.

# Pseudocode:
# 1. Display a welcome message.
# 2. Set the program to repeat using a while loop.
# 3. Ask the user to enter an integer.
# 4. If the integer is greater than or equal to zero:
#       a. Display the multiplication table heading.
#       b. Use a for loop to count from 1 through 12.
#       c. Multiply the entered number by each count.
#       d. Display each multiplication equation and result.
# 5. Otherwise:
#       a. Display a message that negative values are not accepted.
# 6. Ask the user if they want to run the program again.
# 7. If the answer is "yes", repeat the program.
# 8. If the answer is "no", end the program.
# 9. Display a goodbye message when the program ends.

print("Welcome to the Multiplication Table Program!")

run_again = "yes"

while run_again == "yes":
    number = int(input("\nEnter an integer: "))

    if number >= 0:
        print(f"\nMultiplication table for {number}:")

        for multiplier in range(1, 13):
            result = number * multiplier
            print(f"{number} x {multiplier} = {result}")

    else:
        print("Negative values are not accepted.")

    run_again = input(
        "\nWould you like to run the program again? (yes/no): "
    ).lower()

print("Thank you for using the program. Goodbye!")