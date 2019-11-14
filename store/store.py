""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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
    menu_title = "Store module"
    exit_message = "Back to main menu"
    ui.print_menu(menu_title, options, exit_message)


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "0":
        return False
    elif option == "1":
        list_of_games = []
        with open("store/games.csv") as file:
            for line in file:
                list_of_games.append(line.strip('\n'))
        show_table(list_of_games)
    elif option == "2":
        list_of_games = []
        with open("store/games.csv") as file:
            for line in file:
                list_of_games.append(line.strip('\n'))
        add(list_of_games)
    elif option == "3":
        list_of_games = []
        with open("store/games.csv") as file:
            for line in file:
                list_of_games.append(line.strip('\n'))
        remove(list_of_games, input("Please enter an id of a record to be removed: "))
    elif option == "4":
        list_of_games = []
        with open("store/games.csv") as file:
            for line in file:
                list_of_games.append(line.strip('\n'))
        update(list_of_games, input("Please enter an id of a record to update: "))
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
    ui.print_table(table, ["id", "title", "manufacturer", "price", "in stock"])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    # your code

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

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """
    table_index = 0
    for row in table:
        row = row.split(";")
        if id_ == row[0]:
            with open("store/games.csv", "r+") as file:
                for i in range(len(row)):
                    user_input = input(f"Do you want to change this record ({row[i]})? [y/n] ")
                    if user_input == "y":
                        row[i] = input("New record: ")
                    elif user_input == "n":
                        continue
                table[table_index] = ';'.join(row)
                for element in table:
                    file.write(f"{element}\n")
        table_index += 1
                    
    show_table(table)
    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
