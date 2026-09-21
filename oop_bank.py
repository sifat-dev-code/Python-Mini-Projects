print(" Welcome to OOP Bank!")


class BankAccount:
    
    
    def __init__(self, owner_name, initial_balance):
        self.name = owner_name
        self.balance = initial_balance
        print(f" Account created for {self.name} with {self.balance} Taka.")

    def deposit(self, amount):
        self.balance+=amount
        
        print(f" Deposited {amount} Taka.")

    def show_balance(self):
        print(f"Name of the user is {self.name} and his current balance is {self.balance}")
       
my_account = BankAccount("Sifat", 5000)
my_account.deposit(60000)
my_account.show_balance()
