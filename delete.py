from pathlib import Path

def delete_project(attempts_left=3):
    if attempts_left <= 0:
        print("Too many attempts. Aborting.")
        return

    user_id = input("Enter your user ID: ")
    project_id = input("Enter the ID of the project you want to delete: ")

    projects_file = Path('projects_data.txt')

    with projects_file.open() as f:
        projects_data = f.readlines()

    found_project = None
    for i, project in enumerate(projects_data):
        data = project.strip().split(',')
        if data[0] == project_id:
            # Check if the user is authorized to delete the project
            if data[6] != user_id:
                print("You can only delete your own projects.")
                return

            found_project = i
            break

    if found_project is not None:
        del projects_data[found_project]
        with projects_file.open('w') as f:
            f.writelines(projects_data)
        print("\nProject has been deleted successfully.")
    else:
        print("\nTry again..")
        delete_project(attempts_left=attempts_left-1)