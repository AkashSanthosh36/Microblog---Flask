from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,SelectField
from wtforms.validators import DataRequired
mychoice=[('a','b'),('c','d'),('e','f')]
class LoginForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired()])
	password=PasswordField('Password',validators=[DataRequired()])
	aka=SelectField(u'choose',choices=mychoice,validators=[DataRequired()])
	if(aka=='adfn')
	mychoice=(faldsf)
	
	remember_me=BooleanField('Remember Me')
	submit=SubmitField('Sign In')