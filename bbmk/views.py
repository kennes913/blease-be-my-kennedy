"""
The views module contains all views routed in
flask app.
"""
import os
import csv 
import openpyxl

from utils import allowed_file, rsvp_guests_to_csv
from app import db, app_config, utils, basic_auth
from werkzeug.utils import secure_filename
from forms import RSVPForm, FileUploadForm
from database import guest, expected

from flask import (Flask, render_template, Blueprint, 
	request, redirect, url_for, make_response)


views = Blueprint('general', __name__)


@views.route('/')
def home():

  return render_template('home.html')


@views.route('/registry')
def registry():

	return render_template('registry.html')


@views.route('/ceremony')
def ceremony():

	return render_template('ceremony.html')


@views.route('/reception')
def reception():
	
	return render_template('reception.html')


@views.route('/story')
def story():

	return render_template('story.html')


@views.route('/rsvp', methods=['GET', 'POST'])
def rsvp():

	if request.method == 'GET':
		errors = request.args.get('errors')
		return render_template('rsvp.html',form=RSVPForm(), errors=errors)
	if request.method == 'POST':
		db.connect_db()
		form = RSVPForm(request.form)
		if form.validate():
			utils.process_rsvp_form(guest, form.data) 
			return redirect(url_for('general.success'))
		else:
			return render_template('rsvp.html', form=RSVPForm(), errors=form.errors)


@views.route('/success')
def success():

	if request.referrer:
		return render_template('success.html')
	else:
		return render_template('404.html')


@views.route('/manage', methods=['GET', 'POST'])
@basic_auth.required
def manage():

	current_guests = [rsvped_guest._data for rsvped_guest in guest.select()]

	if request.method == 'GET':		
		return render_template('manage.html',
			form=FileUploadForm(), guests=current_guests)

	if request.method == 'POST':

		file = request.files.items()[0][1]
		if file.filename == '':
			bad_file_name = 'No file was uploaded.'
			return render_template('manage.html',
				form=FileUploadForm(), guests=current_guests, error=bad_file_name)

		if file and allowed_file(file.filename):

			filename = secure_filename(file.filename)

			if 'csv' in file.filename:
				expected_guests = utils.process_csv_upload(file.stream)
			if 'xlsx' in file.filename: 
				expected_guests = utils.process_excel_upload(file.stream)

			if not expected_guests:
				bad_processing = ("The file format is wrong. "
					"Make sure to have a column with guest, name or guest name. "
					"The guest names should be First Name Space Last Name")
				return render_template('manage.html',
					form=FileUploadForm(), guests=current_guests, error=bad_processing)

			with db.database.atomic(): 
				db.database.truncate_table(expected)
				expected.insert_many(expected_guests).upsert(True).execute()
			return render_template('manage.html',
					form=FileUploadForm(), guests=current_guests, success=True)
		else:
			bad_file_type = 'Not an accepted file type.'
			return render_template('manage.html',
				form=FileUploadForm(), guests=current_guests, error=bad_file_type)


@views.route('/download')
def download():
	
	csv = rsvp_guests_to_csv(guest)
	response = make_response(csv)
	
	content_disposition = "attachment; filename=rsvp_guests.csv"
	response.headers['Content-Disposition'] = content_disposition
	response.mimetype = "text/csv"

	return response


















