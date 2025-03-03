userinput = []
ticket = 1000
withdraw = 0
option = 0
deposit = 0
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
            dashboard(option,deposit,ticket,withdraw,currentTicket)
            return True  
        elif user[0] != username and user[1] != password:
            print(f"-----User not registered-----\n")
            return False      
        else:
            print("-----Incorrect username or password-----\n")
            
def dashboard(option,deposit,ticket,withdraw,currentTicket):
    while True:
        print("----------DASHBOARD----------")
        print(f"Ticket balance: {ticket}")
        print("[1] Deposit\n[2] Withdraw\n[3] Logout")
        option = int(input("Choose Option: "))
        if option == 1:
            deposit = int(input("Enter Amount to Deposit: "))
            currentTicket = deposit + ticket
            print(f"Current Ticket Balance: {ticket}")
        elif option == 2:
            withdraw = int(input("Enter Amount to Withdraw: "))
            currentTicket = withdraw - ticket
            print(f"Current Ticket Balance: {ticket}")
        elif option == 3:
            print("Logout...")
            return
        else:
            print("Invalid Input!")  
    

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