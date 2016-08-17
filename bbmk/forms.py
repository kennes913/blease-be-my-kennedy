"""
Add all forms here, see:

https://flask-wtf.readthedocs.io/en/latest/quickstart.html#creating-forms

"""
from wtforms import Form
from wtforms import StringField, RadioField, DateTimeField, IntegerField, SubmitField


class RSVPForm(Form):
	""" Wedding Guest RSVP Form.
	"""
	hotel_info_choices = [("Yes", "Yes"), ("No", "No")]
	
	name = StringField(u'Name')
	email = StringField(u'Email')
	guests = IntegerField(u'Guests')
	hotel_rec = RadioField(u'Hotel Info', choices=hotel_info_choices)
	submit = SubmitField("RSVP")


