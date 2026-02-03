"""
Name: Alex Oh
Date: 12/2/25
File: oh_countValues.py
Objective: Takes a user entered dictionary and returns the number of unique values it contains.
"""

# Get number of entries for the dictionary from user
n = int(input("Enter the number of dictionary entries: "))

user_dict = {}

# Loop specified number of times to get user input for dictionary entries
for _ in range(n):
    # Get key-value pairs from user
    key = input("Enter key: ")
    value = input("Enter value: ")

    # Add the key-value pair to the dictionary
    user_dict[key] = value

# Convert dict values to a set, which can only contain distinct items
unique_values = set(user_dict.values())

# Display number of unique values and the dictionary contents
print(f"There are {len(unique_values)} in the dictionary.")
for key, value in user_dict.items():
    print(f"{key}: {value}")