def calculate_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

def print_circle_area(radius):
    if radius < 0:
        print("Error: raduis cannot be less than 0")
        return
    
    area = calculate_area(radius)
    print("The area of a circle with radius " + str(radius) + " is: " + str(area))

def main():
    radius = 5
    print_circle_area(radius)

main()

"""

Errors in the Original Script
Syntax Errors:

Concatenation with Non-String Type: In the print_circle_area function, radius is used as a string in concatenation, but it’s an integer.
Missing Parentheses in print: In Python 3, print is a function and requires parentheses.
Logic Errors:

Incorrect Area Calculation Formula: The formula for the area is correct, but we’ll fix this in context.
Concatenation Issue: The calculate_area function returns a float, but it is being concatenated with strings, which will cause an error.
No Validation for Radius: No validation for the radius to ensure it’s a positive number.

"""