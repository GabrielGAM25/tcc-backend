from colorama import Fore, Style

from config.database import db
from model.user import User

from . import users_generator, assessments_generator


def clear_database():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print(f"{Fore.MAGENTA}Clear table {table}{Style.RESET_ALL}\t", end='')

        db.session.execute(table.delete())
        db.session.execute(f'ALTER SEQUENCE {table}_id_seq RESTART WITH 1')

        print(f"{Fore.GREEN}[DONE]{Style.RESET_ALL}")
    db.session.commit()


def seed_database():
    users_generator.run()
    assessments_generator.run()
