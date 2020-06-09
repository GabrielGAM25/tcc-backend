from dataclasses import dataclass
from config.database import db


@dataclass
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)

    @classmethod
    def from_entity(cls, entity):
        return cls(
            id_=entity.id,
            name=entity.name,
            email=entity.email,
            password=entity.password,
            birth_date=entity.birth_date,
        )
