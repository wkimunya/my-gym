import jwt
from flask import current_app, jsonify
from datetime import datetime, timedelta
from backend.app.models.member import User

def generate_jwt_token(user_id):
    expiration_time = datetime.utcnow() + timedelta(hours=current_app.config['JWT_EXPIRATION_HOURS'])
    token = jwt.encode({'user_id': user_id, 'exp': expiration_time}, current_app.config['SECRET_KEY'], algorithm='HS256')
    return token.decode('utf-8')

def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        user = User.query.get(payload['user_id'])
        return user
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401
