from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from datetime import datetime


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    blog = db.relationship("Blog", backref="user", lazy="dynamic")
    comments = db.relationship('Comment', backref='user', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.uname}'


# class Blog(db.Model):
#     __tablename__ = 'blog'
#
#     id = db.Column(db.Integer, primary_key = True)
#     title = db.Column(db.String(255))
#     content = db.Column(db.String(255))
#     date_posted = db.Column(db.DateTime,default=datetime.utcnow)
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
#     comment_id = db.relationship("Comments", backref = "blog", lazy = "dynamic")
#
#     def save_blog(self):
#         '''
#         Function that saves Blog
#         '''
#
#         db.session.add(self)
#         db.session.commit()
#
#     @classmethod
#     def get_blog(cls):
#         '''
#         Function that returns all the data from blog after being queried
#         '''
#         blog = Blog.query.order_by(Blog.id.desc()).all()
#         return blog
#
#     @classmethod
#     def delete_blog(cls):
#         '''
#         Functions the deletes a blog post
#         '''
#         blog = Blog.query.filter_by(id=blog_id).delete()
#         comment = Comments.query.filter_by(blog_id=blog_id).delete()


# class Comments(db.Model):
#     '''
#     comment class that creates new comments from users
#     '''
#     __tablename__ = 'comment'
#
#     id = db.Column(db. Integer,primary_key = True)
#     comment_section = db.Column(db.String(255))
#     author = db.Column(db.String(255))
#     date_posted = db.Column(db.DateTime,default=datetime.utcnow)
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
#     blog_id = db.Column(db.Integer,db.ForeignKey("blog.id"))
#
#     def save_comment(self):
#         '''
#         save the comments per blog
#         '''
#         db.session.add(self)
#         db.session.commit()
#
#     @classmethod
#     def get_comments(self,id):
#         comment = Comments.query.filter_by(blog_id=id).all()
#         return comment
#
#     @classmethod
#     def delete_comment(cls,comment_id):
#         '''
#         Function that delete a simgle comment in a blog post
#         '''
#         comment = Comments.query.filter_by(id=comment_id).delete()
#         db.session.commit()


class Role(db.Model):

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'
