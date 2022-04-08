def view_all():
    # print(email)
    try:
        file = open('projects.txt', 'r')
        for project in file:
            projects = project.split('|')
            for i in projects:
                print(i)
            print("=======================")    


    except FileNotFoundError:
        print("Not found", FileNotFoundError)
        open('projects.txt', 'w')
   
   
