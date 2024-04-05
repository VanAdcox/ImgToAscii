Simple script to convert image files into ANSI Colored ASCII art

example code:
```python
Import Colors, ASCII_Image
from PIL import Image

image = Image.open('emoji.jpg').resize((128,128))
ascii_obj = ASCII_Image(image)
ascii_obj.print_ascii()
```
![alt text](https://i.ibb.co/BwBhWsg/nerd.png "Nerd ACII") ![alt text](https://s3.amazonaws.com/pix.iemoji.com/images/emoji/apple/ios-12/256/nerd-face.png "Nerd Emoji")
