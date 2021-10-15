# the views/url endpoints of the frontend of the website
# This file is a "blueprint" of this application

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html") # will render the template on the page when the route is accessed