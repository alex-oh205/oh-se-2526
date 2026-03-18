import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            

def frame_one_image(original_image, color, width):
    """ Frames a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with a border of specified color and width
    """
    img_width, img_height = original_image.size
    
    # Make the new image, starting with border
    result = PIL.Image.new('RGBA', (int(img_width + 2*width), int(img_height + 2*width)), color)
    result.paste(original_image, (width,width))
    return result

def alter_one_image(original_image):
    """ Alters a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image
    """
    width, height = original_image.size

    ###
    #create a mask
    ###
    
    mask1 = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer1 = PIL.ImageDraw.Draw(mask1)
    drawing_layer1.polygon([(0, height / 2),(width / 2, 0),
                            (width, height / 2),(width / 2, height)],
                            fill=(127,0,127,255))
    
    mask2 = PIL.Image.new('RGBA', (width, height), (127,0,127,255))
    drawing_layer2 = PIL.ImageDraw.Draw(mask2)
    drawing_layer2.polygon([(0, height / 2),(width / 2, 0),
                            (width, height / 2),(width / 2, height)],
                            fill=(127,0,127,0))
    
    # Make the new image, starting with border
    result = PIL.Image.new('RGBA', original_image.size, (0, 0, 0, 0))
    result.paste(original_image, (0, 0), mask=mask2)
    result.paste(original_image.rotate(180), (0, 0), mask=mask1)
    return result
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def frame_all_images(directory=None, color=(255, 0, 0), width=2):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'Framed', creating it if it does not exist.
    New image files are of type PNG and have a border.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'Framed'
    new_directory = os.path.join(directory, 'Framed')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        new_image = frame_one_image(curr_image, color, width)
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)

def alter_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'Altered', creating it if it does not exist.
    New image files are of type PNG and have a border.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'Altered'
    new_directory = os.path.join(directory, 'Altered')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        new_image = alter_one_image(curr_image)
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)