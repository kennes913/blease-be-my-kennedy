
from forms import RSVPForm
from database import database, guest

from datetime import datetime 
from flask import Flask, render_template, Blueprint, request, flash, redirect, url_for

views = Blueprint('general', __name__)

@views.route('/')
def index():
  return render_template('index.html')

@views.route('/registry')
def wedding_registry():
  raise NotImplementedError

@views.route('/event')
def event():
	return render_template('event.html', form=RSVPForm())

@views.route('/photos')
def photos():
  raise NotImplementedError

@views.route('/espresso')
def espresso_machine():
  raise NotImplementedError

@views.route('/success')
def success():
	return render_template('success.html')

@views.route('/rsvp', methods=['POST'])
def rsvp():
	form = RSVPForm(request.form)
	submit_time = datetime.strftime(datetime.now(), '%Y-%m-%d T %H:%M:%S')
	if request.method=='POST':
		if form.validate():
			database.connect()
			new_guest = guest.create(rsvp_time=submit_time,
									 name=form.name.data,
									 email=form.email.data,
									 guests=form.guests.data,
									 hotel_rec=form.hotel_rec.data)
			new_guest.save()
			database.close()
			return redirect(url_for('general.success'))
		else:
			return redirect(url_for('general.event'))


	







