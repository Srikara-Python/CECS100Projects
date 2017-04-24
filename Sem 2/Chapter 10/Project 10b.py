"""
Make a bank account using classes
"""

class BankAccount:

    def __init__(self):
        self.__balance = 500.00

    def check_bal(self):
        case = str(self.__balance).rpartition('.')
        newbal = ""
        if len(case[2]) < 1:
            place = [case[0], case[1], '00']
            newbal = newbal.join(place)
        elif len(case[2]) == 1:
            place = [case[0], case[1], case[2] + '0']
            newbal = newbal.join(place)
        else:
            newbal = str(self.__balance)

        print("Your balance is", newbal, "\n")


    def deposit(self):
        while 1 == 1:
            amt = input("Enter the amount you would like to deposit:\n~~\t")
            case = amt.rpartition('.')
            if len(case[2]) > 2 and not case[2] == "":
                print("Invalid amount entered.  Please enter a new amount.")
            else:
                try:
                    amt = float(amt)
                except ValueError:
                    print("~~ ValueError Raised ~~\nInvalid amount entered.  Please enter a new amount.")
                else:
                    self.__balance += amt
                break


    def withdraw(self):
        while 1 == 1:
            amt = input("Enter the amount you would like to withdraw:\n~~\t")
            case = amt.rpartition('.')
            if len(case[2]) > 2 and not case[0] == '':
                print("Invalid amount entered.  Please enter a new amount.")
            elif float(amt) > self.__balance:
                print("Invalid amount, cannot overdraft.\n")
            else:
                try:
                    amt = float(amt)
                except ValueError:
                    print("~~ ValueError Raised ~~\nInvalid amount entered.  Please enter a new amount.")
                else:
                    self.__balance -= amt
                break


def main():
    acct = BankAccount()
    check = 1
    while check == 1:
        print("1: Check Balance\n2: Deposit Funds\n3: Withdraw Funds\n\n0: Exit Program")
        user = input("Enter the corresponding number to the action you would like to take\n~~\t")
        if user == '1':
            acct.check_bal()
        elif user == '2':
            acct.deposit()
        elif user == '3':
            acct.withdraw()
        elif user == '0':
            check = 0

main()