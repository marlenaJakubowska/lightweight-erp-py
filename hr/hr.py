""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def handle_menu():
    options = ["Show all", "Add", "Remove", "Update"]
    menu_title = "Human resources manager"
    exit_message = "Back to main menu"
    ui.print_menu(menu_title, options, exit_message)


def choose():
    table = data_manager.get_table_from_file("hr/persons.csv")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "0":
        return False
    elif option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        id_ = ui.get_inputs(["Please enter an ID: "], "")
        remove(table, id_)
    elif option == "4":
        id_ = ui.get_inputs(["Please enter an ID of a record to update: "], "")
        update(table, id_)

    start_module()
        


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    is_running = True
    while is_running:
        handle_menu()
        try:
            is_running = choose()
        except KeyError as err:
            ui.print_error_message(str(err))


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    ui.print_table(table, ["id", "name", "birth_year"])  #, "price", "in stock"])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    unique_id = common.generate_random(table)
    inputs = ui.get_inputs(["Enter name: ", "Enter birth_year: "], "")
    with open("hr/persons.csv", "a") as file:
        file.write(f"{unique_id};{';'.join(inputs)}\n")

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    for row in table:
        if id_[0] == row[0]:
            inputs = ui.get_inputs([f"Do you want to delete this record ({' | '.join(row)})? [y/n] "], "")
            if inputs[0].lower() == "y":
                table.remove(row)
            else:
                continue

    data_manager.write_table_to_file("hr/persons.csv", table)
    
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """
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

    data_manager.write_table_to_file("hr/persons.csv", table)
    show_table(table)

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
