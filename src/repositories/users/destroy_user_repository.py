from config.database import db
from models import User
from factories import UserFactory 


class DestroyUserRepository:
    def __init__(self, factory=UserFactory):
        self.factory = factory

    def delete_user(self, user_id):
        User.query.filter_by(id=user_id).delete()
        db.session.commit()
