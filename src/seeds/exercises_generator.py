from colorama import Fore, Style

from config.database import db
from config.bcrypt import generate_password_hash
from models import Exercise


def run():
    print(f"{Fore.MAGENTA}Create exercises{Style.RESET_ALL}\t", end='')

    exercises = [
        Exercise(
            name="Supino",
            description="Faz o movimento pra empurrar pra frente a barra ou os halteres com os braços",
        ),
        Exercise(
            name="Agachamento",
            description="O nome fala por si só, você só precisa agachar",
        ),
        Exercise(
            name="Rosca direta",
            description="Com os halteres ou barra, dobre os braços de forma a forçar os bíceps",
        ),
        Exercise(
            name="Desenvolvimento",
            description='Faça o mesmo movimento de "dar de ombros"',
        ),
        Exercise(
            name="Augusto Carvalho",
            description="augusto@pullum.com",
        ),
        Exercise(
            name="Leg press",
            description="Empurre a plataforma do leg press",
        ),
        Exercise(
            name="Esteira",
            description="Sobe na esteira e corre",
        ),
        Exercise(
            name="Abdominal",
            description="Se você não sabe nem fazer um abdominal, você tá perdido",
        ),
        Exercise(
            name="Prancha",
            description="Deita no chão e fica apoiado no antebraço por um tempo",
        ),
        Exercise(
            name="Barra",
            description="Cara, isso aqui é o básico. Não é possível que você não sabe nem fazer uma barra",
        ),
    ]

    db.session.bulk_save_objects(exercises)
    db.session.commit()

    print(f"{Fore.GREEN}[DONE]{Style.RESET_ALL}")
