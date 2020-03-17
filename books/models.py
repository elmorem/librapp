from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Book(db.Model):
    id = db.co