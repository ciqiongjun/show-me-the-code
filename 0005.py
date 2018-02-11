import os
import glob
from PIL import Image


def thumb(path):
    size = 1136, 640
    for pic in glob.glob(path+r'\*.jpg'):
        fn, ext = os.path.splitext(pic)
        im = Image.open(pic)
        im.thumbnail(size)
        im.save(fn+'_thumb'+ext, 'jpeg')
        im.close()


if __name__ == '__main__':
    thumb(r'd:\gakki')
