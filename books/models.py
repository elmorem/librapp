from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from books import db 


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(128))
    title = db.Column(db.String(256))
    publisher= db.Column(db.String(128))
    pub_location= db.Column(db.String(128))
    pub_date= db.Column(db.Integer)

    def __init__(self, author, title, publisher, location, date):
        self.author=author
        self.title=title
        self.publisher=publisher
        self.pub_location=location
        self.pub_date=date   
