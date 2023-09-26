from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Email, URL

# Shit Posting Form
class ShitPostForm(FlaskForm):
    post = TextAreaField("What's on your shitty brain?", validators=[InputRequired(), DataRequired()])
    # Image Upload / Image URL
    # img_url = StringField("Shit image URL", validators=[URL, DataRequired()])
    submit = SubmitField("Post Shit")
    
# Sign Up form for shitheads
class SignupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email address", validators=[Email(), DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")
    
# Login form for the shitheads
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
    
# Comment form for the shitheads
class CommentForm(FlaskForm):
    comment = TextAreaField("Write a shit comment.", validators=[InputRequired(), DataRequired()])
    submit = SubmitField("Comment")