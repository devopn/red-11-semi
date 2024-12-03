import json
from datetime import datetime


class Task:
    def __init__(self, task_id, title, description="", done=False, priority="Средний", due_date=None):
        self.id = task_id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
            "priority": self.priority,
            "due_date": self.due_date,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            task_id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            done=data.get("done", False),
            priority=data.get("priority", "Средний"),
            due_date=data.get("due_date"),
        )


class TaskManager:
    FILE_NAME = "tasks.json"

    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Task.from_dict(task) for task in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in self.tasks], file, ensure_ascii=False, indent=4)

    def create_task(self, title, description="", priority="Средний", due_date=None):
        new_id = max((task.id for task in self.tasks), default=0) + 1
        new_task = Task(task_id=new_id, title=title, description=description, priority=priority, due_date=due_date)
        self.tasks.append(new_task)
        self.save_tasks()
        return new_task

    def list_tasks(self, filter_by=None):
        if filter_by:
            return [task for task in self.tasks if filter_by(task)]
        return self.tasks

    def get_task_by_id(self, task_id):
        return next((task for task in self.tasks if task.id == task_id), None)

    def update_task(self, task_id, title=None, description=None, done=None, priority=None, due_date=None):
        task = self.get_task_by_id(task_id)
        if task:
            if title:
                task.title = title
            if description:
                task.description = description
            if done is not None:
                task.done = done
            if priority:
                task.priority = priority
            if due_date:
                task.due_date = due_date
            self.save_tasks()
            return task
        return None

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()

    def export_to_csv(self, filename):
        import csv

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "description", "done", "priority", "due_date"])
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(task.to_dict())

    def import_from_csv(self, filename):
        import csv

        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.create_task(
                    title=row["title"],
                    description=row.get("description", ""),
                    priority=row.get("priority", "Средний"),
                    due_date=row.get("due_date"),
                )
