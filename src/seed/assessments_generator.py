import random
from colorama import Fore, Style
from sqlalchemy.sql import not_

from config.database import db
from utils.random import random_date
from utils.date import date_string_to_date, add_months
from model import User, Assessment


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
            weight=80.1,
            fat_percentage=22.3,
            neck=36.2,
            shoulder=41.1,
            torax=102.8,
            abdomen=95.3,
            waist=97.4,
            hip=98.1,
            left_arm=31.2,
            right_arm=31.4,
            left_forearm=26.2,
            right_forearm=26.8,
            left_thigh=62.1,
            right_thigh=62.0,
            left_calf=38.0,
            right_calf=38.0,
        ),
        Assessment(
            user_id=felipe_id,
            date='2020-01-10',
            weight=84.2,
            fat_percentage=18.2,
            neck=36.4,
            shoulder=41.5,
            torax=103.2,
            abdomen=93.3,
            waist=94.4,
            hip=97.1,
            left_arm=33.0,
            right_arm=32.9,
            left_forearm=27.1,
            right_forearm=27.4,
            left_thigh=64.0,
            right_thigh=64.2,
            left_calf=40.2,
            right_calf=39.9,
        ),
        Assessment(
            user_id=jamal_id,
            date='2019-12-14',
            weight=68.4,
            fat_percentage=16.0,
            neck=33.2,
            shoulder=40.1,
            torax=100.2,
            abdomen=90.7,
            waist=92.1,
            hip=95.0,
            left_arm=30.6,
            right_arm=30.4,
            left_forearm=25.1,
            right_forearm=24.9,
            left_thigh=60.0,
            right_thigh=59.8,
            left_calf=35.7,
            right_calf=35.2,
        ),
        Assessment(
            user_id=jamal_id,
            date='2020-03-06',
            weight=70.5,
            fat_percentage=15.2,
            neck=33.5,
            shoulder=40.5,
            torax=100.8,
            abdomen=90.9,
            waist=91.9,
            hip=95.3,
            left_arm=31.8,
            right_arm=31.5,
            left_forearm=25.8,
            right_forearm=25.7,
            left_thigh=61.2,
            right_thigh=60.9,
            left_calf=36.6,
            right_calf=36.5,
        ),
    ]

    for user_id in db.session.query(User.id).filter(not_(User.id.in_([felipe_id, jamal_id]))):
        first_assessment_date = random_date(
            date_string_to_date('2019-01-01'),
            date_string_to_date('2020-05-10')
        )
        second_assessment_date = random_date(
            add_months(first_assessment_date, 1),
            date_string_to_date('2020-05-13')
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
