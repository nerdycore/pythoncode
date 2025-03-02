ticket = 1000
currentTicket = 0
def ticketWithdraw(ticket,currentTicket):
    print("------------------------------")
    print(f"Your ticket balance: {ticket}")
    print("------------------------------")
    withdraw = int(input("Withdraw: "))
    print("------------------------------")
    if withdraw > ticket:
        print("Invalid Amount")
    elif ticket == 0:
        print("No more tickets")
    else:    
        ticket = ticket - withdraw
        currentTicket = ticket
        print("------------------------------")
        print(f"Your current balance ticket: {currentTicket}")
        print("------------------------------")          
   
while True:
    print("------------------------------")
    username = input("Enter Username: ")
    print("------------------------------")
    if not username.isalpha():
        print("------------------------------")
        print("Your username does not contains numbers!")
        print("------------------------------")
    else:
        ticketWithdraw(ticket,currentTicket)
    
    
    

