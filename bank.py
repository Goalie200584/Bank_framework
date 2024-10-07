import os

class Bank:
    '''Class for your bank account that you can withdraw, deposit, or view account balance'''
    def __init__(self): #initializes bank account starting at user inputted balance
        login = self.login()
        if login == 1:
            self.get_balance()
            print(f"Welcome Back {self.username.capitalize()}!\n")
        elif login == 0:
            self.get_balance()
            print("Account created!")
        elif login == -1:
            print("Incorrect Password, try again!")
            quit()
        elif login == -2:
            print("No account created, Have a great day!")
            quit()

    def login(self):
        self.username = input("Enter your username: ").lower()
        if os.path.exists(f"{self.username}.txt"):
            with open(f"{self.username}.txt", "r") as file:
                given_password = input("Enter your password: ")
                password = file.readlines()[1].split(";")[1]
                if password == given_password:
                    return 1
                else: 
                    return -1
        else: 
            if input("I don't see an account under that name, do you want to create one? (y or n)").lower() == "y":
                return 0
            else: return -2
    def get_balance(self): 
        if os.path.exists(f"{self.username}.txt"):
            with open(f"{self.username}.txt", "r") as file:
                lines = file.readlines()
                if lines == []:
                    self.balance = float(input("Enter your initial deposit"))
                else:
                    self.balance = float(lines[0].split(";")[1])
        else: 
            with open(f"{self.username}.txt", "x") as file:
                password = input("Enter the password you want to use: ")
                self.balance = float(input("Enter your initial deposit: "))
                file.write(f"balance;{self.balance}\npassword;{password}")

    def deposit(self, amount): #does a withdrawel from the bank
        self.balance += amount
        self.update_balance(self.balance)
        
    def withdraw(self, amount): #Does a deposit into th ebank
        if amount > self.balance:
            return -1
        else:
            self.balance -= amount 
            self.update_balance(self.balance)
            return 1
    def update_balance(self, amount):
        with open(f"{self.username}.txt", "r+") as file:
            lines = file.readlines()
            lines[0] = f"balance;{self.balance}"
            new_lines = ""
            for i in lines:
                if i == lines[0]:
                    new_lines += i +"\n"
                else: 
                    new_lines += i
        with open(f"{self.username}.txt", "w") as file:
            file.write(new_lines)


def ask(bank):
    while True:
        option = input("Options: \n 1. Make a Deposit\n 2. Make a Withdrawal\n 3. Obtain Balance\n 4. Quit\n")
        match option:
            case "1": #If option is for deposit, calls bank.deposit, and adds that money
                amount = float(input("Enter the amount of deposit: "))
                bank.deposit(amount)
            case "2": #If option is for withdrawal, calls bank.withdraw and subs that money
                amount = float(input("Enter the amount of withdrawal: "))
                withdraw = bank.withdraw(amount)
                if withdraw == -1: #If money over amount if bank doesnt sub, returns error
                    print(f"Denied, Maximum withdrawal of {bank.balance}\n")
                elif withdraw == 1: #subs money if its enough
                    print("Withdrawal Processed \n")
            case "3": 
                print(f"${bank.balance:,.2f}\n") #Displays balance
            case "4": 
                quit()#Quits program
            case _: 
                print("Please input a 1, 2, 3, or 4\n")
    
    

Bank = Bank()
ask(Bank)