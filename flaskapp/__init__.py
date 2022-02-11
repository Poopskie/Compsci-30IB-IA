#-------------------------------------
#  Initials: JC
#  Program:  __init__.py
#  Class:    Compsci 30-IB
#  Function: Webapp Backend
# ------------------------------------
# Powershell launch webapp with: flask run in virtual environment

# Currently In Debugging mode
# DEbugging PIN: 627-350-771
# Running on http://127.0.0.1:5000/
# CTRL+C to quit app

# basic modules from flask to use:
# Flask: basics, render_template: calls on html file, 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Database library

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # using 3 slashes for relative path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# linking sql database + Initializing with settings from "app"
db = SQLAlchemy(app) 

# secret key is used ----------------------------------------
app.config['SECRET_KEY'] = '9dad5ef9d72c5d4a60a8e6484a3ea272'

from flaskapp import routes # avoiding circular importation

