# the views/url endpoints of the frontend of the website
# we define in this file that this file is a "blueprint" of this application

from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>FlaskNoteApp Home Page</h1>"