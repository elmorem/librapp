from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from books import db 


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(128))
    title = db.Column(db.String(256))