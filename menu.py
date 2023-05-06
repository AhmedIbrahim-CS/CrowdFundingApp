from view import view_projects
from create_project import create
from edit import edit_project
from delete import delete_project
from search import search_projects

def menu():

    while True:
        print("\n\n 1) Create Project \n 2) View Project \n 3) Edit Project \n 4) Delete Project \n 5) Search For Project \n 6) Exit \n")

        choice = input("\nPlease choose from menu: ")
        if choice == "1":
            create()
        elif choice == "2":
            project_id = input("Enter a project ID to view a specific project, or leave blank to view all projects: ")
            view_projects(project_id)
        elif choice == "3":
            edit_project()
        elif choice == "4":
            delete_project()
        elif choice == "5":
            search_projects()
        elif choice == "6":
            print("Exiting menu...")
            break
        else:
            print("\nInvalid choice. Please choose from menu.")