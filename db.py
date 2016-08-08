from peewee import *
import datetime
import json


db = MySQLDatabase(
    'avto_nomera',  # Required by Peewee.
    user='root',  # Will be passed directly to psycopg2.
    password='z',
    host='127.0.0.1',
)



class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = db


    def __str__(self):
        r = {}
        for k in self._data.keys():
          try:
             r[k] = str(getattr(self, k))
          except:
             r[k] = json.dumps(getattr(self, k))
        return str(r)



class Avtonomera(BaseModel):
    class Meta:
        db_table = 'avto_nomera'

    name = TextField(unique=True)
    width = IntegerField()
    height = IntegerField()
    scale = CharField()
    points = TextField()
    scaled_points = TextField()
    bounding_rects = TextField()




