# app/run.py

from app import create_app, db
from app.models.exercise import Exercise
from app.models.trainer import Trainer

app = create_app()

# Print debug information
print("Before app context")

with app.app_context():
    print("Inside app context")
    
    # Create all database tables
    db.create_all()

    # Add exercises to the database
    exercises_data = [
        {"name": "cycling"},
        {"name": "Body Building"},
        {"name": "Fitness"},
        {"name": "Running"},
        {"name": "Power Lifting"},
        {"name": "Boxing"},
        {"name": "Yoga"},
        {"name": "Crossfit"},
        {"name": "Karate"},
        {"name": "Meditation"},
    ]

    for exercise_info in exercises_data:
        exercise = Exercise(**exercise_info)
        db.session.add(exercise)

    # Add trainers to the database
    trainers_data = [
        {"name": "David Vila"},
        {"name": "John Weights"},
        {"name": "Junifor Jonas 3"},
        {"name": "Robert Louis"},
        {"name": "Mike Tyson"},
        {"name": "Mia Kha"},
        {"name": "Cristofer Columbo"},
        {"name": "Tom Rizzly"},
        # Add more trainers as needed
    ]

    for trainer_info in trainers_data:
        trainer = Trainer(**trainer_info)
        db.session.add(trainer)

    # Commit changes to the database
    db.session.commit()
