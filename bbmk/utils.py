"""
The utils module contains functions used throughout
the flask app.
"""
import bbmk.config
import bbmk.app

import os
import subprocess
import openpyxl
import shutil
import csv

from datetime import datetime

def load_config(level=None):
	""" Returns config based on presence of various 
	configuration files. 

	return :: app configuration module 
	"""

	if level == 'production':
		return bbmk.config.production
	if level == 'default':
		return bbmk.config.default
	if level == 'develop':
		return bbmk.config.develop

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
	file = open(config._basedir+'/storage/{}.sqlite'.format(name), 'w')
	file.close()
	 

def remove_db_file(name):
	"""Delete target sqlite3 db file.
	
	:params name: str, name of database file 

	"""
	config = load_config()
	os.remove(config._basedir+'/storage/{}.sqlite'.format(name))


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


def process_rsvp_form(model, form_data):
	""" This takes in the data from the RSVP form, processes 
	any additional guests, adds in the original record and 
	pushes to sqlite database.

	:params table: table class, table you want to insert data
	:params form_data: dict, form data from users 
	
	"""
	push_to_database = []

	form_data['name'] = form_data['name'].strip()
	form_data['rsvp_time'] = datetime.strftime(
		datetime.now(), '%Y-%m-%d')
	form_data['guest_type'] = 'invited'

	if form_data['events'] == 'Both':
			form_data['ceremony'] = 'Yes'
			form_data['reception'] = 'Yes' 
	if form_data['events'] == 'Ceremony':
			form_data['ceremony'] = 'Yes'
			form_data['reception'] = 'No'
	if form_data['events'] == 'Reception':
			form_data['ceremony'] = 'No'
			form_data['reception'] = 'Yes'

	for field in form_data:
		if 'add' in field:
			if form_data[field]:
				temp = {'name':form_data[field].strip(), 
						'rsvp_time':form_data['rsvp_time'],
						'email':'None',
						'guest_type':'additional',
						'ceremony':form_data['ceremony'],
						'reception':form_data['reception']}
				push_to_database.append(temp)

	for field in ('add_guest_1','add_guest_2',
			'add_guest_3','guests','events'):
		del form_data[field]

	push_to_database.append(form_data)
	model.insert_many(push_to_database, validate_fields=True).upsert(True).execute()


def allowed_file(filename):
	""" This function determines whether or not the
	file is allowed to be uploaded.
	
	Written by Armin Ronacher:
	http://flask.pocoo.org/docs/0.11/patterns/fileuploads/

	:params filename: str, name of file being uploaded

	return :: bool
	"""

	return '.' in filename and \
		filename.rsplit('.', 1)[1] in bbmk.app.app_config.ALLOWED_EXTENSIONS


def process_excel_upload(file):
	""" This function parses an uploaded .xlsx or .xls file
	containing expected guests.

	:params name: Bytes.IO object, uploaded guest list
	
	return :: list, expected guest names
	"""
	store = []
	
	xls_upload = openpyxl.load_workbook(filename=file)
	worksheet = xls_upload[xls_upload.get_sheet_names()[0]]

	for column in worksheet.columns:
		if not isinstance(column[0].value, unicode):
			continue
		if column[0].value.lower() in ['name', 'guest']:
			for cell in column:
				if cell.value.lower() not in ['name', 'guest']:
					store.append(dict(name=cell.value.lower()))

	if not store:
		return False

	return store


def process_csv_upload(stream):
	""" This function parses an uploaded .csv file
	containing expected guests.

	:params stream: openpyxl.workbook object, uploaded guest list
	
	return :: list, expected guest names
	"""
	store = []
	mem_copy = [row for row in csv.reader(stream.readlines())]

	for title in ('name', 'guest', 'guest name'):
		try:
			index = mem_copy[0].index(title)
			break
		except ValueError:
			continue
	else:
		return False

	for line in mem_copy[1:]:
		store.append(dict(name=str(line[index].replace('\r\n', ''))))

	if not store:
		return False

	return store


def rsvp_guests_to_csv(model):
	""" This function queries a given model in the 
	database and returns a csv reperesentation. 
	
	:params model: table class, table you want query
	
	return :: str, csv representation of query
	"""
	headers = model._meta.sorted_field_names
	csv = ",".join(headers)+'\n'

	for record in model.select():
		values = record._data
		csv	+= ",".join([values[item] for item in headers])+'\n'

	return csv 















