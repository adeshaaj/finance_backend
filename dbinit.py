import os

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "finance.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)
class Users(db.Model):
    __tablename__ = "Usersdata"
 
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String)
    password = db.Column(db.String)
    occupation = db.Column(db.String)
    age = db.Column(db.String)
    pin=db.Column(db.String)
    email=db.Column(db.String)
    gender=db.Column(db.String)
    phone=db.Column(db.String)
#db.init_app(app)
#db.create_all()

    
 
 
# create tables
#Base.metadata.create_all(engine)