"""
Put database models, functions and utilities here

"""
from playhouse.flask_utils import FlaskDB

# http://flask.pocoo.org/docs/0.10/patterns/appfactories/
# http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#flask-utils

database = FlaskDB()

class Admin(database.Model):
	raise NotImplementedError

class Guest(database.Model):
	raise NotImplementedError

class Comment(database.model):
	raise NotImplementedError




