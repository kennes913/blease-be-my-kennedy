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
	
	name = StringField(u'Name', validators=[DataRequired(message='We need to know who you are.')], render_kw={"placeholder":"Enter your full name"})
	email = StringField(u'What is your email address?', validators=[DataRequired(message="We need an email.")], render_kw={"placeholder":"email@domain.com"})
	guests = IntegerField(u'How many guests are you bringing?', validators=[DataRequired(message="We need to know how many guests your're bringing.")], render_kw={"placeholder":"# of guests you plan to bring"})
	hotel_rec = SelectField(u'Are you interested in hotel information?', choices=hotel_info_choices, validators=[DataRequired(message="Please choose yes or no.")])
	submit = SubmitField("RSVP")


