from colorama import Fore, Style

from config.database import db
from config.bcrypt import generate_password_hash
from models import User


def run():
    print(f"{Fore.MAGENTA}Create users{Style.RESET_ALL}\t\t", end='')

    users = [
        User(
            name="Felipe Gonçalves",
            email="dpgoncalves.felipe@gmail.com",
            password=generate_password_hash("123456"),
            birth_date="2000-06-12",
        ),
        User(
            name="Jamal Marques",
            email="amarques.gabriel@gmail.com",
            password=generate_password_hash("123456"),
            birth_date="2001-04-25",
        ),
        User(
            name="Tomatinho Rodrigues",
            email="tomatinho@pullum.com",
            password=generate_password_hash("123456"),
            birth_date="2000-09-12",
        ),
        User(
            name="Matheus Quintão",
            email="matheus@pullum.com",
            password=generate_password_hash("123456"),
            birth_date="2000-09-12",
        ),
        User(
            name="Augusto Carvalho",
            email="augusto@pullum.com",
            password=generate_password_hash("123456"),
            birth_date="2000-11-24",
        ),
        User(
            name="Victor Hugo Faria Dias Magalhães",
            email="torugo@pullum.com",
            password=generate_password_hash("123456"),
            birth_date="2000-10-16",
        ),
        User(
            name="Luck Araújo",
            email="luck@pullum.com",
            password=generate_password_hash("123456"),
            birth_date="2010-04-25",
        ),
        User(
            name="Célio do Churrasco",
            email="celio@pullum.com",
            password=generate_password_hash("123456"),
            birth_date="1971-06-28",
        ),
        User(
            name="Matheus Marques",
            email="marques@pullum.com",
            password=generate_password_hash("123456"),
            birth_date="1999-12-03",
        ),
        User(
            name="Gabriela Ciríaco",
            email="gabriela@pullum.com",
            password=generate_password_hash("123456"),
            birth_date="2012-06-05",
        ),
    ]

    db.session.bulk_save_objects(users)
    db.session.commit()

    print(f"{Fore.GREEN}[DONE]{Style.RESET_ALL}")
