 #create class
class cardHolder:
    #constructor that initiates the required fields
    def __init__(self,cardNum,pin,fName,lName,balance):
        self.cardNum = cardNum;
        self.pin = pin;
        self.fName = fName;
        self.lName = lName;
        self.balance = balance;
 
    #getters
    def get_cardNum(self):
        return self.cardNum;
    def get_pin(self):
        return self.pin;
    def get_fName(self):
        return self.fName;
    def get_lName(self):
        return self.lName;
    def get_balance(self):
        return self.balance;        
   
    #setters
    def set_cardNum(self,newValue):
        self.cardNum = newValue;
    def set_pin(self,newValue):
        self.pin = newValue;
    def set_fName(self,newValue):
        self.fName = newValue;
    def set_lName(self,newValue):
        self.lName = newValue;
    def set_balance(self,newValue):
        self.balance = newValue;
 
    #print out cardholder information
    def print_out(self):
        print("Card Number: ", self.cardNum);
        print("Pin: ", self.pin);
        print("First Name: ", self.fName);
        print("Last Name: ", self.lName);
        print("Balance: ", self.balance);