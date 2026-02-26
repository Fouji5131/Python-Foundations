import csv

def save_contacts(contact_list: list, filename="contacts.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "phone", "email"])
        writer.writeheader()
        writer.writerows(contact_list)


def load_contacts(filename="contacts.csv"):
    contacts = []

    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass
    return contacts