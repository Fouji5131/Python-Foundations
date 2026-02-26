from taskManager import TaskManager
# from customErrors import InvalidPhoneError
# from storage import save_contacts, load_contacts

def main():
    taskManager = TaskManager()
    # contacts = load_contacts()

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Search Task")
        print("4. Delete Task")
        print("5. Complete Task")
        print("6. Exit")
 
        choice = input("Choose: ")

        if choice == "1":
            task_id = input("ID: ")
            title = input("Tilte: ")
            # email = input("Email: ")

            taskManager.add_task(task_id, title)

            # try:
            #     taskManager.add_task(task_id, title)
            # except InvalidPhoneError as e:
            #     print(e)
            # add_contact(contacts)
            # save_contacts(contacts)
        elif choice == "2":
            taskManager.view_tasks()
            # view_contacts(contacts)
        elif choice == "3":
            title = input("Search title: ")
            taskManager.search_task(title)
        elif choice == "4":
            index = int(input("Enter task id to delete: "))
            taskManager.delete_task(index)
        elif choice == "5":
            index = int(input("Enter task id to complete: "))
            taskManager.complete_task(index)
            # delete_contact(contacts)
            # save_contacts(contacts)
        elif choice == "6":
            # save_tasks(contacts)
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()