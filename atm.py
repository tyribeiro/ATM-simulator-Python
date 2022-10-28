# import cardholder class for access to the cardholder information
from cardholder import cardHolder


# print out menu with options for user
def print_menu():
    print("What would you like to do today?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")


# methods

# deposit method
def deposit(cardHolder):
    # validate user input, check if its a valid number
    try:
        # float to handle decimals
        deposit = float(input("Enter amount to deposit: "))

        # modify balance by using getter and setter methods, print confirmation and new balance
        cardHolder.set_balance(cardHolder.get_balance() + deposit)

        print("Deposit Successful! Your new balance is: $", str(cardHolder.get_balance()))
        print()
    except:
        print
        print("Invalid Input!")


# withdraw method
def withdraw(cardHolder):
    # validate user input, check if its a valid number
    try:
        # float to handle decimals
        withdraw = float(input("Enter amount you want to withdraw: "))

        # validate if user is attempting to withdraw more than they have in balance
        if (cardHolder.get_balance() < withdraw):
            print()
            print("Insufficient balance!")
            print()
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
                    # modify balance by using getter and setter methods, print confirmation and new balance
            print()
            print("Withdrawal Successful! Your new balance is: $", str(cardHolder.get_balance()))
            print()
    except:
        print("Invalid Input!")
        print()


# check balance method
def check_balance(cardHolder):
    print("Current Balance: $", cardHolder.get_balance())
    print()

# main method
if __name__ == '__main__':
    # instantiate new cardholder
    current_user = cardHolder("", "", "", "", "")

    # create cardholders database
    list_of_cardholders = []

    # create cardholders
    list_of_cardholders.append(cardHolder("1234567890123456", 1234, "John", "Smith", 234.87))
    list_of_cardholders.append(cardHolder("1357902468022343", 1235, "Thais", "Ribeiro", 324.12))
    list_of_cardholders.append(cardHolder("6758766525241456", 1357, "Ally", "Johnson", 102.17))
    list_of_cardholders.append(cardHolder("1284765564524434", 2468, "David", "Goliath", 67.88))
    
    # prompt users
    debitCardNumber = ""

    # user validation loop
    # get debit card number from user, validate that its in the database
    while True:
        try:
            debitCardNumber = str(input("Enter debit card number: "))
            print()

            # iterate through cardholders and check if user exists
            debitMatch = [holder for holder in list_of_cardholders if holder.cardNum == debitCardNumber.strip()]

            if (len(debitMatch) > 0):
                current_user = debitMatch[0]
                print(current_user.get_pin())
                break
            else:
                print("Card Number Invalid. Try again.")
                print()
        except:
            print("Card Number Invalid. Try again.")
            print()

# prompt for pin
# user validation loop


# check if pin matches debit card that user entered
while True:
    try:
        userPin = str(input("Enter PIN: ").strip())
        if (current_user.get_pin() == userPin):
            break
        else:
            print("Invalid PIN. Try Again.")
            print()
    except:
        print("Invalid PIN. Try again.")
        print()

# print options for user after validating them
print()
print("Welcome, ", current_user.get_fName(), "!")
option = 0

# run loop while user didnt choose to exit (option 4 from menu)
while (True):
    print_menu()
    # validate option
    try:
        option = int(input())
    except:
        print("Invalid Input. Try again.")
        print()


    if (option == 1):
        print()
        deposit(current_user)
    elif (option == 2):
        print()
        withdraw(current_user)
    elif (option == 3):
        print()
        check_balance(current_user)
    elif (option == 4):
        break
    else:
        option = 0
print()
print("Thank you! Bye Bye!")
