from wtforms import Form,StringField,validators,TextAreaField,SubmitField
#from flask_wtf import Form


class ContactForm(Form):
	name = StringField('Name', [validators.DataRequired()])
	email = StringField('Email', [validators.DataRequired(), validators.Email('your@email.com')])
	address = StringField('Address', [validators.DataRequired])
	subject = StringField('Subject', [validators.DataRequired()])
	message = TextAreaField('Message', [validators.DataRequired()])
	
	
