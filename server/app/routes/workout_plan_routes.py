from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from app.models.workout_plan import WorkoutPlan
from app.extensions import db

workout_plan_bp = Blueprint('workout_plan_bp', __name__)
CORS(workout_plan_bp)  # Enable CORS for workout_plan_bp Blueprint

# Handle OPTIONS request for /workout-plans
@workout_plan_bp.route('/workout-plans', methods=['OPTIONS'])
@cross_origin()
def handle_options():
    return jsonify({'message': 'OK'}), 200

# Fetch all workout plans
@workout_plan_bp.route('/workout-plans', methods=['GET'])
def get_workout_plans():
    workout_plans = WorkoutPlan.query.all()
    return jsonify([plan.to_dict() for plan in workout_plans])

# Create a new workout plan
@workout_plan_bp.route('/workout-plans', methods=['POST'])
def create_workout_plan():
    data = request.get_json()
    print("Received data:", data)

    # member_name = data.get('member_name')  # Update to member_name
    trainer_id = data.get('trainer_id')
    exercise_id = data.get('exercise_id')
    time = data.get('time')
    day = data.get('day')

    if not trainer_id or not exercise_id or not time or not day:
        return jsonify({'error': 'Missing required fields'}), 400

    new_plan = WorkoutPlan(
        # member_name=member_name,
        trainer_id=trainer_id,
        exercise_id=exercise_id,
        time=time,
        day=day
    )

    db.session.add(new_plan)
    db.session.commit()

    return jsonify({'message': 'Workout plan created successfully'}), 201

# Update a workout plan
@workout_plan_bp.route('/workout-plans/<int:plan_id>', methods=['PUT'])
def update_workout_plan(plan_id):
    data = request.get_json()

    time = data.get('time')
    day = data.get('day')

    if not time or not day:
        return jsonify({'error': 'Missing required fields'}), 400

    plan = WorkoutPlan.query.get(plan_id)

    if not plan:
        return jsonify({'error': 'Workout plan not found'}), 404

    plan.time = time
    plan.day = day

    db.session.commit()

    return jsonify({'message': 'Workout plan updated successfully'}), 200

# Delete a workout plan
@workout_plan_bp.route('/workout-plans/<int:plan_id>', methods=['DELETE'])
def delete_workout_plan(plan_id):
    plan = WorkoutPlan.query.get(plan_id)

    if not plan:
        return jsonify({'error': 'Workout plan not found'}), 404

    db.session.delete(plan)
    db.session.commit()

    return jsonify({'message': 'Workout plan deleted successfully'}), 200
