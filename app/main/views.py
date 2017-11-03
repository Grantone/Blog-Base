from flask import render_tenplate
from app import app

# Views


@main.route('/')
def index():
    '''
    view root page
    '''

    return render_tenplate('index.html')
