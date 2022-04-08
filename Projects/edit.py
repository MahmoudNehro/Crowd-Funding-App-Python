import re
def edit(email):
    date_regex='^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
    old_title = input("Please enter a title: ")
    new_data = []
    try:
        file = open('projects.txt', 'r')
        for project in file:
            projects = project.split('|')
            email1= email + '\n'
            if(old_title==projects[0] and email1 == projects[5]):
                new_title = input("Enter your project title: ") 
                file1 = open('projects.txt', 'r')
                for item in file1:
                    items = item.split('|')
                    while new_title==items[0]:
                        print("title is repeated")
                        new_title = input("Enter your project title: ") 
                while not new_title.isalpha():
                     print("Please enter a valid title")
                     new_title = input("Enter your project title: ")

                new_details = input("Enter your project details: ")
                while not new_details.isalpha():
                    print("Please enter details")
                    new_details = input("Enter your project details: ")

                new_target = input("Enter your target: ")
                while not new_target.isnumeric():
                    print("Please enter valid currency")
                    new_target = input("Enter your target: ")

                new_start_date = input("Enter start date: ")
                while not re.search(date_regex,new_start_date):
                    print("Please enter valid date")
                    new_start_date = input("Enter start date: ")
                new_end_date = input("Enter end date: ")
                while not re.search(date_regex,new_end_date):
                    print("Please enter valid date")
                    new_end_date = input("Enter end date: ")  
                projects[0] = new_title
                projects[1]= new_details
                projects[2]= new_target
                projects[3]= new_start_date
                projects[4]= new_end_date
            new_file='|'.join(projects)
            new_data.append(new_file)
        print(new_data)
        new_data1=''.join(new_data)
        file1 = open('projects.txt', 'w')
        file1.write(new_data1)
        file1.close()
    


    except FileNotFoundError:
        print("Not found", FileNotFoundError)
        open('projects.txt', 'w')