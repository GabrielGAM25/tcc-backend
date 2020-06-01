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
            'weight': float(self.weight),
            'fat_percentage': float(self.fat_percentage),
            'neck': float(self.neck),
            'shoulder': float(self.shoulder),
            'torax': float(self.torax),
            'abdomen': float(self.abdomen),
            'waist': float(self.waist),
            'hip': float(self.hip),
            'left_arm': float(self.left_arm),
            'right_arm': float(self.right_arm),
            'left_forearm': float(self.left_forearm),
            'right_forearm': float(self.right_forearm),
            'left_thigh': float(self.left_thigh),
            'right_thigh': float(self.right_thigh),
            'left_calf': float(self.left_calf),
            'right_calf': float(self.right_calf),
        }
