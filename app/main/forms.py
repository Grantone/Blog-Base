from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class CommentForm(FlaskForm):

    title = StringField('Comment title', validators=[Required()])
    comment = TextAreaField('Category comment', validators=[Required()])
    submit = SubmitField('Submit')
