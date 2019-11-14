""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    the_longest_in_col = [['-']*len(table[0].split(";"))]
    for row in table:
        row = row.split(";")
        # Loop to create a list of the longest elements
        for i in range(len(row)):
            if len(row[i]) > len(the_longest_in_col[0][i]):
                the_longest_in_col[0][i] = row[i]

    # Loop to eventually modify the list of longest elements, if title_list has longer elements
    for i in range(len(title_list)):
        # print(i)
        # print(len(title_list))
        # print(title_list)
        if len(title_list[i]) > len(the_longest_in_col[0][i]):
            the_longest_in_col[0][i] = title_list[i]
        title_list[i] = title_list[i].center(len(the_longest_in_col[0][i]))

    # Loop to create width of the table
    table_width = 3*len(the_longest_in_col[0])-1
    for element in the_longest_in_col[0]:
        table_width += len(element)

    # Print awesome table
    print(f"/{'-'*(table_width)}\\")
    print(f"| {' | '.join(title_list)} |")
    for row in table:
        print(f"|{'-'*(table_width)}|")
        # Loop to center elements in row
        row = row.split(";")
        for i in range(len(row)):
            row[i] = row[i].center(len(the_longest_in_col[0][i]))
        print(f"| {' | '.join(row)} |")
    print(f"\\{'-'*(table_width)}/")


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print()
    print(f"{title}:")
    for index, element in enumerate(list_options):
        print(f"\t({index+1}) {element}")
    print(f"\t(0) {exit_message}")


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    print(title)
    inputs = []
    for label in list_labels:
        print(label)
        user_input = input()
        inputs.append(user_input)
    # print(inputs)
    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(f"Error: {message}")
