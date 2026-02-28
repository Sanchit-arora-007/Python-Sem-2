contacts = {}

while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.View 6.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif choice == 2:
        name = input("Enter name: ")
        print("Phone:", contacts.get(name, "Not found"))

    elif choice == 3:
        name = input("Enter name to update: ")
        if name in contacts:
            contacts[name] = input("New phone: ")
        else:
            print("Contact not found")

    elif choice == 4:
        name = input("Enter name to delete: ")
        contacts.pop(name, None)

    elif choice == 5:
        print(contacts)

    elif choice == 6:
        break
