# Alex Oh
# 11/11/25
# Triangle Area Calculator
# This program calculates the area of a triangle given its base and height.

base = float(input("Enter the base of the triangle: "))         # Get base from user
height = float(input("Enter the height of the triangle: "))     # Get height from user
area = 0.5 * base * height                                      # Calculate area
print(f"The area of the triangle is: {area:.3f}")               # Display area rounded to 3 decimal places