import os
restaurants_list = ['Pizza', 'Sushi']

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
    print("1. Register restaurant") 
    print("2. List restaurants")
    print("3. Activate restaurant")
    print("4. Quit\n")

def finish_app():
    # os.system("cls") at windows
    # os.system("clear") #at Mac and Linux
    show_subheading("Finishing the Program")
    exit()

def return_to_main_menu():
    input("\nType ENTER to return to the Main menu.")
    main()

def invalid_option():
    print("Invalid option.\n")
    return_to_main_menu()

def show_subheading(texto):
    os.system('clear')
    print(texto)
    print()


def register_restaurant():
    show_subheading("Registration of new restaurants")
    restaurant_name = input("Type the desired restaurant name: ")
    restaurants_list.append(restaurant_name)
    print(f"The restaurant {restaurant_name} was registered succesfully!")
    
    return_to_main_menu()

def list_restaurants():
    show_subheading("List of restaurants")
    
    for restaurants in restaurants_list:
        print(f'.{restaurants}')
    
    return_to_main_menu()
def choose_option():
    try:
        chosen_option = int(input("Choose an option: "))

        if chosen_option == 1:
            register_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            print("Activate restaurant")
        elif chosen_option == 4:
            finish_app()
        else:
            invalid_option()
    except Exception:
        invalid_option()

def main(): # Define the working steps of the app, makes easier the maintenance
    os.system("clear")
    show_app_name()
    show_options()
    choose_option()


if __name__ == "__main__":  #if main file
    main()