import csv
from contact import Contact

class ContactManager:
    def __init__(self, filename="contacts.csv"):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to show.\n")
            return
        
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact}")

    def delete_contact(self, index):
        try:
            self.contacts.pop(index - 1)
            self.save_contacts()
        except IndexError:
            print("Invalid Index.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return
        return None

    def save_contacts(self):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "email"])
            writer.writeheader()
            writer.writerows([c.to_dict() for c in self.contacts])

    def load_contacts(self):
        try:
            with open(self.filename, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    contact = Contact(row["name"], row["phone"], row["email"])
                    self.contacts.append(contact)
        except FileNotFoundError:
            pass
















# from models import create_contact

# def add_contact(contact_list):
#     name = input("Enter name: ")
#     phone = input("Enter phone: ")
#     email = input("Enter email: ")

#     contact = create_contact(name, phone, email)
#     contact_list.append(contact)


# def view_contacts(contact_list):
#     if not contact_list:
#         print("No contacts Found.\n")
#         return
    
#     for i, contact in enumerate(contact_list, start=1):
#         print(f"{i}. {contact["name"]} - {contact["phone"]} - {contact["email"]}")
#     print()

# def search_contact(contact_list):
#     keyword = input("Search by name: ").lower()
#     results = [c for c in contact_list if keyword in c["name"].lower()]

#     if not results:
#         print("No match found.\n")

#     for contact in results:
#         print(contact)

# def delete_contact(contact_list):
#     view_contacts(contact_list)
#     try:
#         index = int(input("Enter contact number to delete: "))
#         contact_list.pop(index - 1)
#     except (ValueError, IndexError):
#         print("Invalid selection.\n")