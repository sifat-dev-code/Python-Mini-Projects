import os

print("📝 Welcome to the Secret Diary!")

def write_note():
    note = input("Write your secret note today: ")
    with open ("diary.txt", "a" ) as file:
        file.write(note +"\n" )
    
    
    
    print("✅ Note saved permanently!")

def read_notes():
    print("\n--- Your Secret Notes ---")
    
    
    if os.path.exists("diary.txt"):
        with open ("diary.txt", "r") as file:
            Written = file.read()
            print(Written)
       
    else:
        print("No notes found. Start writing first!")


while True:
    print("\n1. Write a Note")
    print("2. Read All Notes")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == '1':
        write_note()
    elif choice == '2':
        read_notes()
    elif choice == '3':
        print("Closing diary. Goodbye!")
        break
    else:
        print("Invalid choice!")