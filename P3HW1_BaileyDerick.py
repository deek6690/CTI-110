# Derick Bailey
# October 16, 2026
# P3HW1 - Debugging
# This program collects six grades, calculates statistics,
# and displays the letter grade based on the average.

# Pseudocode:
# 1. Create an empty list to store grades.
# 2. Ask the user to enter six grades.
# 3. Add each grade to the list.
# 4. Find the lowest and highest grades.
# 5. Calculate the sum and average of the grades.
# 6. Determine the letter grade using the average.
# 7. Display the grade statistics and letter grade.

# Create an empty list for the grades
grades = []

# Get six grades from the user
for i in range(1, 7):
    grade = float(input(f"Enter grade #{i}: "))
    grades.append(grade)

# Calculate grade statistics
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# Determine the letter grade
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the results
print()
print("-" * 12, "Results", "-" * 12)
print(f"{'Lowest Grade:':<20}{lowest:.1f}")
print(f"{'Highest Grade:':<20}{highest:.1f}")
print(f"{'Sum of Grades:':<20}{total:.1f}")
print(f"{'Average:':<20}{average:.2f}")
print(f"{'Letter Grade:':<20}{letter_grade}")
print("-" * 31)