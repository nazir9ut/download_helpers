import xml.etree.cElementTree as ET
import numpy as np
import cv2
from db import *
import json


all_rows = Avtonomera.select()



final_xml_path = '/home/naz/Desktop/avto_6500/final_xml'


for row in all_rows:
    # print row.id
    # print row.name.split('.')[0]


    bounding_rects = json.loads(row.bounding_rects)


    annotation = ET.Element("annotation")


    ET.SubElement(annotation, "folder").text = 'VOC2007'
    ET.SubElement(annotation, "filename").text = row.name.split('.')[0]


    source = ET.SubElement(annotation, "source")
    ET.SubElement(source, "database").text = "The VOC2007 Database"
    ET.SubElement(source, "annotation").text = "PASCAL VOC2007"
    ET.SubElement(source, "image").text = "flickr"
    ET.SubElement(source, "flickrid").text = row.name.split('.')[0]


    owner = ET.SubElement(annotation, "owner")
    ET.SubElement(owner, "flickrid").text = 'naz'
    ET.SubElement(owner, "name").text = "Thom Zemanek"


    size = ET.SubElement(annotation, "size")
    ET.SubElement(size, "width").text = str(int(round(row.width / float(row.scale))))
    ET.SubElement(size, "height").text = str(int(round(row.height / float(row.scale))))
    ET.SubElement(size, "depth").text = "3"

    ET.SubElement(annotation, "segmented").text = '0'


    for bounding_rect in bounding_rects:
        object = ET.SubElement(annotation, "object")
        ET.SubElement(object, "name").text = "plate"
        ET.SubElement(object, "pose").text = "Unspecified"
        ET.SubElement(object, "truncated").text = "0"
        ET.SubElement(object, "difficult").text = "0"

        xmin = str(bounding_rect[0])
        ymin = str(bounding_rect[1])
        xmax = str(bounding_rect[2])
        ymax = str(bounding_rect[3])


        bndbox = ET.SubElement(object, "bndbox")
        ET.SubElement(bndbox, "xmin").text = xmin
        ET.SubElement(bndbox, "ymin").text = ymin
        ET.SubElement(bndbox, "xmax").text = xmax
        ET.SubElement(bndbox, "ymax").text = ymax





    tree = ET.ElementTree(annotation)
    tree.write(final_xml_path + '/' + row.name.split('.')[0] +  ".xml")