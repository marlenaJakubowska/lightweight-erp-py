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
    options = ["Show all", "Add", "Remove", "Update", "Show manufacturers"]
    menu_title = "Store module"
    exit_message = "Back to main menu"
    ui.print_menu(menu_title, options, exit_message)


def choose():
    table = data_manager.get_table_from_file("store/games.csv")
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
    elif option == "5":
        get_counts_by_manufacturers(data_manager.get_table_from_file("store/games.csv"))

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
    common.add("store/games.csv", table, ["Title of the game: ", "Manufacturer: ", "Price: ", "In stock: "])
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
    common.remove("store/games.csv", table, id_)
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
    common.update("store/games.csv", table, id_)
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
    
    for row in table:
        row = row.split(";")


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
