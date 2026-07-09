class Account:
    def __init__(self):
        self.__account_no=0
        self.__balance=0

    def set_balance(self,acc,bal):
        self.__balance=bal
        self.__account_no=acc

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("DEPOSIT SUCCESSFUL")
        else:
            print("INVALID AMOUNT")

    def withdraw(self, amount):
        if amount <= 0:
            print("INVALID AMOUNT")

        elif self.__balance >= amount:
            self.__balance -= amount
            print("WITHDRAWAL SUCCESSFUL")

        else:
            print("INSUFFICIENT BALANCE")

    def get_balance(self):
        print(self.__balance)

p = Account()
acc = int(input("ENTER THE  ACCOUNT NUMBER: "))
bal= int(input("ENTER THE AMOUNT IN ACCOUNT : "))
p.set_balance(acc,bal)

option = int(input(
    "SELECT THE FOLLOWING OPTIONS\n"
    "1. DEPOSIT INTO ACCOUNT 1\n"
    "2. WITHDRAW FROM ACCOUNT 1\n"
    "3. GET BALANCE FROM ACCOUNT 1\n"
    "0. EXIT\n"
    "ENTER YOUR CHOICE: "
))

while option != 0:

    if option == 1:
        amount = int(input("ENTER THE AMOUNT TO BE DEPOSITED: "))
        p.deposit(amount)

    elif option == 2:
        amount = int(input("ENTER THE AMOUNT TO BE WITHDRAWN: "))
        p.withdraw(amount)

    elif option == 3:
        p.get_balance()

    else:
        print("INVALID CHOICE")

    option = int(input("ENTER YOUR CHOICE: "))
