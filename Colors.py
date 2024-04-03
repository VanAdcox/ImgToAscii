import math,sys
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

    RGB_PALETTE = []
    
    def __init__(self):
        rgb_pallette = []
        for atr in Colors.__dict__.keys():
            if atr.__contains__('RGB'):
                rgb_pallette.append(Colors.__dict__.get(atr))
        self.RGB_PALETTE = rgb_pallette
        
 
    def clrPrint(self, color, text):
        print(f"{color}{text}{self.RESET}")
    
    def get_closest_color(self, input_rgb):
        closest_color = self.BLACK_RGB
        closest_dist = sys.maxsize 
        for rgb_color in self.RGB_PALETTE:
            dist = math.sqrt((rgb_color[0]-input_rgb[0]) + (rgb_color[1]-input_rgb[1]) + (rgb_color[2]-input_rgb[2]))
            
            if dist < closest_dist:
                closest_dist = dist
                closest_color = rgb_color
        return closest_color

