from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
bootstrap = Bootstrap()
db = SQLAlchemy()


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(config_options[config_name])

bootstrap.init_app(app)
db.init_app(app)
login_manager.init_app(app)
from app import views
