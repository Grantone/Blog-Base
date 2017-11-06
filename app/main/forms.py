from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms.validators import Required


class BlogForm(FlaskForm):

    title = StringField('Blog Title', validators=[Required()])
    content = TextAreaField('Type Blog', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment_section = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')
