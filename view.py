from prettytable import PrettyTable


def view_projects(project_id=None):
    if project_id:
        with open('projects_data.txt') as f:
            data = f.readlines()
            projects = []
            for line in data:
                project = line.strip().split(',')
                if project[0] == project_id:
                    projects.append(project)

            table = PrettyTable()
            table.field_names = ["project_id", "title", "details", "total_target", "start_time", "end_time", "user_id"]

            for project in projects:
                table.add_row([project[0], project[1], project[2], project[3], project[4], project[5], project[6]])

            if len(table.get_string()) > len(table.field_names) + 1:
                print(f"Project with ID {project_id}:\n{table}\n")
            else:
                print(f"No project found with ID {project_id}.")
    else:
        with open('projects_data.txt') as f:
            data = f.readlines()
            projects = []
            for line in data:
                project = line.strip().split(',')
                projects.append(project)

            table = PrettyTable()
            table.field_names = ["project_id", "title", "details", "total_target", "start_time", "end_time", "user_id"]

            for project in projects:
                table.add_row([project[0], project[1], project[2], project[3], project[4], project[5], project[6]])

            if len(table.get_string()) > len(table.field_names) + 1:
                print(f"All projects:\n{table}\n")
            else:
                print(f"No projects found.")