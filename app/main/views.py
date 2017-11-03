from flask import render_tenplate
from app import app
from flask_login import login_required
# Views


@main.route('/')
def index():
    '''
    view root page
    '''

    return render_tenplate('index.html')


@main.route('blog/comment/new<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    blog = get_blog(id)

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        new_comment = Comment(blog.id, title, comment)
        new_comment.save_comment()
        return redirect(url_for('blog', id=blog.id))

    # title = f'{category.name} comment'
    return render_template('new_comment.html', title=title, comment_form=form, blog=blog)
