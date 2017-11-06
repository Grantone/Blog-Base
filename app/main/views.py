from flask import render_template, redirect, url_for, abort
from .. import db
from . import main
from flask_login import login_required, current_user
from .forms import BlogForm, CommentForm
from ..models import User, Role


@main.route('/')
def index():
    '''
    view root page
    '''

    blog = BlogForm()
    title = 'Home - Welcome to Blog Base'
    return render_template('index.html', title=title, blog=blog)


@main.route('/blog/<int:blog_id>')
def blogs(id):
    '''
    View blog page function
    '''

    return render_template('blog.html', id=id)


@main.route('/blog/comment/new<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):

    blog = Blog.query.filter_by(id=id).first()

    if blog is None:
        abort(404)
    form = CommentForm()

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        new_comment = Comments(blog.id, title, comment)
        new_comment.save_comment()
        return redirect(url_for('blog', id=blog.id))

    # title = f'{category.name} comment'
    return render_template('new_comment.html', title=title, comment_form=form, blog=blog)
