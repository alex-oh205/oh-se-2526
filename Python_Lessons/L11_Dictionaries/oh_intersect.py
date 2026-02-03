"""
Name: Alex Oh
Date: 12/3/25
File: oh_intersect.py
Objective: Compares two dictionaries and prints a third dictionary
           that contains only the key/value pairs found in both of
           the original two dictionaries.
"""

dict1 = {"red": 3, "blue": 5, "green": 3, "yellow": 1, "purple": 2, "orange": 1}
dict2 = {"yellow": 1, "blue": 2, "orange": 1, "red": 1, "green": 3, "purple": 4}

intersection = {}

# Loop through keys in the first dictionary
for key in dict1.keys():
    if dict1[key] == dict2.get(key): # Check if key and value exist and match in second dictionary
        intersection[key] = dict1[key] # Add key and value to intersection dictionary

sortedKeys = sorted(intersection.keys()) # Sort third dictionary keys

# Loop through sorted keys and print key/value pairs
for key in sortedKeys:
    print(f"{key}: {intersection[key]}")