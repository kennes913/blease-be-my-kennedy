import os

from app import db, app_config, utils
from forms import RSVPForm
from database import guest

from flask import (Flask, render_template, Blueprint, 
	request, redirect, url_for)


views = Blueprint('general', __name__)


@views.route('/')
def home():
  return render_template('base.html')


@views.route('/photos')
def photos():
  filenames = os.listdir(app_config.STATIC_IMAGES_PATH)
  return render_template('photos.html', filenames=filenames)


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
			return render_template('rsvp.html', form=form, errors=form.errors)


@views.route('/success')
def success():
	if request.referrer:
		return render_template('success.html')
	else:
		return render_template('404.html')


	







