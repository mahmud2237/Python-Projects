# Project: A program that calculates simple interest based on your user input.

# simple interest calculator
print('Welcome to the simple interest calculator!')

# Get user inputs
principal = float(input('Enter the principal amount: '))
rate = float(input('Enter the interest rate(in %): '))
time = float(input('Enter the time(in years): '))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Now display the result on the screen
print('The simple interest is: ', simple_interest)



