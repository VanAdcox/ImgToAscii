from PIL import Image, ImageOps
import numpy as np
import Colors

class Proccessed_Image:
    def __init__(self, image_file):
        self.image = image_file
        self.grayscale = ImageOps.grayscale(self.image)
        self.rgb_array = np.array(self.image)
        self.gray_array = np.array(self.grayscale)
    def image_to_ascii_array(self):
        image_array = []

        for row_index in range(len(self.gray_array)):
            next_row = []

            for col_index in range(len(self.gray_array[row_index])):
                pixel_brightness = self.gray_array[row_index][col_index]
                closest_color = Colors.get_closest_color(self.rgb_array[row_index][col_index])

                new_char = ' '
                if pixel_brightness <= 15:
                    new_char = '█'
                elif pixel_brightness <= 30:
                    new_char = '▓'
                elif pixel_brightness <= 45:
                    new_char = '▐'
                elif pixel_brightness <= 60:
                    new_char = '#'
                elif pixel_brightness <= 75:
                    new_char = '@'
                elif pixel_brightness <= 90:
                    new_char = '▒'
                elif pixel_brightness <= 105:
                    new_char = '0'
                elif pixel_brightness <= 120:
                    new_char = '%'
                elif pixel_brightness <= 135:
                    new_char = '='
                elif pixel_brightness <= 150:
                    new_char = '+'
                elif pixel_brightness <= 165:
                    new_char = '-'
                elif pixel_brightness <= 180:
                    new_char = '_'
                elif pixel_brightness <= 195:
                    new_char = '|'
                elif pixel_brightness <= 210:
                    new_char = '!'
                elif pixel_brightness <= 225:
                    new_char = '\''
                elif pixel_brightness <= 240:
                    new_char = '.'
                
                next_row.append(f'{closest_color}{new_char}')
            next_row.append(Colors.Colors.RESET)
            image_array.append(next_row)

        return image_array
    def print_ascii(self):
        image_array = self.image_to_ascii_array()
        
        for row in image_array:
            for col in row:
                print(col, end='')
            print('')


image = Image.open('emoji.jpg').resize((256,128))
ascii_obj = Proccessed_Image(image)

ascii_obj.print_ascii()
