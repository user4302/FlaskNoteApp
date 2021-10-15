# the views/url endpoints of the frontend of the website
# This file is a "blueprint" of this application

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method =='POST':
        note = request.form.get('note')
        if len(note) <1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user) # will render the template on the page when the route is accessed

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data) # convert into a python dictionary object to access the noteId
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})