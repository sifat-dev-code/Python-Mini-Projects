print(" Welcome to the SMART Contact Book!")


contacts = {}


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name]= phone
    print(f" Contact '{name}' saved successfully!") 
  


def view_contacts():
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts found")

    else:
        for key, value in contacts.items():
            print(key, value)
            


def search_contact():
    search_name = input("Enter name to search: ")
    if search_name in contacts:
        print(f"\n Name: {search_name} | Number: {contacts[search_name]}")
    else:
        print("Contact not found")
    
    


while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        print("\n Exiting Contact Book. Goodbye!")
        break
    else:
        print("\n Invalid Input! Please try again.")