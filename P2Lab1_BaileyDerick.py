# Derick Bailey
# 10/01/2026
# P2LAB1 - Circle Calculations
# This program calculates the diameter, circumference,
# and area of a circle using a radius entered by the user.

# Pseudocode:
# Get the radius from the user as a float.
# Calculate the diameter using 2 * radius.
# Calculate the circumference using 2 * pi * radius.
# Calculate the area using pi * radius squared.
# Display the diameter with 1 decimal place.
# Display the circumference with 2 decimal places.
# Display the area with 3 decimal places.

import math

radius = float(input("Enter the radius of the circle: "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")