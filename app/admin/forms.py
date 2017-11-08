from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class BlogForm(FlaskForm):

    title = StringField('Blog Title', validators=[Required()])

    description = StringField('Blog Description', validators=[Required()])

    blog = TextAreaField('Blog')

    submit = SubmitField('Submit')


class EditBlog(FlaskForm):
    submit = SubmitField('Edit Blog')


class DeleteBlog(FlaskForm):
    submit = SubmitField('Delete Blog')


class DeleteComment(FlaskForm):
    submit = SubmitField('Delete Comment')


class CommentForm(FlaskForm):
    comment = TextAreaField('Blog Comment')
    submit = SubmitField('Submit')
