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
	hotel_info_choices = [("Yes", "Yes"), ("No", "No")]
	
	name = StringField(u'Name', default='Enter your name', validators=[DataRequired(message='We need to know who you are.')])
	email = StringField(u'What is your email address?', default='email@domain.com', validators=[DataRequired(message="We need an email.")])
	guests = IntegerField(u'How many guests are you bringing?', default='Enter # of guests', validators=[DataRequired(message="We need to know how many guests your're bringing.")])
	hotel_rec = SelectField(u'Are you interested in hotel information?',choices=hotel_info_choices,validators=[DataRequired(message="Please choose yes or no.")])
	submit = SubmitField("RSVP")


