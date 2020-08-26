from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    Name = StringField('Name', validators=[DataRequired(), Length(max=50)],render_kw={'placeholder':'Name'})
    username = StringField('Username', validators = [DataRequired(), Length(min=2, max=20)],
                           render_kw={'placeholder':'UserName'})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw = {'placeholder':'Email'})
    Date_Of_Birth = DateField('DOB', validators=[DataRequired()], render_kw={'placeholder':'Date of Birth'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder':'Password'})
    confirm_password = PasswordField('Confirm_Password',
                    validators=[DataRequired(), EqualTo('Password')],render_kw={'placeholder':'Confirm Password'})

    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw = {'placeholder':'Email'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder':'Password'})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')