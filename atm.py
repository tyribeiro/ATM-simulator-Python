#import cardholder class for access to the cardholder information
from cardholder import cardHolder
 
 
#print out menu with options for user
def print_menu():
    print("What would you like to do today?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
 
    deposit(current_user)
 
#methods
 
#deposit method
def deposit(cardHolder):
    #validate user input, check if its a valid number
    try:
        #float to handle decimals
        deposit = float(input("Enter amount to deposit: "))
       
        #modify balance by using getter and setter methods, print confirmation and new balance
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Deposit Successful! Your new balance is: $", str(cardHolder.get_balance()))
    except:
        print("Invalid Input!")
 
#withdraw method
def withdraw(cardHolder):
    #validate user input, check if its a valid number
    try:
        #float to handle decimals
        withdraw = float(input("Enter amount you want to withdraw: "))
       
        #validate if user is attempting to withdraw more than they have in balance
        if (cardHolder.get_balance() < withdraw):
            print("Insufficient balance!")
        else:
            cardHolder.set_balance(cardHolder.get_balance()-withdraw)
            print("Withdraw Successful!")
 
 
        #modify balance by using getter and setter methods, print confirmation and new balance
        cardHolder.set_balance(cardHolder.get_balance() - withdraw)
        print("Withdrawal Successful! Your new balance is: $", str(cardHolder.get_balance()))
    except:
        print("Invalid Input!")
   
 
#check balance method
def check_balance(cardHolder):
    print("Current Balance: $", cardHolder.get_balance())
 
 

