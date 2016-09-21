"""
Add all forms here, see:

https://flask-wtf.readthedocs.io/en/latest/quickstart.html#creating-forms

"""
from wtforms import Form
from wtforms.validators import DataRequired
from wtforms import StringField, SelectField, DateTimeField, IntegerField, SubmitField


class RSVPForm(Form):
	""" Wedding Guest RSVP Form.
	"""
	hotel_info_choices = [('', ''),('Yes', 'Yes'), ('No', 'No')]
	additional_guest_choices = [('', ''),('Yes', 'Yes'), ('No', 'No')]

	name = StringField(u'Name', validators=[DataRequired(message='Did you input your name?')], render_kw={"placeholder":"Enter your full name"})
	email = StringField(u'What is your email address?', validators=[DataRequired(message="Did you input your email?")], render_kw={"placeholder":"email@domain.com"})
	guests = SelectField(u'Are you bringing additional guests?', choices=additional_guest_choices, validators=[DataRequired(message="Are you bringing guests?")])
	add_guest_1 = StringField(u'Additional Guest #1', default=None, render_kw={"placeholder":"Enter guest name"})
	add_guest_2 = StringField(u'Additional Guest #2', default=None, render_kw={"placeholder":"Enter guest name"})
	add_guest_3 = StringField(u'Additional Guest #3', default=None, render_kw={"placeholder":"Enter guest name"})
	add_guest_4 = StringField(u'Additional Guest #4', default=None, render_kw={"placeholder":"Enter guest name"})
	add_guest_5 = StringField(u'Additional Guest #5', default=None, render_kw={"placeholder":"Enter guest name"})


