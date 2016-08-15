"""
Add all forms here, see:

https://flask-wtf.readthedocs.io/en/latest/quickstart.html#creating-forms

"""
from wtforms import Form
from wtforms import StringField, SelectField, DateTimeField, IntegerField
from wtforms.validators import DataRequired

class RSVPForm(Form):
	"""
	"""
	name = StringField(u'Name', validators=[DataRequired()])
	email = StringField(u'Email', validators=[DataRequired()])
	guests = IntegerField(u'Guests', validators=[DataRequired()])
	hotel = SelectField(u'Hotel Info', validators=[DataRequired()])

