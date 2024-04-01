from PIL import Image, ImageOps
import numpy as np
from glob import glob
import os


def process_images():
    raw_images = glob(os.path.join(f"{os.getcwd()}\\images\\", "*.png"))
    processed_images = []
    for image in raw_images:
        image_init = Image.open(image).resize((128,128))
        image_grayscale = ImageOps.grayscale(image_init)

        processed_images.append(np.array(image_grayscale))
    return processed_images

def image_to_ascii(input_array):
    image_array = []
    for row in input_array:
        new_row = []
        for pixel_value in row:
            if pixel_value <= 15:
                new_row.append('█')
                continue
            if pixel_value <= 30:
                new_row.append('▓')
                continue
            if pixel_value <= 45:
                new_row.append('▐')
                continue
            if pixel_value <= 60:
                new_row.append('#')
                continue
            if pixel_value <= 75:
                new_row.append('@')
                continue
            if pixel_value <= 90:
                new_row.append('▒')
                continue
            if pixel_value <= 105:
                new_row.append('0')
                continue
            if pixel_value <= 120:
                new_row.append('%')
                continue
            if pixel_value <= 135:
                new_row.append('=')
                continue
            if pixel_value <= 150:
                new_row.append('+')
                continue
            if pixel_value <= 165:
                new_row.append('-')
                continue
            if pixel_value <= 180:
                new_row.append('_')
                continue
            if pixel_value <= 195:
                new_row.append('|')
                continue
            if pixel_value <= 210:
                new_row.append('!')
                continue
            if pixel_value <= 225:
                new_row.append('\'')
                continue
            if pixel_value <= 240:
                new_row.append('.')
                continue
            if pixel_value <= 255:
                new_row.append(' ')
                continue
            
        image_array.append(new_row)
    return image_array

def print_out_img(image_array):
    for row in image_array:
        for col in row:
            print(col, end ="")
        print("")

def output_to_txt(image_array, name):
    f = open(f"{os.getcwd()}\\output\\{name}.txt", "w",encoding="utf-8")
    for row in image_array:
        for col in row:
            f.write(col)
        f.write("\n")

if __name__ == "__main__":
    images = process_images()
    i = 0
    for image in images:
        i += 1
        output_to_txt(image_to_ascii(image), f'{i}_output')
    print("\nSuccessfully Outputed txt files\n")
