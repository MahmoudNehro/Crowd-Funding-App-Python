import re
def search():
    date_regex='^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
    start_date = input("Please enter start date to search: ")
    while not re.search(date_regex,start_date):
        print("Please enter valid date")
        start_date = input("Enter start date: ")
    end_date = input("Please enter end date to search: ")
    while not re.search(date_regex,end_date):
        print("Please enter valid date")
        end_date = input("Enter end date to search: ")  
    file = open('projects.txt', 'r')
    for project in file:
        projects = project.split('|')
        if start_date == projects[3] and end_date == projects[4]:
            return  f"Project title: {projects[0]}, project details: {projects[1]}, total funding: {projects[2]} start_date: {projects[3]} , end_date: {projects[4]}"
    return None    
        

