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
    bio = StringField('Add Bio', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    role = SelectField('Role', choices=[("Teacher","Teacher"),("Student","Student")])
    age = SelectField('Age', choices=[("Freshman", "Freshman",),("Sophomore","Sophomore"),("Junior","Junior"),("Senior","Senior"),("Teacher","Teacher")])
    ##age = SelectField('Age', choices=[(17,17),(18,18),("old","old")])
    
class BlogForm(FlaskForm):
    #curr working on
    image = FileField("Image")
    color = SelectField("Color", choices=[('Red','Red'),('Orange','Orange'),('Yellow','Yellow'),('Green','Green')])
    length = SelectField("Length", choices=[('Short', 'Short'),('Regular','Regular'),('Long','Long')])
    quality = SelectField("Quality", choices=[('Bad', 'Bad'),('OK','OK'),('Good','Good'),('New','New')])
    sale = SelectField("Swap or Giveaway", choices=[('Swap','Swap'),('Give away','Give away')])
    style = StringField('Style', validators=[DataRequired()])
    clothingsize = SelectField("Size", choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Describe the clothing and include your email', validators=[DataRequired()])
    tag = StringField('Brand', validators=[DataRequired()])
    submit = SubmitField('Enter')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    rating = SelectField('Rating', choices=[('1-Good',"1-Good"),('2-OK','2-OK'),('3-Bad','3-Bad')])
    reserve = SelectField('Reserve', choices=[('Reserve', 'Reserve'),('Thinking about it','Thinking about it')])
    submit = SubmitField('Comment')


class ClothingForm(FlaskForm):
    color = SelectField('Color', choices=[('White','White'),('Black','Black'),('Red','Red')])
    size = SelectField('Size', choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])
    submit = SubmitField('Add')

class EventForm(FlaskForm): 
    image = FileField("Image")
    day = StringField('Day', validators=[DataRequired()])
    time = StringField('Time', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class eventcommentForm(FlaskForm):
    attending = SelectField('Will you be attending?', choices=[("Yes, I'm coming!", "Yes, I'm coming!"),("Next time","Next time")])
    submit = SubmitField('Submit')