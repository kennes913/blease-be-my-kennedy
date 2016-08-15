from flask import Flask, render_template, Blueprint

from forms import RSVPForm

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

@views.route('/rsvp', methods=["GET", "POST"])
def rsvp():
	form = RSVPForm()
	if form.validate_on_submit():
		print 'It worked!'
		return redirect(url_for('index'))
	return render_template('event.html', form=form)



