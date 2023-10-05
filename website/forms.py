from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Email

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email address", validators=[Email(), DataRequired()])
    password = PasswordField("Password", validators=[InputRequired(), DataRequired()])
    submit = SubmitField("Sign Up")
    
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[InputRequired(), DataRequired()])
    submit = SubmitField("Login")

class ShitPostForm(FlaskForm):
    post = TextAreaField("What's on your mind?", validators=[InputRequired()])
    submit = SubmitField("Post")
    
class CommentForm(FlaskForm):
    comment = TextAreaField("Say something about this shit.", validators=[InputRequired()])
    submit = SubmitField("Comment")