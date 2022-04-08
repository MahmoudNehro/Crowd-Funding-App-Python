def delete(email):
    old_title = input("Please enter a title: ")
    new_data = []
    try:
        file = open('projects.txt', 'r')
        for project in file:
            projects = project.split('|')
            email1= email + '\n'
            if(old_title==projects[0] and email1 == projects[5]):
                projects.clear()
            new_file='|'.join(projects)
            new_data.append(new_file)
        new_data1=''.join(new_data)
        file1 = open('projects.txt', 'w')
        file1.write(new_data1)
        file1.close()
    


    except FileNotFoundError:
        print("Not found", FileNotFoundError)
        open('projects.txt', 'w')