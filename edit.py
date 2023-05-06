from view import view_projects

def edit_project():
    user_id = input("Enter your user ID: ")
    project_id = input("Enter the ID of the project you want to edit: ")


    with open('projects_data.txt') as f:
        projects_data = f.readlines()

    found_project = None
    for i, project in enumerate(projects_data):
        data = project.strip().split(',')
        if data[0] == project_id:
            if data[6] != user_id:
                print("You can only edit your own projects.")
                return

            found_project = i
            break

    if found_project is not None:
        project = projects_data[found_project].strip().split(',')
        while True:
            key = input('\nPlease enter the name of the key that you want to update: ')
            if key in ['title', 'details', 'total_target', 'start_time', 'end_time']:
                break
            else:
                print("Invalid key name")

        new_value = input('\nPlease enter the new value for the key: ')
        key_index = ['title', 'details', 'total_target', 'start_time', 'end_time'].index(key)
        project[key_index+1] = new_value
        projects_data[found_project] = ','.join(project) + '\n'

        with open('projects_data.txt', 'w') as f:
            f.writelines(projects_data)

        print("\nProject has been updated successfully.")
