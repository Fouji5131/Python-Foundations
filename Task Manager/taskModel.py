class Task:
    def __init__(self, task_id, title, completed=False):
        self.task_id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "completed": self.completed,
            "task_id": self.task_id,
            "title": self.title
        }

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.task_id} - {self.title}"