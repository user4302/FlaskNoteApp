from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash # password hashing
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) # 'method' gives the ability to accept GET and POST requests
def login():
    return render_template("login.html", boolean=True) # 2nd+ argument can be passed to the html file to be used in jinja syntax

@auth.route('/logout')
def logout():
    return render_template("logout.html")
    
@auth.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        # getting the data within the form as an 'ImmutableMultiDict' Object 
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # flashes a notification banner if any of the following are true
        if len(email) < 4:
            flash('email must be greater than 4 characters', category='error')
        elif len(first_name) <2:
            flash('First Name must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256')) # creation of new user
            db.session.add(new_user) # add new user to database
            db.session.commit() # update database with changes

            flash('Account Created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("register.html")