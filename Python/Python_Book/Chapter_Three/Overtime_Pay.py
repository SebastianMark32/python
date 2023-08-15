# This program will calculate the employee's hourly rate and overtime

# User input for how many hours worked
days_worked = float(input("How hours did you work (this calcualtes per week)?:"))

# Days to hours conversion
hours = days_worked

# Pay rate per hour
pay_rate = float(input("Enter your current pay rate:"))

# Overtime rate
over_time_rate = pay_rate * 1.5 

# Calculating the current tax rate
tax = .1186

# Calculating overtime if the user is over 40 hours or under
if hours > 40:
    pre_overtime = 40 * pay_rate
    overtime = hours % 40
    overtime_pay = overtime * over_time_rate
    before_tax = pre_overtime + overtime_pay 
    tax = before_tax * tax
    total = before_tax - tax
    print("Overtime hours", overtime)
    print("Pre-overtime pay", pre_overtime)
    print("Overtime amount", format(overtime_pay, '.2f'))
    print("Before tax", format(before_tax, '.2f'))
    print("Your total pay for the week after tax:", format(total,'.2f'), "for", hours, "hours")
else:
    payment = hours * pay_rate
    print("Your weekly amount for", days_worked, "days worked and", hours, "hours is:", payment)