from manager import ContactManager
# from storage import save_contacts, load_contacts

def main():
    manager = ContactManager()
    # contacts = load_contacts()

    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
 
        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            manager.add_contact(name, phone, email)

            # add_contact(contacts)
            # save_contacts(contacts)
        elif choice == "2":
            manager.view_contacts()
            # view_contacts(contacts)
        elif choice == "3":
            name = input("Search name: ")
            manager.search_contact(name)
        elif choice == "4":
            index = int(input("Enter contact number to delete: "))
            manager.delete_contact(index)
            # delete_contact(contacts)
            # save_contacts(contacts)
        elif choice == "5":
            # save_contacts(contacts)
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()