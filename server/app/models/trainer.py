# app/models/trainer.py
from app.extensions import db

class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    # Add other trainer details
