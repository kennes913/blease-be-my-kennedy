import bbmk.config

import os
import subprocess

from datetime import datetime 


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
		print 'Admin user exists.'


def process_RSVP_form(model, record):
	""" This takes in RSVP form data submitted by user and processes
	for import into database table. 

	:params table: table class, table you want to insert data
	:params record: dict, form data from users 
	"""
	records = []
	
	record['rsvp_time'] = datetime.strftime(datetime.now(), '%Y-%m-%d T %H:%M:%S')
	record['guest_type'] = 'invited'

	if record['events'] == 'Both':
			record['ceremony'] = 'Yes'
			record['reception'] = 'Yes'
	if record['events'] == 'Ceremony':
			record['ceremony'] = 'Yes'
			record['reception'] = 'No'
	if record['events'] == 'Reception':
			record['ceremony'] = 'No'
			record['reception'] = 'Yes'

	for field in record:
		if 'add_guest' in field:
			if record[field]:
				temp = {'name':record[field], 
						'rsvp_time':record['rsvp_time'],
						'email':record['email'],
						'guest_type':'additional',
						'ceremony':record['ceremony'],
						'reception':record['reception']}
				records.append(temp)

	del record['add_guest_1']
	del record['add_guest_2']
	del record['add_guest_3']
	del record['add_guest_4']
	del record['add_guest_5']
	del record['guests']
	del record['events']

	records.append(record)
	model.insert_many(records, validate_fields=True).upsert(True).execute()


def allowed_file(filename):
	""" This function determines whether or not the
	file is allowed to be uploaded.
	
	Written by Armin Ronacher:
	http://flask.pocoo.org/docs/0.11/patterns/fileuploads/

	:params filename: str, name of file being uploaded

	return :: bool
	"""
	return '.' in filename and \
		filename.rsplit('.', 1)[1] in bbmk.config.ALLOWED_EXTENSIONS


def xls_guests_to_list(stream):
	""" This function parses an uploaded .xlsx or .xls file
	containing expected guests.

	:params stream: Bytes.IO object, uploaded guest list
	
	return :: list, expected guest names
	"""
	store = []
	
	xls_upload = openpyxl.load_workbook(filename=file)
	worksheet = xls_upload[xls_upload.get_sheet_names()[0]]

	for row in worksheet.rows:
		for cell in row:
			if cell.value.lower() not in ['name', 'guest']:
				store.append(dict(name=cell.value.lower()))
	return store 


def csv_guests_to_list(stream):
	""" This function parses an uploaded .csv file
	containing expected guests.

	:params worksheet: openpyxl.workbook object, uploaded guest list
	
	return :: list, expected guest names
	"""
	store = []
	
	for item in stream.readlines():
		if item.lower() not in ['name', 'guest']:
			store.append(dict(name=str(item.replace('\r\n', ''))))

	return store
	




