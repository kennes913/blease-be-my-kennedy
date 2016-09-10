import os

from app import db, app_config
from forms import RSVPForm
from database import guest

from datetime import datetime 
from flask import Flask, render_template, Blueprint, request, redirect, url_for

views = Blueprint('general', __name__)

@views.route('/')
def home():
  return render_template('base.html')

@views.route('/photos')
def photos():
  filenames = os.listdir(app_config.STATIC_IMAGES_PATH)
  return render_template('photos.html', filenames=filenames)

@views.route('/rsvp')
def event():
	return render_template('rsvp.html', form=RSVPForm())

@views.route('/submit_rsvp', methods=['POST'])
def submit_rsvp():
	form = RSVPForm(request.form)
	submit_time = datetime.strftime(datetime.now(), '%Y-%m-%d T %H:%M:%S')
	if form.validate():
		db.connect_db()
		new = guest.create(rsvp_time=submit_time,
						   name=form.name.data,
						   email=form.email.data,
						   guests=form.guests.data,
						   hotel_rec=form.hotel_rec.data)
		new.save()
		return redirect(url_for('general.success'))
	else:
		return render_template('rsvp.html', form=form)

@views.route('/success', methods=['GET'])
def success():
	if request.referrer:
		return render_template('success.html')
	else:
		return render_template('404.html')


	







