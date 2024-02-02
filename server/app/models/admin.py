# app/models/admin.py

from ..extensions import db

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add other admin details

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    # Add other member details
