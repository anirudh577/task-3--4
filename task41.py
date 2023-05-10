from PIL import Image 
import numpy as np

# taking input
image_file_path = input("Please enter the path to your image file: ")

try:
    dataset_path = "path/to/dataset/folder"
    dataset_images = []
    for i in range(1, 150):
        img_path = dataset_path + "/image" + str(i) + ".png"
        imge = Image.open(img_path)
        dataset_images.append(imge)
#converting to hsv format
    input_path = "path/to/input/image.png"
    input_image = Image.open(input_path)
    hsv_input = input_image.convert('HSV')

#converting input image to hsv
    img = Image.open(image_file_path)
    img_hsv = img.convert("HSV")
    
    low_green = (30, 50, 50)
    up_green = (90, 255, 255)

    mask = Image.new('1', img.size)
    for x in range(img.width):
        for y in range(img.height):
            pixel = hsv.getpixel((x, y))
            if pixel[0] >= low_green[0] and pixel[0] <= up_green[0] and pixel[1] >= low_green[1] and pixel[1] <= \
                    up_green[1]:
                mask.putpixel((x, y), 1)
except IOError:
    print("Error: Unable to open image file.")
    