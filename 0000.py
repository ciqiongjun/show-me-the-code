import os
from PIL import Image, ImageFont, ImageDraw


def num_add(file):
    with Image.open(file) as f:
        fn, ext = os.path.splitext(file)
        mydraw = ImageDraw.Draw(f)
        myfont = ImageFont.truetype(r'c:\windows\fonts\simhei.ttf', 60)
        x, y = f.size
        mydraw.text((x-70, 0), '99', '#ff0000', myfont)
        f.save(fn+'_added'+ext, 'jpeg')


if __name__ == '__main__':
    num_add(r'd:\gakki\1000.jpg')