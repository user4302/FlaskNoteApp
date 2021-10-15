# the views/url endpoints of the frontend of the website
# we define in this file that this file is a "blueprint" of this application

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")