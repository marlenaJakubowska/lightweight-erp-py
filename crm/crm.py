""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


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


def handle_menu():
    options = ["Show all", "Add", "Delete"]
    menu_title = "Human resources manager"
    exit_message = "Back to main menu"
    ui.print_menu(menu_title, options, exit_message)


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "0":
        return False
    elif option == "1":
        list_of_customers = []
        with open("crm/customers.csv") as file:
            for line in file:
                list_of_customers.append(line.strip('\n'))
        show_table(list_of_customers)
        # start_module()
    elif option == "2":
        table = data_manager.get_table_from_file("crm/customers.csv")
        add(table)
    elif option == "3":
        id_ = ui.get_inputs(["Please enter an ID: "], "")
        remove(data_manager.get_table_from_file("crm/customers.csv"), id_)


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    ui.print_table(table, ["id", "name", "email", "subscribed"])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    unique_id = common.generate_random(table)
    inputs = ui.get_inputs(["Enter name: ", "Enter email: ", "Subscription (1/0 = yes/no): "], "")
    with open("crm/customers.csv", "a") as file:
        file.write("\n")
        file.write(f"{unique_id};{';'.join(inputs)}")

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
    print(id_)
    for row in table:
        #print(id_[0], row[0])
        if id_[0] == row[0]:
            #print('dos,,')
            #with open("crm/customers.csv", "r+") as file:
            #for i in range(len(row)):
            inputs = ui.get_inputs([f"Do you want to delete this record ({row})? [y/n] "], "")
            print(inputs)
            print(inputs[0])

            if inputs[0] == "y":
                table.remove(row)
            else: #inputs == "n":
                continue

    data_manager.write_table_to_file("crm/customers.csv", table)
            
            # table[row] = ';'.join(row)
            # for element in table:
            #     file.write(f"{element}\n")
                    
    #show_table(table)
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

    # your code

    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    # longest_name = ""
    # name_index = 1
    # id_table = [line[longest_name] for line in table]


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code
