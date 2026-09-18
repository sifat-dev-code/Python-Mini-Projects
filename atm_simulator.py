print(" Welcome to the SMART CLI ATM!")


def check_balance(current_balance):
    print(f"\n Your current balance is: ${current_balance}")

def deposit_money(current_balance):
    amount = float(input("\nEnter amount to deposit: $"))
    new_balance = current_balance + amount
    print(f" Deposit Successful! Your new balance is: ${new_balance}")
    return new_balance
    
    

def withdraw_money(current_balance):
    amount = float(input("\nEnter amount to withdraw: $"))
    if amount>current_balance:
        print("Insufficient balance!")
        return current_balance
    else:
        new_balance = current_balance - amount
        print(f" Withdrawal Successful! Your new balance is: ${new_balance}")
        return new_balance
    
    
balance = 500.0 

while True:
    print("\n Atm Menu")
    print("1: Check Balance")
    print("2: Deposit Money")
    print("3: Withdraw Money")
    print("4: Exit")

    choice = input("Enter Number Between (1-4):")

    if choice == "1":
        check_balance(balance)
    elif choice =="2":
        balance=deposit_money(balance)
    elif choice == "3":
        balance = withdraw_money(balance)
    elif choice == "4":
        print("\nThank You for using this ATM SIMULATORY! GOODBYE...")

        break
    else:
        print("\n Invalid Input! Please select from 1 to 4.")    

