# Define constants for tax rate and hourly rate
TAX_RATE = 0.2  # 20% tax rate
HOURLY_RATE = 15  # $15 per hour

# Function to calculate gross pay
def calculate_gross_pay(hours_worked):
    return hours_worked * HOURLY_RATE

# Function to calculate net pay after taxes
def calculate_net_pay(gross_pay):
    taxes = gross_pay * TAX_RATE
    net_pay = gross_pay - taxes
    return net_pay

# Main program
print("Welcome to the Payroll System")
name = input("Enter employee's name: ")
hours_worked = float(input("Enter the number of hours worked: "))
employee_id = input("Enter employee ID: ")

gross_pay = calculate_gross_pay(hours_worked)
net_pay = calculate_net_pay(gross_pay)

# Display the payroll information
print("\nPayroll Information:")
print(f"Employee Name: {name}")
print(f"Employee ID: {employee_id}")
print(f"Gross Pay: ₱{gross_pay:.2f}")
print(f"Net Pay (after taxes): ₱{net_pay:.2f}")
