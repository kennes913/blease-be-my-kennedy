"""
Put database models, functions and utilities here

"""
import utils

import os
import subprocess

from playhouse.flask_utils import FlaskDB

def write_db_file(name):
	"""Create a sqlite3 db file.
	
	:params name: str, name of database file 

	returns :: return 
	"""
	config = utils.load_config()
	file = open(config._basedir+'/storage/{}.db'.format(name), 'w')
	file.close()
	 
def remove_db_file(name):
	"""Delete target sqlite3 db file.
	
	:params name: str, name of database file 

	returns :: return
	"""
	config = utils.load_config()
	os.remove(config._basedir+'/storage/{}.db'.format(name))

def build(config):
	""" Build the application datbase using a sql schema file.
	If database exists, do nothing. 
	
	:params config: config module, application configuration module

	returns :: return 
	"""
	if not os.path.isfile(config.DATABASE_PATH):
		print 'Building application database..'
		write_db_file('database')
		db_file, schema_file = config.DATABASE_PATH, config.DATABASE_SCHEMA 
		subprocess.call("sqlite3 {} < {}".format(db_file, schema_file), shell=True)
	else:
		print 'Application database is already built.'
	return

def build_admin_user(auth, user, password, email):
	""" Create a user auth table if one does not exists. Then create
	an Admin to edit site. 

	:params auth: flask_pewee.auth.Auth object
	:params user: str, set in environment's config
	:params password: str, set in environment's config

	returns :: return 
	"""
	auth.User.create_table(fail_silently=True)
	try:
		admin = auth.User(username=user, email=email, admin=True, active=True)
		admin.set_password(password)
		admin.save()
	except:
		print 'Admin user exists.'
	return 





