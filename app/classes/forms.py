# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    role = SelectField('Role', choices=[("Teacher","Teacher"),("Student","Student")])
    age = SelectField('Age', choices=[(17, 17,),(18,18),("old","old")])

class BlogForm(FlaskForm):
    #curr working on
    image = FileField("Image")
    size = SelectField("Size", choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])

    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Blog')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    rating = SelectField('Rating', choices=[('Good',"Good"),('OK','OK'),('Bad','Bad')])
    submit = SubmitField('Comment')

class ClothingForm(FlaskForm):
    color = SelectField('Color', choices=[('White','White'),('Black','Black'),('Red','Red')])
    size = SelectField('Size', choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])
    submit = SubmitField('Add')

class EventForm(FlaskForm): 
    day = StringField('Day', validators=[DataRequired()])
    time = StringField('Time', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')