import math,sys
class Colors:
    COLORS = {
        'BLACK' : '\033[30m',
        'RED' : '\033[31m',
        'GREEN' : '\033[32m',
        'YELLOW' : '\033[33m',
        'BLUE' : '\033[34m',
        'MAGENTA' : '\033[35m',
        'CYAN' : '\033[36m',
        'LIGHT_GRAY' : '\033[37m',
        'DARK_GRAY' : '\033[90m',
        'BRIGHT_RED' : '\033[91m',
        'BRIGHT_GREEN' : '\033[92m',
        'BRIGHT_YELLOW' : '\033[93m',
        'BRIGHT_BLUE' : '\033[94m',
        'BRIGHT_MAGENTA' : '\033[95m',
        'BRIGHT_CYAN' : '\033[96m',
        'WHITE' : '\033[97m',
    }

    COLORS_RGB = {
        'BLACK' : (0, 0, 0), 
        'RED' : (197, 15, 31), 
        'GREEN' : (19, 161, 14), 
        'YELLOW' : (193, 156, 0), 
        'BLUE' : (0, 55, 218), 
        'MAGENTA' : (178, 0, 178), 
        'CYAN' : (58, 150, 221), 
        'LIGHT_GRAY' : (118, 118, 118), 
        'DARK_GRAY' : (204, 204, 204), 
        'BRIGHT_RED' : (231, 72, 86), 
        'BRIGHT_GREEN' : (22, 198, 12), 
        'BRIGHT_YELLOW' : (249, 241, 165), 
        'BRIGHT_BLUE' : (59, 120, 255), 
        'BRIGHT_MAGENTA' : (180, 0, 158), 
        'BRIGHT_CYAN' : (41, 184, 219), 
        'WHITE' : (255, 255, 255), 
    }

    RESET = '\033[0m' 
 
def clrPrint(color, text):
    print(f"{color}{text}{Colors.RESET}")

def get_closest_color(input_rgb):
    closest_color = Colors.COLORS_RGB.get('BLACK')
    closest_dist = sys.maxsize 

    for rgb_color in Colors.COLORS_RGB.values():
        dist = math.sqrt( abs( pow(((rgb_color[0]-input_rgb[0]) * .3),2) + pow(((rgb_color[1]-input_rgb[1]) * .25),2) + pow(((rgb_color[2]-input_rgb[2]) * .3),2)))
        
        if dist < closest_dist:
            closest_dist = dist
            closest_color = rgb_color
    # TW: bad code  | grabs ANSI code
    return Colors.COLORS.get((list(Colors.COLORS_RGB.keys())[list(Colors.COLORS_RGB.values()).index(closest_color)]))
