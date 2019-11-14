""" Common module
implement commonly used functions here
"""

import random


def create_id():
    letters = "qwertyuiopasdfghjklzxcvbnm"
    numbers = "1234567890"
    spec_char = "!@#$%^&?"

    id_el1 = "".join(random.sample(letters, 1)).lower()
    id_el2 = "".join(random.sample(letters, 1)).upper()
    id_el3 = "".join(random.sample(numbers, 2))
    id_el4 = "".join(random.sample(letters, 1)).upper()
    id_el5 = "".join(random.sample(letters, 1)).lower()
    id_el6 = "".join(random.sample(spec_char, 2))

    id = id_el1 + id_el2 + id_el3 + id_el4 + id_el5 + id_el6
    return id


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    id_index = 0
    generated_id = ''
    id_table = [line[id_index] for line in table]
    generated_id = create_id()
    if id in id_table:
        generate_random(table)
    
    return generated_id
