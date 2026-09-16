import random
print("Welcome To The Guessing Game!!")
print("I am thinking of a number in between 1 to 100...")

secret_number = random.randint(1,100)

while True:
    guess = int(input("Enter your guessing number: "))
    
    if guess<secret_number:
        print("Number is too low!, Try again....")

    elif guess>secret_number:
        print("Number is too high!, Try again....")

    elif guess == secret_number:
        print("Congratulations! You guessed it right..")
    
        break
    
    else:
        print("Number not found..")
