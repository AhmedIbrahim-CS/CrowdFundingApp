import re
import uuid

def validate_first_name(first_name):
    return bool(first_name) and not first_name.isdigit()

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.fullmatch(pattern, email) is not None

def validate_password(password, confirm_password):
    return password == confirm_password

def validate_phone_number(phone_number):
    pattern = r'^01[0125][0-9]{8}$'
    return re.fullmatch(pattern, phone_number) is not None

def user_id_exists(uid):
    with open("users_data.txt", "r") as f:
        for line in f:
            if line.startswith(uid):
                return True
        return False

def register_user():
    # First Name Validation
    while True:
        first_name = input("Enter your first name: ")
        if not validate_first_name(first_name):
            print("Please enter a valid name.")
        else:
            break

    # Email Validation
    while True:
        email = input("Enter your email: ")
        if not validate_email(email):
            print("Please enter a valid email.")
        else:
            break

    # Password Validation
    while True:
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")
        if not validate_password(password, confirm_password):
            print("Passwords do not match")
        else:
            break

    # Phone Validation
    while True:
        mobile_phone = input("Enter your phone number: ")
        if not validate_phone_number(mobile_phone):
            print("Please enter a valid phone number.")
        else:
            break

    # Generate User ID
    while True:
        uid = input("Enter your user id: ")
        if user_id_exists(uid):
            print("User ID already exists. Please enter a different user ID.")
        else:
            break

    # Save user data to file
    user_data = {
        "uid": uid,
        "first_name": first_name,
        "email": email,
        "password": password,
        "mobile_phone": mobile_phone
    }
    with open("users_data.txt", "a") as f:
        f.write(f"{uid},{first_name},{email},{password},{mobile_phone}\n")