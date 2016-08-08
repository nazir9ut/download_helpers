from db import *
import untangle
import xmltodict
import os
import json





all_rows = Avtonomera.select()

for row in all_rows:

    objects = json.loads(row.points)

    for idx, points in enumerate(objects):

        for idx2, point in enumerate(points):

            objects[idx][idx2]['x'] = float(objects[idx][idx2]['x']) / float(row.scale)
            objects[idx][idx2]['y'] = float(objects[idx][idx2]['y']) / float(row.scale)

            objects[idx][idx2]['x'] = int(round(objects[idx][idx2]['x']))
            objects[idx][idx2]['y'] = int(round(objects[idx][idx2]['y']))




    row.scaled_points = json.dumps(objects)
    row.save()
