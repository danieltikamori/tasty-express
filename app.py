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
    restaurant_category = input(f"Type the desired category of the restaurant {restaurant_name}: ")
    restaurant_data = {"name":restaurant_name, "category":restaurant_category, "active": False}
    restaurants_list.append(restaurant_data)
    print(f"The restaurant {restaurant_name} was registered succesfully!")
    
    return_to_main_menu()

def list_restaurants():
    show_subheading("List of restaurants")
    
    for restaurants in restaurants_list:
        restaurant_name = restaurants['name']
        restaurant_category = restaurants['category']
        restaurant_active = restaurants['active']
        print(f'- {restaurant_name} | {restaurant_category} | {restaurant_active}')
    
    return_to_main_menu()

def switch_restaurant_state():
    show_subheading("Switching the state of a restaurant")
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
    try:
        chosen_option = int(input("Choose an option: "))

        if chosen_option == 1:
            register_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            switch_restaurant_state()
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