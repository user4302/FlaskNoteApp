from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash # password hashing
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) # 'method' gives the ability to accept GET and POST requests
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first() # when querying a specific item
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully!', category='success')
                login_user(user, remember=True) # saves user session in the flask server to maintain the login/out status
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password, try Again', category='error')
        else:
                flash('Email does not exist', category='error')

    return render_template("login.html", user=current_user) # 2nd+ argument can be passed to the html file to be used in jinja syntax

@auth.route('/logout')
@login_required
def logout():
    logout_user() # simply logs out the current user
    return redirect(url_for('auth.login'))
    
@auth.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        # getting the data within the form as an 'ImmutableMultiDict' Object 
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        # flashes a notification banner if any of the following are true
        if user:
            flash('Email Already Exists', category='error')
        elif len(email) < 4:
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

            login_user(new_user, remember=True)
            flash('Account Created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("register.html", user=current_user)