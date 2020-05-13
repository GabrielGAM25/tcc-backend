from colorama import Fore, Style

from config.database import db
from model.user import User

from .user import seed_users


def clear_database():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print(f"{Fore.MAGENTA}Clear table {table}{Style.RESET_ALL}\t", end='')

        db.session.execute(table.delete())

        print(f"{Fore.GREEN}[DONE]{Style.RESET_ALL}")
    db.session.commit()


def seed_database():
    seed_users()
