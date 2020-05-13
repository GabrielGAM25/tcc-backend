import os
import sys
from colorama import Fore, Style
from dotenv import load_dotenv


load_dotenv()

available_options = [
    "seed_db",
    "clear_db",
]

chosen_option = sys.argv[1]


def print_help():
    print(
        f'\nCorrect usage:\t{Fore.LIGHTBLUE_EX}python app [OPTION]{Style.RESET_ALL}'
    )

    print(
        f'Possible values for OPTION:\t{Fore.LIGHTBLUE_EX}{available_options}{Style.RESET_ALL}'
    )


if chosen_option == '--help':
    print_help()
    sys.exit()

if chosen_option not in available_options:
    print(f'{Fore.RED}Invalid option!{Style.RESET_ALL}')
    print_help()
else:
    os.system(f'python src/app.py {chosen_option}')
