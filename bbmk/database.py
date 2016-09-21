"""
Put database models, functions and utilities here

"""
import utils

from peewee import *
from app import db

config = utils.load_config()

class DatabaseModel(db.Model):
    class Meta:
        database = db

class guest(db.Model):
    """Guest RSVP information 
    """
    rsvp_time = TextField(null=True)
    name = CharField(null=True, primary_key=True)
    email = CharField()
    guest_type = TextField(null=True)
    
    class Meta:
        db_table = 'guest'

class user(db.Model):
    """Website User information
    """
    active = IntegerField()
    admin = IntegerField()
    email = CharField(unique=True)
    password = CharField()
    username = CharField(unique=True)
    
    class Meta:
        db_table = 'user'



