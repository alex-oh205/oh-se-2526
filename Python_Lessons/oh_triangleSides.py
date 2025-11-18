"""
Name: Alex Oh
Date: 11/17/25

File: oh_triangleSides.py

Purpose: This program classifies a triangle as impossible, equilateral, isosceles, or scalene based on the lengths of its sides.
"""

s1 = float(input("Enter length of side 1: "))  # float
s2 = float(input("Enter length of side 2: "))  # float
s3 = float(input("Enter length of side 3: "))  # float
sides = [s1, s2, s3]
sides.sort()  # Sort the sides from smallest to largest
a, b, c = sides  # a and b are the smaller sides, c is the largest side
if a + b > c:   # Check possibility of triangle
    print("The lengths can form a triangle.")
    if a == b == c:                             # Check for equilateral
        print("The triangle is equilateral.")
    elif a == b or b == c or a == c:            # Check for isosceles
        print("The triangle is isosceles.")
    else:                                       # Otherwise, it's scalene
        print("The triangle is scalene.")
else:
    print("The lengths cannot form a triangle.")