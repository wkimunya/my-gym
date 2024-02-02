from ..extensions import db

class WorkoutPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    time = db.Column(db.String(10))
    day = db.Column(db.String(10))

    def to_dict(self):
        return {
            'id': self.id,
            'trainer_id': self.trainer_id,
            'exercise_id': self.exercise_id,
            'time': self.time,
            'day': self.day
        }
