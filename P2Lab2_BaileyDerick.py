# Derick Bailey
# 10/1/2026
# P2LAB2 - Automobile MPG
# This program uses a dictionary to store automobile MPG values,
# asks the user to select a vehicle and enter miles driven,
# then calculates and displays the gallons of gas needed.

# Pseudocode:
# Create a dictionary containing vehicles and their MPG.
# Get all dictionary keys and display them.
# Ask the user to enter a vehicle.
# Display the MPG for the selected vehicle.
# Ask the user how many miles they will drive.
# Calculate gallons needed by dividing miles by MPG.
# Display gallons needed rounded to two decimal places.

cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = cars.keys()
print(keys)

vehicle = input("Enter a vehicle to see its MPG: ")
print(f"The {vehicle} gets {cars[vehicle]} MPG.")

miles = float(input("Enter the number of miles you will drive: "))

gallons = miles / cars[vehicle]

print(f"To drive {miles:.1f} miles, you will need {gallons:.2f} gallons of gas.")