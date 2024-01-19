import os
restaurants_list = [{'name':'Patio', 'category':'Italian', 'active':'False'},
                    {'name':'La Cocina', 'category':'Mexican', 'active':'True'},
                    {'name':'Nanoko', 'category':'Japanese', 'active':'True'},
                    {'name':'Le Puissant', 'category':'French', 'active':'False'}
                    ]

def show_app_name():
    print("""
████████╗░█████╗░░██████╗████████╗██╗░░░██╗  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝╚██╗░██╔╝  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
░░░██║░░░███████║╚█████╗░░░░██║░░░░╚████╔╝░  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░░░██║░░░██╔══██║░╚═══██╗░░░██║░░░░░╚██╔╝░░  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
░░░██║░░░██║░░██║██████╔╝░░░██║░░░░░░██║░░░  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░░░╚═╝░░░  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""") #""" line break

# SHORTCUT: to apply TAB in many lines at once -  select the lines, then CTRL + ]
def show_options():
    """
    Display the available options for the user.

    This function prints a menu of options that the user can choose from.
    The options include:
        1. Register restaurant
        2. List restaurants
        3. Switch restaurant status
        4. Quit

    Parameters:
        None

    Returns:
        None
    """
    print("1. Register restaurant") 
    print("2. List restaurants")
    print("3. Switch restaurant status")
    print("4. Quit\n")

def finish_app():
    """
    Finish the application by clearing the console and exiting the program.
    """
    # os.system("cls") at windows
    # os.system("clear") #at Mac and Linux
    show_subheading("Finishing the Program")
    exit()

def return_to_main_menu():
    """
    Prompt the user to type ENTER to return to the Main menu.
    """
    input("\nType ENTER to return to the Main menu.")
    main()

def invalid_option():
    """
    This function prints an error message for an invalid option and returns to the main menu.
    """
    print("Invalid option.\n")
    return_to_main_menu()

def show_subheading(text):
    """
    Display a subheading with a clear screen, a line of asterisks, the input text, another line of asterisks, and a blank line.
    Param:
        text: a string representing the subheading text
    Return:
        None
    """
    os.system('clear')
    line = "*" * (len(text))
    print(line)
    print(text)
    print(line)
    print()


def register_restaurant():
    """
    Register a new restaurant.

    This function prompts the user to enter the desired restaurant name and category.
    It then creates a dictionary with the restaurant name, category, and sets the "active" flag to False.
    The dictionary is appended to the restaurants_list global variable.
    Finally, a success message is printed.

    Returns:
        None

    Inputs:
    - Restaurant name
    - Category

    Outputs:
    - Adds a new restaurant to the dictionary
    """

    show_subheading("Registration of new restaurants")
    restaurant_name = input("Type the desired restaurant name: ")
    restaurant_category = input(f"Type the desired category of the restaurant {restaurant_name}: ")
    restaurant_data = {"name":restaurant_name, "category":restaurant_category, "active": False}
    restaurants_list.append(restaurant_data)
    print(f"The restaurant {restaurant_name} was registered succesfully!")
    
    return_to_main_menu()

def list_restaurants():
    """
    Function to list restaurants in a formatted table with name, category, and status. 
    No parameters. 
    No return value.
    """
    show_subheading("List of restaurants")
    
    print(f"{'Name of restaurant'.ljust(22)} | {'Category'.ljust(20)} | Status")
    for restaurants in restaurants_list:
        restaurant_name = restaurants['name']
        restaurant_category = restaurants['category']
        restaurant_active = "Activated" if restaurants['active'] else "Deactivated"
        print(f'- {restaurant_name.ljust(20)} | {restaurant_category.ljust(20)} | {restaurant_active}')
    
    return_to_main_menu()

def switch_restaurant_status():
    """
    Switches the status of a restaurant based on user input.
    This function prompts the user for a restaurant name, then searches for
    the restaurant in the 'restaurants_list'. If found, it toggles the 
    'active' status of the restaurant and prints a message. If the 
    restaurant is not found, it prints a message indicating the same. 
    After the operation, the function returns to the main menu.
    """
    show_subheading("Switching the status of a restaurant")
    restaurant_name = input("Type the desired restaurant name: ")
    restaurant_found = False

    for restaurant in restaurants_list:
        if restaurant_name == restaurant["name"]:
            restaurant_found = True
            restaurant["active"] = not restaurant["active"]
            state_message = f"The restaurant {restaurant_name} was successfully activated." if restaurant["active"] else f"The restaurant {restaurant_name} was successfully deactivated."
            print(state_message)
            break
    if not restaurant_found:
            print(f"The restaurant {restaurant_name} was not found.")

    return_to_main_menu()
def choose_option():
    """
    Function to prompt the user to choose an option and call the corresponding 
    function based on the chosen option. No parameters or return types specified.
    """
    try:
        chosen_option = int(input("Choose an option: "))

        if chosen_option == 1:
            register_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            switch_restaurant_status()
        elif chosen_option == 4:
            finish_app()
        else:
            invalid_option()
    except Exception:
        invalid_option()

def main():
    """
    Execute the main program logic, which clears the screen, shows the app name,
    displays the available options, and allows the user to choose an option.
    """
    os.system("clear")
    show_app_name()
    show_options()
    choose_option()

if __name__ == "__main__":  #if main file
    main()