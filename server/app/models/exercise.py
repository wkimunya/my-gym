# app/models/exercise.py

from app.extensions import db

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    # Add other exercise details
