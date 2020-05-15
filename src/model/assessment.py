from dataclasses import dataclass
from config.database import db


@dataclass
class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    date = db.Column(db.Date)
    weight = db.Column(db.Numeric(5,2))
    fat_percentage = db.Column(db.Numeric(5,2))
    neck = db.Column(db.Numeric(6,2))
    shoulder = db.Column(db.Numeric(6,2))
    torax = db.Column(db.Numeric(6,2))
    abdomen = db.Column(db.Numeric(6,2))
    waist = db.Column(db.Numeric(6,2))
    hip = db.Column(db.Numeric(6,2))
    left_arm = db.Column(db.Numeric(6,2))
    right_arm = db.Column(db.Numeric(6,2))
    left_forearm = db.Column(db.Numeric(6,2))
    right_forearm = db.Column(db.Numeric(6,2))
    left_thigh = db.Column(db.Numeric(6,2))
    right_thigh = db.Column(db.Numeric(6,2))
    left_calf = db.Column(db.Numeric(6,2))
    right_calf = db.Column(db.Numeric(6,2))

    user = db.relationship('User', foreign_keys=user_id)

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'date': self.date,
            'weight': self.weight,
            'fat_percentage': self.fat_percentage,
            'neck': self.neck,
            'shoulder': self.shoulder,
            'torax': self.torax,
            'abdomen': self.abdomen,
            'waist': self.waist,
            'hip': self.hip,
            'left_arm': self.left_arm,
            'right_arm': self.right_arm,
            'left_forearm': self.left_forearm,
            'right_forearm': self.right_forearm,
            'left_thigh': self.left_thigh,
            'right_thigh': self.right_thigh,
            'left_calf': self.left_calf,
            'right_calf': self.right_calf,
        }
