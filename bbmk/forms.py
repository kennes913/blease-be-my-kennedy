"""
TODO: add docstring
"""
from database import expected

from wtforms import Form
from wtforms import ValidationError
from wtforms.validators import DataRequired, InputRequired
from wtforms import StringField, SelectField, FileField

class Bouncer:
	"""
	TODO: add docstring 
	"""
	def __init__(self, guest_list=None):
		if guest_list:
			self.approved = [guest.lower() for guest in guest_list]
		else:
			self.approved = [guest.name.lower() for guest in expected.select()]

	def __call__(self, form, field):
		if str(field.data).lower() not in self.approved:
			raise ValidationError('This name is now on the guest list.')


class RSVPForm(Form):
	"""
	TODO: add docstring 
	"""
	placeholders = {'name':{"placeholder":"First and Last Name"},
				    'email':{"placeholder":"email@domain.com"},
				    'guests':{"placeholder":"Enter guest name"}}
	events = [('', ''),
			  ('Ceremony','Wedding at Chapel Dulcinea (3:30-4:30 P.M.)'), 
			  ('Reception','Reception at Palm Door (5:00-11:00 P.M.)'),
			  ('Both', 'Both')]					
	guests = [('', ''),('Yes', 'Yes'),('No', 'No')]

	name = StringField('Name', validators=[InputRequired(), Bouncer()], render_kw=placeholders['name']) # Bouncer Validator not inserted for testing purposes
	email = StringField('What is your email address?', validators=[DataRequired()], render_kw=placeholders['email'])
	guests = SelectField('Are you bringing a guest?', choices=guests, validators=[DataRequired()])
	events = SelectField('What event(s) are you attending?', choices=events, validators=[DataRequired()])
	add_guest_1 = StringField('Guest #1', default=None, render_kw=placeholders['name'])
	add_guest_2 = StringField('Guest #2', default=None, render_kw=placeholders['name'])
	add_guest_3 = StringField('Guest #3', default=None, render_kw=placeholders['name'])


class FileUploadForm(Form):
	"""
	TODO: add docstring 
	"""
	guests = FileField()	

