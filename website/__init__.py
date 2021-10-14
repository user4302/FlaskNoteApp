# makes the website folder into a python package
# when importing the website folder, the commands in this file will be run

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '^R795wEm#Y!$jzS8#*9%3pu*ob6huhmA$^f4N7mNK2%J9K2C7ZWZb@9@WU5Nd553'
    return app