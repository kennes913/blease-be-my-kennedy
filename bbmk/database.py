"""
Put database models, functions and utilities here

"""
import utils

from peewee import *
from playhouse.flask_utils import FlaskDB

config = utils.load_config()
database = SqliteDatabase(config.DATABASE_PATH, **{})

class BaseModel(Model):
    class Meta:
        database = database

class guest(BaseModel):
	"""Guest RSVP information 
	"""
    email = CharField(null=True, primary_key=True)
    guests = IntegerField()
    hotel_rec = CharField()
    name = CharField()
    rsvp_time = TextField(null=True)

    class Meta:
        db_table = 'guest'

class user(BaseModel):
	"""Website User information
	"""
    active = IntegerField()
    admin = IntegerField()
    email = CharField(unique=True)
    password = CharField()
    username = CharField(unique=True)

    class Meta:
        db_table = 'user'



