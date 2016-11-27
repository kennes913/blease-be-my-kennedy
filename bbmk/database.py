"""
TODO: add docstring
"""
import utils

from peewee import *
from app import db

config = utils.load_config()

class DatabaseModel(db.Model):
    class Meta:
        database = db

class guest(db.Model):
    """
    TODO: add docstring 
    """
    rsvp_time = TextField(null=True)
    name = CharField(null=True, primary_key=True)
    email = CharField()
    guest_type = TextField(null=True)
    ceremony = TextField(null=True)
    reception = TextField(null=True)
    
    class Meta:
        db_table = 'guest'

class expected(db.Model):
    """
    TODO: add docstring 
    """
    name = CharField(null=True, primary_key=True)

    class Meta:
        db_table = 'expected'



