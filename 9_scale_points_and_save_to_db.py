from db import *
import untangle
import xmltodict
import os
import json


all_rows = Avtonomera.select()

for row in all_rows:

    print json.loads(row.points)[0][0]['x']