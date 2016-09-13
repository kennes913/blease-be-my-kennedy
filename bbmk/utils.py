import bbmk.config

import os
import subprocess

def load_config():
	""" Returns config based on presence of various 
	configuration files. 

	return :: app configuration module 
	"""
	try:
		if bbmk.config.develop:
			return bbmk.config.develop
		else:
			return bbmk.config.production
	except AttributeError:
	 	return bbmk.config.default

def write_db_file(name):
	"""Create a sqlite3 db file.
	
	:params name: str, name of database file 
	
	"""
	config = load_config()
	file = open(config._basedir+'/storage/{}.db'.format(name), 'w')
	file.close()
	 
def remove_db_file(name):
	"""Delete target sqlite3 db file.
	
	:params name: str, name of database file 

	"""
	config = load_config()
	os.remove(config._basedir+'/storage/{}.db'.format(name))

def build_database(config):
	""" Build the application datbase using a sql schema file.
	If database exists, do nothing. 
	
	:params config: config module, application configuration module
	
	"""
	if not os.path.isfile(config.DATABASE_PATH):
		write_db_file('database')
		db_file, schema_file = config.DATABASE_PATH, config.DATABASE_SCHEMA 
		subprocess.call("sqlite3 {} < {}".format(db_file, schema_file), shell=True)
		print 'Created database file.'
	else:
		print 'Attempted database creation failed. Database already exists.'

def create_admin_user(auth, user, password, email):
	""" Create a user auth table if one does not exists. Then create
	an Admin to edit site. 

	:params auth: flask_pewee.auth.Auth object
	:params user: str, set in environment's config
	:params password: str, set in environment's config
	
	"""
	auth.User.create_table(fail_silently=True)
	try:
		admin = auth.User(username=user, email=email, admin=True, active=True)
		admin.set_password(password)
		admin.save()
		print 'Admin user {} created. Use secret key from config.'.format(user)
	except:
		print 'Attempted Admin creation failed. Admin user already exists.'








