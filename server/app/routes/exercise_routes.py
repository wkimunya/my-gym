# app/routes/exercise_routes.py

from flask import Blueprint, jsonify
from app.models.exercise import Exercise, db

exercise_bp = Blueprint('exercise_bp', __name__)

# Fetch all exercises
@exercise_bp.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify([{'id': exercise.id, 'name': exercise.name} for exercise in exercises])
