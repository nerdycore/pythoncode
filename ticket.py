userinput = []
ticket = 1000
currentTicket = 0

def signup(username, password):
    for user in userinput:
        if user[0] == username:
            print("-----User already exists-----\n")
            return False
    if not username.isalpha():
        print("-----Not contain numbers!-----\n") 
        return False   
    userinput.append((username,password))
    print(f"------------User created succesfully!-----------\n")   
    return True 

def login(username,password):
    for user in userinput:
        if user[0] == username and user[1] == password:
            print("----------Login Succesfully!-----------\n")
            return True  
        elif user[0] != username and user[1] != password:
            print(f"-----User not registered-----\n")
            return False      
        else:
            print("-----Incorrect username or password-----\n")
            
while True:
    print("---------------Ticket Withdrawal---------------")
    print("[1] Sign up")
    print("[2] Login")
    print("[3] Exit")
    choose = int(input("Choice: "))
    if choose == 1:
        print("-----------Sign up-----------")
        username = input("Enter username: ")
        password = input("Enter password: ")
        signup(username, password)
    elif choose == 2:
        print("-----------Log In-----------")
        username = input("Enter username: ")
        password = input("Enter password: ")
        login(username,password)
    elif choose == 3:
        print("-----Exit the program------")
        break
    else:
        print("Invalid Choice")          