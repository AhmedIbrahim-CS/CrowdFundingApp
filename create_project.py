import time
from pathlib import Path
import re

def is_project_name_exist(title, project_id):
    with open('projects_data.txt', 'r') as f:
        for line in f:
            data = line.strip().split(',')
            if data[0] == project_id and data[1] == title:
                return True
    return False
def project_id_exists(project_id):
    with open('projects_data.txt', 'r') as f:
        for line in f:
            data = line.strip().split(',')
            if data[0] == project_id:
                return True
    return False
def create():
    userid = input( "enter your user id: " )

    # Generate Project ID
    while True:
        project_id = input("Enter your project id: ")
        if project_id_exists(project_id):
            print("Project ID already exists. Please enter a different project ID.")
        else:
            break

    title = input("Title: ")
    details = input("Details: ")
    total_target = input("Total target: ")
    start_time = input("Start Date (mm/dd/yyyy): ")
    end_time = input("End Date (mm/dd/yyyy): ")


    date_regex = r'\d{2}/\d{2}/\d{4}'

    if not re.match(date_regex, start_time) or not re.match(date_regex, end_time):
        print('Invalid date format')
        create()
        return

    start_date = time.strptime(start_time, '%m/%d/%Y')
    end_date = time.strptime(end_time, '%m/%d/%Y')

    # # Generate a unique project id
    # project_id = str(int(time.time()))

    project_data = f"{project_id},{title},{details},{total_target},{start_time},{end_time},{userid}"

    start_date = None
    end_date = None

    try:
        start_date = time.strptime( start_time, '%m/%d/%Y' )
        end_date = time.strptime( end_time, '%m/%d/%Y' )
    except ValueError:
        print( 'Invalid date format' )
        create()
        return

    start_date = None
    end_date = None

    try:
        start_date = time.strptime( start_time, '%m/%d/%Y' )
        end_date = time.strptime( end_time, '%m/%d/%Y' )
    except ValueError:
        print( 'Invalid date format' )
        create()
        return

    if is_project_name_exist(title, project_id):
        print("\nThis project name already exists")
        create()
    else:
        with open('projects_data.txt', 'a') as f:
            f.write(project_data + "\n")
        print('Your project is created successfully')