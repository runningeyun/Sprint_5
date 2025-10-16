import random


class AccountData:

    existing_user = {
        'email': 'Aleksandr_Alekseev33main@ya.ru',
        'password': '1234567'
    }
    new_correct_user = {
        'name': 'Aleksandr',
        'email': f'Aleksandr_Alekseev_33_{random.randint(100, 999)}@ya.ru',
        'password': str(random.randint(100000, 999999))
    }
