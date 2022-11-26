"""Create Memes."""

from PIL import Image
from PIL import ImageDraw
import random
import textwrap


class MemeEngine:
    """Class for manipulating image files and adding text."""

    def __init__(self, save):
        """Initialize class."""
        self.save = save
        pass

    def make_meme(self, image_path, text, author, width=500) -> str:
        """Manipulate images files and saving the output."""
        print(image_path)
        wrapper = textwrap.TextWrapper(width=40)
        with Image.open(image_path) as im:
            if im.width > width:
                new_width = width
                new_height = im.height*500/im.width
                im = im.resize((new_width, int(new_height)))
            im_draw = ImageDraw.Draw(im)
            text_x = random.randint(0, 100)
            text_y = random.randint(0, 100)
            quotation = wrapper.fill(text=text)
            im_draw.text((text_x, text_y), quotation, fill=(255, 255, 0))
            im_draw.text((text_x, text_y + 30), author, fill=(255, 255, 0))
            saved_path = f'{self.save}/{random.randint(0,1000000)}.jpg'
            im.save(saved_path)
        im.close()
        return saved_path
