# Derick Bailey
# October 21, 2026
# P4HW1
# This program collects scores, validates them, drops the lowest score,
# calculates the average, and displays the letter grade.

# Pseudocode:
# Ask how many scores the user wants to enter.
# Create an empty list to store scores.
# Use a loop to collect each score.
# Validate that each score is between 0 and 100.
# If invalid, display an error and ask for the score again.
# Add valid scores to the list.
# Find the lowest score and remove it from the list.
# Calculate the average of the modified list.
# Determine the letter grade.
# Display the results.

num_scores = int(input("How many scores do you want to enter? "))

scores = []

for i in range(num_scores):
    score = float(input(f"\nEnter score #{i + 1}: "))

    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i + 1} again: "))

    scores.append(score)

lowest_score = min(scores)
scores.remove(lowest_score)

if len(scores) > 0:
    average = sum(scores) / len(scores)
else:
    average = 0

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("\n")
print("--------------Results--------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("-----------------------------------")
