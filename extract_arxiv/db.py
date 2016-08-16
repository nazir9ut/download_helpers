from peewee import *
import datetime
import json


db = MySQLDatabase(
    'deep_learning',  # Required by Peewee.
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



class Arxiv(BaseModel):
    class Meta:
        db_table = 'arxiv'

    name = TextField(unique=True)





