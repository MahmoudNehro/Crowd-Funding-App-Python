import re

def store_info(first_name, last_name, email, password, mobile):
    file = open("users.txt", "a")
    file.write(first_name + '|' + last_name + '|' + email + '|' + password + '|'+ mobile + '\n')
    file.close()


def take_info():
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    regex_phone = '^01[0-2,5]{1}[0-9]{8}$'
    # first_name ####################
    first_name = input("Enter your first name: ")
    while not first_name.isalpha():
        print("Please enter a valid name")
        first_name = input("Enter your first name: ")
    # last_name ##################
    last_name = input("Enter your last name: ")
    while not last_name.isalpha():
        print("Please enter a valid name")
        last_name = input("Enter your last name: ")
    # email ###########################
    email = input("Enter your email: ")
    file1 = open('users.txt', 'r')
    for item in file1:
        items = item.split('|')
        while email==items[2]:
            print("Email is repeated! ")
            email = input("Enter your email: ") 
    while(not re.search(regex, email)):
        print("Please enter a valid email")
        email = input("Enter your email: ")
    # password  #####################
    password = input("Enter your password: ")
    while len(password) < 8:
        print("Password can't be shorter than 8 characters")
        password = input("Enter your password: ")
    #confirm password #################
    confirm_password = input("confirm your password: ")
    while confirm_password != password:
        print("password doesn't match")
        confirm_password = input("confirm your password: ")
    #mobile phone #################
    mobile = input("enter your mobile: ")
    while not re.search(regex_phone, mobile) :
        print("invalid phone number")
        mobile = input("enter your mobile: ")    
    store_info(first_name, last_name, email,password, mobile)
    