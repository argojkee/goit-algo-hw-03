from datetime import datetime, timedelta
import random
import re

#! Exercise 1
def get_days_from_today(date: str) -> int:
    try:
        today = datetime.now()
        converted_date = datetime.strptime(date, '%Y-%m-%d')
        return (today - converted_date).days
    except ValueError:
        print('Bad string format! Please, enter string with format YYYY-MM-DD')
    except TypeError:
        print('Data should be string with format YYYY-MM-DD')


#! Exercise 2
def get_numbers_ticket(min: int, max:int, quantity:int) -> list:
    try:
        random_values = random.sample(range(min, max), quantity)
        random_values.sort()
        return random_values
    except TypeError:
        print('Minimal value, maximum value and quantity should be integer')
        return []
    except ValueError:
        if max < min:
            print('Maximum value can\'t be less than minimum value')
        elif quantity > max - min:
            print('Difference with maximum and minimum values ca\'t be less than quantity')
        return []

#! Exercise 3

pattern = r'\D'
def normalize_phone(phone_number: str) -> str:
    just_numbers = re.sub(pattern, '', phone_number)
    is_start_with_code = not just_numbers[0] == '0'
    correct_phone_number = f'+{just_numbers}' if is_start_with_code else f'+38{just_numbers}'
    return correct_phone_number

#! Exercise 4

