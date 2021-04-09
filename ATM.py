class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your Balance is 10000")

    def withdrawl(self, number):
        new_number = 10000 - number
        print("The Amount Withdrawed From Your Account:"+str(number)+". Your Available Balance is"+ str(new_number))

def main():
    Card_number = input("Insert Your Card Number:-")
    pin_number = input("Enter Your Pin:-")

    new_user = Atm(Card_number, pin_number)

    print("Choose Your Activity")
    print("1. Balance Enquiry 2. Withdrawl")
    activity = int(input("Enter The Activity Number :-"))
    if(activity == 1):
        new_user.check_balance()
    elif(activity == 2):
        amount = int(input("Enter The Amount:-"))
        new_user.withdrawl(amount)
    else:
        print("Enter A Valid Number")

main()
