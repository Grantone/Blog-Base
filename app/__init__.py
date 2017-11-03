from flask import Blueprint
main = Blueprint('main', __name__)
from . import views, error
from flask import Flask


app = Flask(__name__)

from app import views
