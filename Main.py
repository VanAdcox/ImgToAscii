from PIL import Image, ImageOps
import numpy as np
from glob import glob
import os


class Colors:
    BLACK, BLACK_RGB = ('\033[30m',(0,0,0))
    RED, RED_RGB = ('\033[31m', (197,15,31))
    GREEN, GREEN_RGB = ('\033[32m', (19,161,14))
    YELLOW, YELLOW_RGB = ('\033[33m', (193,156,0))
    BLUE, BLUE_RGB = ('\033[34m', (0,55,218))
    MAGENTA, MAGENTA_RGB = ('\033[35m', (178,0,178))
    CYAN, CYAN_RGB = ('\033[36m', (58,150,221))
    LIGHT_GRAY, LIGHT_GRAY_RGB = ('\033[37m', (118,118,118))
    DARK_GRAY, DARK_GRAY_RGB = ('\033[90m', (204,204,204))
    BRIGHT_RED, BRIGHT_RED_RGB = ('\033[91m', (231,72,86))
    BRIGHT_GREEN, BRIGHT_GREEN_RGB = ('\033[92m', (22,198,12))
    BRIGHT_YELLOW, BRIGHT_YELLOW_RGB = ('\033[93m', (249,241,165))
    BRIGHT_BLUE, BRIGHT_BLUE_RGB = ('\033[94m', (59,120,255))
    BRIGHT_MAGENTA, BRIGHT_MAGENTA = ('\033[95m', (180,0,158))
    BRIGHT_CYAN,BRIGHT_CYAN = ('\033[96m', (41,184,219))
    WHITE, WHITE_RGB = ('\033[97m',(255,255,255))

    RESET = '\033[0m' 

    def clrPrint(self, color, text):
        print(f"{color}{text}{self.RESET}")


class Proccessed_Image:
    def __init__(self, image_file):
        self.image = Image.open(image_file).resize((128,128))
        self.grayscale = ImageOps.grayscale(self.image)
        self.rgb_array = np.array(self.image)
        self.gray_array = np.array(self.grayscale)
    def image_to_ascii_array(self):
        image_array = []
        for row in self.gray_array:
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



def process_images():
    raw_images = glob(os.path.join(f"{os.getcwd()}\\images\\", "*.png"))
    processed_images = []
    for image in raw_images:
        image_init = Image.open(image).resize((128,128))
        image_grayscale = ImageOps.grayscale(image_init)

        processed_images.append(np.array(image_grayscale))
    return processed_images

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


