Simple script to convert image files into ANSI Colored ASCII art
(Make sure your terminal supports ANSI Color!)

Example code:
```python
Import Colors, ASCII_Image
from PIL import Image

image = Image.open('emoji.jpg').resize((256,128))
ascii_obj = ASCII_Image(image)
ascii_obj.print_ascii()
```
# Input
<img src="https://s3.amazonaws.com/pix.iemoji.com/images/emoji/apple/ios-12/256/nerd-face.png" width="250" height="250">

# Output
<img src="https://i.ibb.co/bvntvNs/nerd.png" width="250" height="250">
