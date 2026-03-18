'''
AlexOh431: Read and show an image.
'''
import matplotlib
matplotlib.use('TkAgg') # Must be specified before importing pyplot as plt
import matplotlib.pyplot as plt
import os.path
import numpy as np      # "as" lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 3 subplots
fig, ax = plt.subplots(1, 3)
# Show the image data in the subplots
for i in range(len(ax)):
    ax[i].imshow(img)
    ax[i].set_xlim((i + 4) * 10, (i + 5) * 10)
    ax[i].set_ylim(40, 30)

# Show the figure on the screen
plt.show()