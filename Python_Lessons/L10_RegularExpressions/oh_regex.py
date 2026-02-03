"""
Name: Alex Oh
Date: 11/25/25

File: oh_regex.py

Objective: Uses regular expressions to extract all revision numbers and compute their average.
"""

import re

def main(): # Find all lines containing "New Revision: [number]" and compute the average of the numbers.
    with open("L10_mbox-short.txt", "r") as f:
        revisions = []
        for line in f:
            line = line.rstrip()    # Remove all trailing whitespace
            revision = re.findall(r"^New Revision:\s(\d{5})", line) # Find all revision numbers
            
            if len(revision) > 0:
                revisions.append(int(revision[0])) # Append to revisions list as integer if found
    
    if revisions:   # If revisions list is not empty
        average_revision = sum(revisions) / len(revisions) # Compute average
        print(f"Average: {average_revision:.3f}") # Display average rounded to three decimal places

if __name__ == "__main__":
    main()