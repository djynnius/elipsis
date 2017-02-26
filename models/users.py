import os.path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#determining path to database
ipath = os.path
zpath = ipath.dirname(__file__)
zpath = ipath.split(zpath)
zpath = zpath[0]
ELIPSIS_DB = ipath.join(zpath, 'databases', 'app.db')

print 'sqlite:///' + ELIPSIS_DB

users_model = Flask("users_model") #register model
users_model.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///' + ELIPSIS_DB
users_model.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(users_model)
db.create_all()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.Text())
    created_at = db.Column(db.DateTime())
    db.create_all()

    def __init__(self):
        pass

    def __repr__(self):
        pass
