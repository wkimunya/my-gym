# app/create_tables.py

from .extensions import db
from .models.member import Member
from .models.trainer import Trainer
from .models.exercise import Exercise
from .models.workout_plan import WorkoutPlan

# Create tables
db.create_all()
