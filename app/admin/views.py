from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user

from ..models import User
from .forms import BlogForm, CommentForm
from . import admin
from ..models import Blog, Comments

from .. import db


def check_user():

    if current_user.id != 1:
        abort(404)

    return render_template('admin/dashboard.html')


@admin.route('/blog/new', methods=['GET', 'POST'])
def new_blog():

    form = BlogForm()

    if form.validate_on_submit():

        title = form.title.data
        description = form.description.data
        blog = form.blog.data

        new_blog = Blog(blog=blog, title=title, description=description)

        new_blog.save_blog()

        return redirect(url_for('main.index'))

    return render_template('new_blog.html', blog_form=form)


@admin.route('/delete/blog/<int:id>', methods=['GET', 'POST'])
def delete_blog(id):

    blog = Blog.delete_blog(id)

    return redirect(url_for('main.index'))


@admin.route('/delete/comment/<int:id>', methods=['GET', 'POST'])
def delete_review(id):

    comment = Comment.delete_blog(id)

    return redirect(url_for('.single_blog'))


@admin.route('/edit/blog/<int:id>', methods=['GET', 'POST'])
def edit_blog(id):

    edit = Comment.delete_blog(id)

    return redirect(url_for('.single_blog'))
