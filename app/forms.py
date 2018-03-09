from wtforms import Form,StringField,TextAreaField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired



class ContactForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	subject = StringField('Subject', validators=[DataRequired()])
	body = TextAreaField('Message', validators=[DataRequired()])
	
	
