import os
import csv 
import openpyxl

from app import db, app_config, utils, basic_auth
from werkzeug.utils import secure_filename
from forms import RSVPForm, FileUploadForm
from database import guest, expected

from flask import (Flask, render_template, Blueprint, 
	request, redirect, url_for)

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
			utils.process_RSVP_form(guest, form.data) 
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
	if request.method == 'POST':	
		if not request.files:
			return redirect(request.url)
		file = request.files.items()[0][1]
		if file.filename == '':
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			if 'csv' in file.filename:
				expected_guests = utils.csv_guests_to_list(file.stream)
			if 'xlsx' in file.filename: 
				expected_guests = utils.xls_guests_to_list(file.stream)
			with db.database.atomic():
				db.database.truncate_table(expected)
				expected.insert_many(expected_guests).upsert(True).execute()
			return redirect(url_for('general.manage', filename=file.filename))
	if request.method == 'GET':
		db.connect_db()
		current_guests = [rsvped_guest._data for rsvped_guest in guest.select()]
		return render_template('manage.html', form=FileUploadForm(), guests=current_guests)







