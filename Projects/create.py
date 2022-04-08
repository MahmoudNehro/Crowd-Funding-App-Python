import re
def create_project(email):
    date_regex='^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
    ###############title
    project_title = input("Enter your project title: ")
    file1 = open('projects.txt', 'r')
    for item in file1:
        items = item.split('|')
        while project_title==items[0]:
            print("Title is repeated! ")
            project_title = input("Enter your project title: ") 
    while not project_title.isalpha():
        print("Please enter a valid title")
        project_title = input("Enter your project title: ")
    #################details
    Details = input("Enter your project details: ")
    while not Details.isalpha():
        print("Please enter details")
        Details = input("Enter your project details: ")
    ###################target
    total_target = input("Enter your target: ")
    while not total_target.isnumeric():
        print("Please enter valid currency")
        total_target = input("Enter your target: ")
    ###################start_date    
    start_date = input("Enter start date: ")
    while not re.search(date_regex,start_date):
        print("Please enter valid date")
        start_date = input("Enter start date: ")
    ###################end_date    
    end_date = input("Enter end date: ")
    while not re.search(date_regex,end_date):
        print("Please enter valid date")
        end_date = input("Enter end date: ")  
    ############storing            
    file = open('projects.txt', 'a')
    file.write(project_title + '|' + Details + '|' + total_target + '|' +  start_date + '|' + end_date + '|' + email + '\n')
    file.close()