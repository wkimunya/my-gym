# app/routes/trainer_routes.py
from flask import Blueprint, jsonify
from app.models.trainer import Trainer
from app.extensions import db

trainer_bp = Blueprint('trainer_bp', __name__)

# Fetch all trainers
@trainer_bp.route('/trainers', methods=['GET'])
def get_trainers():
    trainers = Trainer.query.all()
    return jsonify([{'id': trainer.id, 'name': trainer.name} for trainer in trainers])
