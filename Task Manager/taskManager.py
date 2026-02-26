import csv
from taskModel import Task
# from customErrors import InvalidPhoneError

class TaskManager:
    def __init__(self, filename="tasks.csv"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, task_id, title):
        # self.validate_phone(phone)
        
        task = Task(task_id, title, completed=False)
        
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.\n")
            return
        
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def delete_task(self, index):
        try:
            self.tasks.pop(index - 1)
            self.save_tasks()
        except IndexError:
            print("Invalid Index.")

    def complete_task(self, index):
        self.tasks[index - 1].completed = True
        

    def search_task(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                return
        return None
    
    # def validate_phone(phone):
    #     if not phone.isdigit() or len(phone) < 10:
    #         raise InvalidPhoneError("Phone number must be numeric and at least 10 digits")
    
    def sort_tasks(self):
        self.tasks.sort(key=lambda c: c.task_id)

    def save_tasks(self):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["task_id", "title", "completed"])
            writer.writeheader()
            writer.writerows([c.to_dict() for c in self.tasks])

    def load_tasks(self):
        try:
            with open(self.filename, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task = Task(row["task_id"], row["title"], row["completed"],)
                    self.tasks.append(task)
        except FileNotFoundError:
            pass












