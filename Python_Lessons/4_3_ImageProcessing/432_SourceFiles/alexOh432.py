'''
AlexOh432: Change pixels in an image.
'''

import matplotlib.pyplot as plt
import os.path
import numpy as np

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename).copy()

# print(img) # Prints the array of pixels
# print("# of rows in image:  " + str(len(img)))  # The number of rows in the image
# print("# of columns in image:  " + str(len(img[0])))  # The number of columns in the image
# print("Color of pixel at (5, 9):  " + str(img[5][9]))  # The color of the pixel at (5, 9)
# print("Green intensity at (5, 9):  " + str(img[5][9][1]))  # The green intensity at pixel (5, 9)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)

###
# Change a region if condition is True
###

height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if int(img[r][c].sum()) > 500: # brightness R+G+B goes up to 3*255=765
            img[r][c] = [255, 0, 255] # R + B = magenta

for r in range(420, 470):
    for c in range(135, 165):
        if int(img[r][c].sum()) > 500:
            img[r][c] = [0, 255, 0]

# Show the image data in a subplot - this is called after all image updates
# and just before you show the figure.
ax.imshow(img, interpolation='none')

# Show the figure on the screen
plt.show()