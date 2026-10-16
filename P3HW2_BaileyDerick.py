# Your Name
# October 16, 2026
# P3HW2 - Employee Pay
# This program calculates regular pay, overtime pay, and gross pay.

# Pseudocode:
# 1. Get the employee's name, hours worked, and pay rate.
# 2. If hours worked are greater than 40, calculate overtime hours,
#    regular pay for 40 hours, and overtime pay at 1.5 times the rate.
# 3. Otherwise, calculate regular pay for all hours and set overtime to 0.
# 4. Calculate gross pay.
# 5. Display the employee's pay information in columns.

# Get employee information
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_pay = 40 * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    overtime_hours = 0
    regular_pay = hours_worked * pay_rate
    overtime_pay = 0

gross_pay = regular_pay + overtime_pay

# Display results in the format shown in the assignment
print("-----------------------------------------------")
print(f"Employee name:    {employee_name}")
print()
print(f"{'Hours Worked':<17}{'Pay Rate':<12}{'OverTime':<13}"
      f"{'OverTime Pay':<24}{'RegHour Pay':<24}{'Gross Pay'}")
print("-" * 105)
print(f"{hours_worked:<17.1f}{pay_rate:<12.1f}{overtime_hours:<13.1f}"
      f"{overtime_pay:<24.2f}${regular_pay:<23.2f}${gross_pay:.2f}")