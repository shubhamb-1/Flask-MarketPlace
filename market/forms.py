from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField
from wtforms.validators import Length,Email,DataRequired,EqualTo,ValidationError
from market.models import User,Item

class RegisterForm(FlaskForm):
    def validate_username(self,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("This username already Exists,try with a new one")

    def validate_email_address(self,email_address_to_check):
        email=User.query.filter_by(email_address=email_address_to_check.data).first()
        if email:
            raise ValidationError("This email address already exits,try with a new one")

    username=StringField(label='User Name: ',validators=[Length(min=2,max=30),DataRequired()])
    email_address=StringField(label='Email Address: ',validators=[Email(),DataRequired()])
    password1=PasswordField(label='Password: ',validators=[Length(min=6),DataRequired()])
    password2=PasswordField(label='Confirm Password: ',validators=[DataRequired(),EqualTo('password1')])
    submit=SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username=StringField(label='Username: ',validators=[DataRequired()])
    password=PasswordField(label='Password: ',validators=[DataRequired()])
    submit=SubmitField(label='Login')