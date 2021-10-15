from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return render_template("logout.html")
    
@auth.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")