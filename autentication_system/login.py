import Projects.crud_menu as crud
import main
def auth():
    email = input("Please Enter your email: ")
    password = input("Enter your password: ")
    found = False
    try:
        file = open('users.txt', 'r')
        for user in file:
            users = user.split('|')
            if (users[2] == email) and (users[3] == password):
                found = True

    except FileNotFoundError:
        print("Not found", FileNotFoundError)
        open('users.txt', 'w')
   
    if found:
        print("========Valid Login!========")
        crud.crud_menu(email)
    else:
        print("Invalid, try again or register")
        main.main()
