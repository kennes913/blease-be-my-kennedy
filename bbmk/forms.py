
from database import expected

from wtforms import Form
from wtforms import ValidationError
from wtforms.validators import DataRequired, InputRequired
from wtforms import StringField, SelectField, FileField

class Bouncer:
	""" A callable class used as a field validator 
	for the name field in the RSVPForm class.

	:params list: list, list of strings of guests
	"""
	def __init__(self, guest_list=None):
		if guest_list:
			self.approved = [guest.lower() for guest in guest_list]
		else:
			self.approved = [guest.name.lower() for guest in expected.select()]

	def __call__(self, form, field):
		if str(field.data).lower() not in self.approved:
			raise ValidationError('Dummy Error thrown.')

class RSVPForm(Form):
	""" An RSVP form for wedding guests.
	"""
	event_choices = [('', ''),
					('Ceremony','Wedding at Chapel Dulcinea'), 
					('Reception','Reception at Palm Door'),
					('Both', 'Both')]					
	additional_guest_choices = [('', ''),('Yes', 'Yes'), ('No', 'No')]

	name = StringField(u'Name', validators=[InputRequired(), Bouncer()], render_kw={"placeholder":"First Name and Last Name"})
	email = StringField(u'What is your email address?', validators=[DataRequired(message="Did you input your email?")], render_kw={"placeholder":"email@domain.com"})
	guests = SelectField(u'Are you bringing additional guests?', choices=additional_guest_choices, validators=[DataRequired(message="Are you bringing guests?")])
	events = SelectField(u'What event(s) are you attending?', choices=event_choices, validators=[DataRequired(message="What are you attending??")])
	add_guest_1 = StringField(u'Additional Guest #1', default=None, render_kw={"placeholder":"Enter guest name"})
	add_guest_2 = StringField(u'Additional Guest #2', default=None, render_kw={"placeholder":"Enter guest name"})
	add_guest_3 = StringField(u'Additional Guest #3', default=None, render_kw={"placeholder":"Enter guest name"})
	add_guest_4 = StringField(u'Additional Guest #4', default=None, render_kw={"placeholder":"Enter guest name"})
	add_guest_5 = StringField(u'Additional Guest #5', default=None, render_kw={"placeholder":"Enter guest name"})

class FileUploadForm(Form):
	""" An RSVP form for wedding guests.
	"""
	guests = FileField('File:', validators=[InputRequired()], render_kw={"placeholder":"Add your csv or xlsx file here."})
