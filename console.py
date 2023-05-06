from pathlib import Path
from login import login_app
from register import register_user

def menu():
    from menu import menu
    menu()

choice = input("Please choose registration or login \n1) Registration \n2) Login \n3) exit \n> ")

if choice == "1":
    mypath = Path("users_data.txt")

    register_user()
    menu()

elif choice == "2":
    login_app()

elif choice == "3":
    exit()

else:
    print("\nPlease choose from the menu")