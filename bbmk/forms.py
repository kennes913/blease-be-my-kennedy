"""
Add all forms here, see:

https://flask-wtf.readthedocs.io/en/latest/quickstart.html#creating-forms

"""
from wtforms import Form
from wtforms.validators import DataRequired
from wtforms import StringField, RadioField, DateTimeField, IntegerField, SubmitField


class RSVPForm(Form):
	""" Wedding Guest RSVP Form.
	"""
	hotel_info_choices = [("Yes", "Yes"), ("No", "No")]
	
	name = StringField(u'Name', validators=[DataRequired(message='We need to know who you are.')])
	email = StringField(u'Email')
	guests = IntegerField(u'Guests',validators=[DataRequired(message="We need to know if you're bringing guests.")])
	hotel_rec = RadioField(u'Hotel Info',choices=hotel_info_choices)
	submit = SubmitField("RSVP")


