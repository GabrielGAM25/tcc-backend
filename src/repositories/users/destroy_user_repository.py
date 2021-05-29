from config.database import db
from models import User
from factories import UserFactory

from .errors import UserNotFound


class DestroyUserRepository:
    def __init__(self, factory=UserFactory):
        self.factory = factory

    def delete_user(self, user_id):
        deleted_user = User.query.filter_by(id=user_id).delete()

        if not deleted_user:
            raise UserNotFound
        db.session.commit()
