import random
print("Welcome to the SMART Password Generator!")


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

while True:
        lenth_number = input("Enter the lenth of the number,(or type 'exit' to quit): ")
        if lenth_number == 'exit':
            break

        lenth= int(lenth_number)

        password =""



        for i in range(lenth):
            password+=random.choice(chars)

        print(password)
