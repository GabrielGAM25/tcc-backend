from colorama import Fore, Style

from config.database import db
from config.bcrypt import generate_password_hash
from model.user import User


def seed_users():
    print(f"{Fore.MAGENTA}Create users{Style.RESET_ALL}\t", end='')

    users = [
        User(
            name="Felipe",
            email="dpgoncalves.felipe@gmail.com",
            password=generate_password_hash("123456"),
            birth_date="2000-06-12",
        ),
        User(
            name="Jamal",
            email="amarques.gabriel@gmail.com",
            password=generate_password_hash("123456"),
            birth_date="2001-04-25",
        )
    ]

    db.session.bulk_save_objects(users)
    db.session.commit()

    print(f"{Fore.GREEN}[DONE]{Style.RESET_ALL}")
