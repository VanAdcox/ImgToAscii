Simple script to convert image files into ANSI Colored ASCII art

example code:
```python
Import Colors, ASCII_Image

image = Image.open('emoji.jpg').resize((255,128))
ascii_obj = ASCII_Image(image)
ascii_obj.print_ascii()
```
![alt text](https://i.ibb.co/BwBhWsg/nerd.png "Nerd Emoji")
