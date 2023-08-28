from graphics import graphics


def load_image(file, width, height):
    image = []
    for line in file:
        line = line.strip().split()
        row = []
        for i in range (0, len(line), 3):
            pixel = ( int(line[i]), int(line[i+1]), int(line[i+2]) )
            row.append(pixel)
        image.append(row)
    return image


def display_image(image, width, height, scale):
    gui = graphics(width * scale, height * scale, "Custom PPM Image Viewer")
    for row in range (len(image)):
        for column in range (len(image[row])):
            pixel = image[row][column]
            color = gui.get_color_string(pixel[0], pixel[1], pixel[2])
            gui.rectangle(column * scale, row * scale, scale, scale, color)
    gui.draw()


def convert_to_black_and_white(image):
    for row in range (len(image)):
        for column in range (len(image[row])):
            pixel = image[row[column]]
            average = int((pixel[0] + pixel[1] + pixel[2]) / 3)
            image[row][column] = (average, average, average)


def get_neighbor_average(image, row, column, amount, channel):            
    '''          
    This function get's the average of a sub-grind of pixels from within an image.       
    It does this for one color channel at a time (red=0, green=1, blue=2).
    Parameters:  
        image: The 2D-array of RGB tuples, representing the full image.     
        row: The row of the pixel to calculate the average-of-neighbors for.
        column: The column of the pixel to calculate the average-of-neighbors for.         
        amount: The amount of blurring to do (determines the amount of neighbors to check).
        channel: The color channel to get the average for (red=0, green=1, blue=2)
    The function returns the average calculated.
    '''          
    summation = 0                                                         
    count = 0    
    # Iterate through a subset of the pixels in the image.                
    # The amount to iterate over is controlled by the amount parameter.   
    for i in range(row-amount, row+amount):                               
        for j in range(column-amount, column+amount):                     
            # This if ensures that the color being checked is within the image boundaries.
            if i >= 0 and j >= 0 and i < len(image) and j < len(image[0]):
                summation += image[i][j][channel]
                count += 1
    # Calculate the average and return
    return int(summation / count)

def main():
    file_name = input("What file to load: ")
    scale = float(input("How should I scale the image? "))

    file = open(file_name, 'r')
    image_format = file.readline().strip()
    width_height = file.readline().strip().split(" ")
    width = int(width_height[0])
    height = int(width_height[1])
    max_rgb = int(file.readline())

    full_image = load_image(file, width, height)

    # <-- Execute whatever image manipulation code you want here, before displaying
    print()
    display_image(full_image, width, height, scale)
    convert_to_black_and_white(full_image)
    
main()
