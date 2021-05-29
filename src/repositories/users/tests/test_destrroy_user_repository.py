import pytest
import unittest

from config.conftest import app
from models import User
from repositories.users.errors import UserNotFound

from .. import DestroyUserRepository


repository = DestroyUserRepository()


@pytest.mark.usefixtures('app')
class TestDestroyUserRepository(unittest.TestCase):
    def should_raise_when_user_is_not_found(self):
        with pytest.raises(UserNotFound):
            repository.delete_user(0)

    def should_delete_the_user(self):
        User.create()
        repository.delete_user(user.id)
