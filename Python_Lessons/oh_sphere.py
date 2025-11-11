"""
Name: Alex Oh
Date: 11/11/25

File: oh_sphere.py

Purpose: This program calculates the diameter, circumference, surface area, and volume of a sphere given its radius.
"""

import math

def main():
    # Gather inputs
    radius = float(input("Enter the radius of the sphere: "))

    diameter = 2 * radius                       # Calculate diameter
    circumference = 2 * math.pi * radius        # Calculate circumference
    surface_area = 4 * math.pi * radius ** 2    # Calculate surface area
    volume = (4/3) * math.pi * radius ** 3      # Calculate volume

    # Display the results rounded to 2 decimal places
    print(f"Diameter: {diameter:.2f}")
    print(f"Circumference: {circumference:.2f}")
    print(f"Surface Area: {surface_area:.2f}")
    print(f"Volume: {volume:.2f}")

main()  # Call the main() function