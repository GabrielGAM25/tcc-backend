from dataclasses import dataclass
from config.database import db


@dataclass
class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(), nullable=False)

    @classmethod
    def from_entity(cls, entity):
        return cls(
            id_=entity.id,
            name=entity.name,
            description=entity.description,
        )
