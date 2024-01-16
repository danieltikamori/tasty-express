import os

print("""
████████╗░█████╗░░██████╗████████╗██╗░░░██╗  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝╚██╗░██╔╝  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
░░░██║░░░███████║╚█████╗░░░░██║░░░░╚████╔╝░  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░░░██║░░░██╔══██║░╚═══██╗░░░██║░░░░░╚██╔╝░░  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
░░░██║░░░██║░░██║██████╔╝░░░██║░░░░░░██║░░░  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░░░╚═╝░░░  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""") #""" line break

print("1. Register restaurant")
print("2. List restaurants")
print("3. Activate restaurant")
print("4. Quit\n")

chosen_option = int(input("Choose an option: "))

def finish_app():
    # os.system("cls") at windows
    os.system("clear") #at Mac and Linux
    print("Finishing the Program")
    exit()

if chosen_option == 1:
    print("Register restaurant")
elif chosen_option == 2:
    print("List restaurants")
elif chosen_option == 3:
    print("Activate restaurant")
else:
    finish_app()
