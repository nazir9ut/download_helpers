from db import *
import PIL
from PIL import Image



orig_img_path = '/home/naz/Desktop/avto_6500/all_img'

new_img_path = '/home/naz/Desktop/avto_6500/all_img_scaled'

all_rows = Avtonomera.select()



for row in all_rows:
    img = Image.open(orig_img_path + '/' + row.name)

    new_width = int(round(row.width / float(row.scale)))
    new_height = int(round(row.height / float(row.scale)))

    print new_width

    img = img.resize((new_width, new_height), PIL.Image.ANTIALIAS)

    img.save(new_img_path + '/' + row.name)