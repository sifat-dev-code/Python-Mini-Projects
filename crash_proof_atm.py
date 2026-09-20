print(" Welcome to the Crash-Proof ATM!")

balance = 5000

while True:
    try:
        amount = int(input("Enter the withdraw:"))

        if amount > balance:
            print("Insufficient Balance!")

        else:
            balance-=amount
            print("Success")
            break 
        
        
        

    except ValueError:
        print('Error: Please enter numbers only!')
      