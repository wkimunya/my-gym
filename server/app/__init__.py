from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .config import Config
from .extensions import db  # Assuming extensions.py is in the same directory

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configure CORS with allowed headers
    CORS(app, supports_credentials=True, allow_headers=["Content-Type", "Authorization"])

    # Initialize extensions
    db.init_app(app)
    jwt = JWTManager(app)

    # Register blueprints (routes)
    from .routes.member_routes import member_bp
    from .routes.trainer_routes import trainer_bp
    from .routes.exercise_routes import exercise_bp
    from .routes.workout_plan_routes import workout_plan_bp

    app.register_blueprint(member_bp)
    app.register_blueprint(trainer_bp)
    app.register_blueprint(exercise_bp)
    app.register_blueprint(workout_plan_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
