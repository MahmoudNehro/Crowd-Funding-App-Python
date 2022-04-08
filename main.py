import helpers.helpers as helpers
import autentication_system.register as register
import autentication_system.login as login
def main():
    if __name__ == "__main__":
        print("""
        [------1-Register------]
        [------2-Login--------]
            """)
        user_choice = input("Plese Choose an option: ")
        if user_choice.isnumeric():
            switch = int(user_choice)
            if switch == helpers.menu_items["Register"]:
                register.take_info()
            elif switch == helpers.menu_items["Login"]:
                login.auth()
            else:
                print("please choose 1 or 2")
                main()    
        else:
            print("Please choose a valid input")
            main()    

main()