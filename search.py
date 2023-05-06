from view import view_projects

def search_projects():
    user_id = input("Enter your user ID: ")
    project_id = input("Enter the ID of the project you want to search for: ")

    with open("projects_data.txt") as f:
        data = f.readlines()

    projects_found = []
    for line in data:
        project = line.strip().split(',')
        if project_id == project[0]:
            projects_found.append(project)

    if projects_found:
        print(f"\n{len(projects_found)} project(s) found:")
        for project in projects_found:
            if user_id == project[6]:
                view_projects(str(project[0]))
            else:
                print("No projects found for this user ID and project ID combination.")
    else:
        print("No projects found for this project ID.")
