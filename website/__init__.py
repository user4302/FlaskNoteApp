# makes the website folder into a python package
# when importing the website folder, the commands in this file will be run

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) # initialize app
    app.config['SECRET_KEY'] = '^R795wEm#Y!$jzS8#*9%3pu*ob6sockA$^f4N7mNK2%J9K2C7ZWZb@9@WU5Nd553' #used to encrypt session cookies
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # location of the database
    db.init_app(app) # point db at the app that it wil connect with 
    
    # importing the blueprints
    from .views import views 
    from .auth import auth

    # registering the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note # load file and make the database
    create_database(app) # 'app' will tell sqlalchemy what app werecreating the db for

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # where flask will redirect if user is not logged in
    login_manager.init_app(app) # tell login manager which app to use

    @login_manager.user_loader # tell flask how to load th user
    def load_user(id):
        return User.query.get(int(id)) # looks for primary key by default and checks what is passed to it

    return app 

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Database Created')