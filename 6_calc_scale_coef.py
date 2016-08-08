from db import *

all_rows = Avtonomera.select()

for row in all_rows:

    if row.width > row.height:
        print row.id, 'xxx'
        row.scale = row.width / 500.0
    else:
        print row.id, 'ddd'
        row.scale = row.height / 500.0


    row.save()


