import xml.etree.cElementTree as ET
import numpy as np
import cv2
from db import *
import json


all_rows = Avtonomera.select()


out_path = '/home/naz/Desktop/avto_6500'


for row in all_rows:
    print row.id

    with open(out_path + '/' + "trainval.txt", "a") as myfile:
        myfile.write(row.name.split('.')[0] + '\n')





