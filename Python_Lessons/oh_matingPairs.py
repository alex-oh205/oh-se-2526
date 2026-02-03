"""
Name: Alex Oh
Date: 12/8/25
File: oh_matingPairs.py
Objective: This program pairs gerbils from two sets into a set of tuples.
"""

males = {'Dusty', 'Murphy', 'Olaf', 'Dante', 'Gizmo'}
females = {'Ginger', 'Lily', 'Piper', 'Daisy', 'Elsa'}
pairs = set()

# Loop until one of the sets is empty
while len(males) > 0 and len(females) > 0:
    # Remove value from each set and add as a tuple to pairs set
    pairs.add((males.pop(), females.pop()))

print(pairs)