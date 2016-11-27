"""
The database module contains all database models
used in flask app. 
"""
import utils

from peewee import *
from app import db

config = utils.load_config()

class DatabaseModel(db.Model):
    """ Base model. 
    """
    class Meta:
        database = db

class guest(db.Model):
    """ The guest table. This contains
    people who have RSVPed to the wedding.
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
    """ The expected table. This contains
    people who are invited to wedding. 
    """
    name = CharField(null=True, primary_key=True)

    class Meta:
        db_table = 'expected'



