# store database models

from . import db # the dot (.) referst to the package (website)
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin): # UserMixin is used to access the current user's info
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # everytime a note is created, add the note.id to this field. Uppercase like the class name
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # foreign key is lowercase