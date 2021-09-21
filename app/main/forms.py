from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import required, Required


class PitchForm(FlaskForm):
    title = StringField('pitch_title')
    text = TextAreaField('pitch_text')
    category = SelectField('pitch_type', choices=[('technology','Tech-Pitch'), ('travels', 'Travels-Pitch'),('sports', 'Sports-Pitch')])
    submit = SubmitField('submit')


class CommentForm(FlaskForm):
    text = TextAreaField('yoursay')
    submit = SubmitField('submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you',validators=[Required()])
    
    submit = SubmitField('Submit')
        