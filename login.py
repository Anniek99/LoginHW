def login():
    # ask for user, psw, & age
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    age = int(input("Enter your age: ")) 

    # example login for testing
    stored_username = "annie1"
    stored_password = "youllneverguessmypsw123"

    # check if entered username + password match the stored ones
    if username == stored_username and password == stored_password:
        print("Login successful!")
        
        # determine level of access based on user age
        if age >= 13:
            print("You have been granted full access.")
        else:
            print("You have been granted partial access.")
    else:
        print("Login has failed, you are denied access. The username or password you entered is incorrect.")

login()
