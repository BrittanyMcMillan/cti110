# P1HW1

# 4/4/2023

# CTI-110 P1HW1 - Travel Expense

# Brittany McMillan

# the information being collected for the trip
print('This program calculates and displays travel expenses')
print()
num1 = int(input('Enter Budget: '))
print()
num2 = input('Enter your travel destination: ')
print()
num3 = int(input('How much do you think you will spend on gas? '))
print()
num4 = int(input('Approximately, how much will you need for accomodation/hotel? '))
print()
num5 = int(input('Last, how much do you need for food? '))
print()
# convert text into number
num1 = int(num1)
num2 = (num2)
num3 = int(num3)
num4 = int(num4)
num5 =int(num5)

# Program math for the cost
expense = num3 + num4 + num5
remainder = num1 - expense
#Program Display of the progam
print('--------------Travel Expenses-------------')
print('Location: ', num2)
print('Initial Budget: ', num1)
print()
print('Fuel: ', num3 )
print('Accommodation: ', num4)
print('Food: ', num5)
print()
print('Remaining Balance: ', remainder)
