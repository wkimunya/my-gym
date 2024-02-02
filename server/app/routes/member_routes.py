from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.member import Member, db

member_bp = Blueprint('member_bp', __name__)

# Fetch all members
@member_bp.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    return jsonify([{'id': member.id, 'name': member.name} for member in members])

# Sign up a new member
@member_bp.route('/members/signup', methods=['POST'])
def signup_member():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    existing_member = Member.query.filter_by(email=email).first()
    if existing_member:
        return jsonify({'error': 'Email is already in use'}), 400

    new_member = Member(name=name, email=email)
    new_member.set_password(password)

    db.session.add(new_member)
    db.session.commit()

    return jsonify({'message': 'Member registered successfully'}), 201

# Log in a member
@member_bp.route('/members/login', methods=['POST'])
def login_member():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400

    member = Member.query.filter_by(email=email).first()

    if not member or not member.check_password(password):
        return jsonify({'error': 'Invalid email or password'}), 401

    # Generate JWT token on successful login
    access_token = member.generate_auth_token()

    return jsonify({'access_token': access_token}), 200

# Protected route that requires authentication
@member_bp.route('/members/profile', methods=['GET'])
@jwt_required()
def get_member_profile():
    current_member_id = get_jwt_identity()
    member = Member.query.get(current_member_id)

    return jsonify({'id': member.id, 'name': member.name, 'email': member.email}), 200
