import random
from colorama import Fore, Style
from sqlalchemy.sql import not_

from config.database import db
from utils.random import random_date
from utils.date import date_string_to_date, add_months
from models import User, Assessment


def run():
    print(f"{Fore.MAGENTA}Create assessment{Style.RESET_ALL}\t", end='')

    felipe_id = User.query.with_entities(User.id).\
        filter_by(email='dpgoncalves.felipe@gmail.com').first()

    jamal_id = User.query.with_entities(User.id).\
        filter_by(email='amarques.gabriel@gmail.com').first()

    assessments = [
        Assessment(
            user_id=felipe_id,
            date='2019-10-07',
            weight=80.10,
            fat_percentage=22.30,
            neck=36.20,
            shoulder=41.10,
            torax=102.80,
            abdomen=95.30,
            waist=97.40,
            hip=98.10,
            left_arm=31.20,
            right_arm=31.40,
            left_forearm=26.20,
            right_forearm=26.80,
            left_thigh=62.10,
            right_thigh=62.00,
            left_calf=38.00,
            right_calf=38.00,
        ),
        Assessment(
            user_id=felipe_id,
            date='2020-01-10',
            weight=84.20,
            fat_percentage=18.20,
            neck=36.40,
            shoulder=41.50,
            torax=103.20,
            abdomen=93.30,
            waist=94.40,
            hip=97.10,
            left_arm=33.00,
            right_arm=32.90,
            left_forearm=27.10,
            right_forearm=27.40,
            left_thigh=64.00,
            right_thigh=64.20,
            left_calf=40.20,
            right_calf=39.90,
        ),
        Assessment(
            user_id=jamal_id,
            date='2019-12-14',
            weight=68.40,
            fat_percentage=16.00,
            neck=33.20,
            shoulder=40.10,
            torax=100.20,
            abdomen=90.70,
            waist=92.10,
            hip=95.00,
            left_arm=30.60,
            right_arm=30.40,
            left_forearm=25.10,
            right_forearm=24.90,
            left_thigh=60.00,
            right_thigh=59.80,
            left_calf=35.70,
            right_calf=35.20,
        ),
        Assessment(
            user_id=jamal_id,
            date='2020-03-06',
            weight=70.50,
            fat_percentage=15.20,
            neck=33.50,
            shoulder=40.50,
            torax=100.80,
            abdomen=90.90,
            waist=91.90,
            hip=95.30,
            left_arm=31.80,
            right_arm=31.50,
            left_forearm=25.80,
            right_forearm=25.70,
            left_thigh=61.20,
            right_thigh=60.90,
            left_calf=36.60,
            right_calf=36.50,
        ),
    ]

    for user_id in db.session.query(User.id).filter(not_(User.id.in_([felipe_id, jamal_id]))):
        first_assessment_date = random_date(
            date_string_to_date('2019-01-01'),
            date_string_to_date('2020-05-10')
        )
        second_assessment_date = random_date(
            add_months(first_assessment_date, 1),
            date_string_to_date('2020-06-13')
        )

        dates = [first_assessment_date, second_assessment_date]

        for i in range(2):
            arm = random.uniform(28, 42)
            forearm = random.uniform(22, 30)
            thigh = random.uniform(50, 70)
            calf = random.uniform(30, 40)

            assessments.append(
                Assessment(
                    user_id=user_id,
                    date=dates[i],
                    weight=random.uniform(65, 110),
                    fat_percentage=random.uniform(8, 25),
                    neck=random.uniform(30, 40),
                    shoulder=random.uniform(40, 50),
                    torax=random.uniform(90, 130),
                    abdomen=random.uniform(80, 100),
                    waist=random.uniform(80, 110),
                    hip=random.uniform(80, 110),
                    left_arm=arm,
                    right_arm=arm,
                    left_forearm=forearm,
                    right_forearm=forearm,
                    left_thigh=thigh,
                    right_thigh=thigh,
                    left_calf=calf,
                    right_calf=calf,
                ))

    db.session.bulk_save_objects(assessments)
    db.session.commit()

    print(f"{Fore.GREEN}[DONE]{Style.RESET_ALL}")
