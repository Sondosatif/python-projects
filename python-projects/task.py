class Task:
    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
    def display_task(self):
        print(f"Task: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}")

    def mark_as_complete(self, new_status):
        self.status = new_status
        print(f"Status updated to: {self.status}")


task1=Task("Review Syntax", "Review how to create a class and an object", "2024-12-31", "Incomplete")
task1.display_task()

new_status = input("Enter new status for the task: ")
task1.mark_as_complete(new_status)