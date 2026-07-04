class Account:

    def set_balance(self, a):
        self.balance = a

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("DEPOSIT SUCCESSFUL")
            return True
        else:
            print("INVALID AMOUNT")
            return False

    def withdraw(self, amount):
        if amount <= 0:
            print("INVALID AMOUNT")
            return False

        elif self.balance >= amount:
            self.balance -= amount
            print("WITHDRAWAL SUCCESSFUL")
            return True

        else:
            print("INSUFFICIENT BALANCE")
            return False

    def transfer(self, other_account, amount):
        if self.withdraw(amount):
            other_account.deposit(amount)
            print("TRANSFER SUCCESSFUL")
        else:
            print("TRANSFER FAILED")


p = Account()
p2 = Account()

n = int(input("ENTER THE AMOUNT IN ACCOUNT 1: "))
p.set_balance(n)

n2 = int(input("ENTER THE AMOUNT IN ACCOUNT 2: "))
p2.set_balance(n2)

option = int(input(
    "SELECT THE FOLLOWING OPTIONS\n"
    "1. CHECK ACCOUNT 1 BALANCE\n"
    "2. DEPOSIT INTO ACCOUNT 1\n"
    "3. WITHDRAW FROM ACCOUNT 1\n"
    "4. TRANSFER FROM ACCOUNT 1 TO ACCOUNT 2\n"
    "5. CHECK ACCOUNT 2 BALANCE\n"
    "0. EXIT\n"
    "ENTER YOUR CHOICE: "
))

while option != 0:

    if option == 1:
        print(f"ACCOUNT 1 BALANCE : {p.get_balance()}")

    elif option == 2:
        amount = int(input("ENTER THE AMOUNT TO BE DEPOSITED: "))
        p.deposit(amount)

    elif option == 3:
        amount = int(input("ENTER THE AMOUNT TO BE WITHDRAWN: "))
        p.withdraw(amount)

    elif option == 4:
        amount = int(input("ENTER THE AMOUNT TO BE TRANSFERRED: "))
        p.transfer(p2, amount)

    elif option == 5:
        print(f"ACCOUNT 2 BALANCE : {p2.get_balance()}")

    else:
        print("INVALID CHOICE")

    option = int(input("ENTER YOUR CHOICE: "))

print("THANK YOU")