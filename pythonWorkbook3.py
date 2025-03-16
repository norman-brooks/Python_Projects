# Practical Exercises page 23

# Create a program that calculates the absolute difference between two numbers


def absolute_difference(num1, num2):
    return abs(num1 - num2)
num1 = -20
num2 = 5
difference = absolute_difference(num1, num2)
print(f"The absolute difference between {num1} and {num2} is {difference}")
                                    
# Note the indentation above. It would not recognize num1 when it wasn't equal
# with the def of absolute_difference




# Write a program that finds the highest and lowest numbers in a list

def find_extremes(num_list):
    return max(num_list), min(num_list)
highest, lowest = find_extremes ([1, 42, 3, 7])
print(f"The highest number is: {highest}")
print(f"The lowest number is: {lowest}")

# Implement a function that takes a number & returns its square root

import math

def find_sqrt(num):
    if num < 0:
        return "Square root of negative numbers are not supported."
    return math.sqrt(num)
result = find_sqrt(16)
print(f"The square root of {16} is: {result}")

# Formatting Numbers-can be crucial especially during a presentation
# This provides several ways to format numbers for better readability and presentation

print(format(123.4567, '.2f'))

# Above shows to format the number to 2 decimal places

# You can format FLOATING POINT numbers as well the general syntax is
# {:.NF} where N is the number of decimal places.

print('{:.2f}'.format(123.456))

# Exercise: Format the number 12.34567 to show 3 decimal places

print('{:.3f}'.format(12.34567))

# Formatting numbers in scientific notation page 25
# When dealing with very large or very small numbers you may prefer to use scientific notation

print('{:.2e}'.format(1234567890))# Output "1.23e+09"

# Inserting commas

print('{:,}'.format(1234567890)) # Output "1,234,567,890"

# Formatting Number as Percentages you can use the % symbol

print('{:.1%}'.format(0.456))

# Output: "45.6%"

# Setting Alignment-You can also control the alignment of the formatted number

print('{:>10}'.format(123))




