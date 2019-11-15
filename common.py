""" Common module
implement commonly used functions here
"""

import random
import data_manager
import ui


def add(file, table, inputs):
    unique_id = generate_random(table)
    inputs = ui.get_inputs(inputs, "")
    with open(file, "a") as file:
        file.write(f"{unique_id};{';'.join(inputs)}\n")
    return table


def remove(file, table, id_):
    for row in table:
        if id_[0] == row[0]:
            inputs = ui.get_inputs([f"Do you want to delete this record ({' | '.join(row)})? [y/n] "], "")
            if inputs[0].lower() == "y":
                table.remove(row)
            else:
                continue
    data_manager.write_table_to_file(file, table)


def update(file, table, id_):
    table_index = 0
    for row in table:
        if id_[0] == row[0]:
            for i in range(len(row)):
                user_input = ''.join(ui.get_inputs([f"({row[i]}) Write new record or press 'Enter' to continue "], ""))
                if user_input == "":
                    continue
                else:
                    row[i] = user_input
                table[table_index] = row
        table_index += 1
    data_manager.write_table_to_file(file, table)


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
