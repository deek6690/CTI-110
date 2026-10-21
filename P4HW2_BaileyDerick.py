# Derick Bailey
# October 21, 2026
# P4HW2 - Salary Calculator
# This program calculates employee pay for multiple employees
# and displays total overtime, regular pay, and gross pay.

# Pseudocode:
# Initialize total overtime, regular pay, gross pay, and employee count.
# Ask for an employee's name.
# While the name is not exactly "Done":
#     Ask how many hours the employee worked.
#     Ask for the employee's pay rate.
#     If hours worked are greater than 40:
#         Calculate overtime hours.
#         Calculate regular pay for 40 hours.
#         Calculate overtime pay at 1.5 times the pay rate.
#     Otherwise:
#         Set overtime hours and overtime pay to 0.
#         Calculate regular pay for all hours worked.
#     Calculate gross pay.
#     Display the employee name and pay information.
#     Add the employee's pay to the running totals.
#     Increase the employee count.
#     Ask for the next employee's name.
# Display the final totals and employee count.

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

employee_name = input("Enter employee's name or \"Done\" to terminate: ")

while employee_name != "Done":

    hours_worked = float(input("How many hours did " + employee_name + " work? "))
    pay_rate = float(input("What is " + employee_name + "'s pay rate? "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_pay = 40 * pay_rate
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    else:
        overtime_hours = 0
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0

    gross_pay = regular_pay + overtime_pay

    print()
    print("Employee name:   ", employee_name)
    print()
    print(f"{'Hours Worked':<15}{'Pay Rate':<13}{'OverTime':<13}"
          f"{'OverTime Pay':<23}{'RegHour Pay':<23}{'Gross Pay'}")
    print("-" * 105)
    print(f"{hours_worked:<15.1f}{pay_rate:<13.2f}{overtime_hours:<13.1f}"
          f"{overtime_pay:<23.2f}${regular_pay:<22.2f}${gross_pay:.2f}")
    print()

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    employee_name = input("Enter employee's name or \"Done\" to terminate: ")

print()
print("Total number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
