from dataclasses import dataclass
from config.database import db


@dataclass
class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'),
        primary_key=True
    )
    date = db.Column(db.Date, nullable=False)
    weight = db.Column(db.Numeric(5, 2), nullable=False)
    fat_percentage = db.Column(db.Numeric(5, 2), nullable=False)
    neck = db.Column(db.Numeric(6, 2), nullable=False)
    shoulder = db.Column(db.Numeric(6, 2), nullable=False)
    torax = db.Column(db.Numeric(6, 2), nullable=False)
    abdomen = db.Column(db.Numeric(6, 2), nullable=False)
    waist = db.Column(db.Numeric(6, 2), nullable=False)
    hip = db.Column(db.Numeric(6, 2), nullable=False)
    left_arm = db.Column(db.Numeric(6, 2), nullable=False)
    right_arm = db.Column(db.Numeric(6, 2), nullable=False)
    left_forearm = db.Column(db.Numeric(6, 2), nullable=False)
    right_forearm = db.Column(db.Numeric(6, 2), nullable=False)
    left_thigh = db.Column(db.Numeric(6, 2), nullable=False)
    right_thigh = db.Column(db.Numeric(6, 2), nullable=False)
    left_calf = db.Column(db.Numeric(6, 2), nullable=False)
    right_calf = db.Column(db.Numeric(6, 2), nullable=False)

    user = db.relationship('User', foreign_keys=user_id)
