from db import *
import untangle
import xmltodict
import os
import json






def get_objects_from_xml(xml_file):

    objects = []

    with open(xml_file) as fd:
        doc = xmltodict.parse(fd.read())

        xml_objects = doc['annotation']['object']



        if not isinstance(xml_objects, list):
            xml_objects = [xml_objects]



        for xml_object in xml_objects:
            points = []

            for pt in xml_object['polygon']['pt']:
                point = {}

                point['x'] = pt['x']
                point['y'] = pt['y']

                points.append(point)


            objects.append(points)


    return objects







xml_path = '/home/naz/Desktop/avto_6500/all_xml'


print get_objects_from_xml('/home/naz/Desktop/ru_8737213.xml')

all_rows = Avtonomera.select()

for row in all_rows:

    file_name_not_ext = os.path.splitext(row.name)[0]

    xml_file = xml_path + '/' + file_name_not_ext + '.xml'

    print xml_file

    json_str = json.dumps(get_objects_from_xml(xml_file))

    row.points = json_str

    row.save()







