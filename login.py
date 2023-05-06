def menu():
    from menu import menu
    menu()

def login_app():
    user_email = input("Enter your Email: ")
    password = input("Enter your Password: ")

    with open('users_data.txt') as f:
        users_data = f.readlines()

    user_dict = None
    for user in users_data:
        data = user.strip().split(',')
        if data[2] == user_email and data[3] == password:
            user_dict = {'user_id': data[0], 'email': data[2], 'password': data[3]}
            break

    if user_dict:
        user_id = user_dict.get('user_id')
        print("Login successful")
        menu()
    else:
        print("Invalid email or password. Please try again.")
        login_app()
