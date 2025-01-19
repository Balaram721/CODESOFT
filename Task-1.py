class ToDoList:
    def __init__(self):
        self.tasks = []

    def show_menu(self):
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def add_task(self):
        task = input("Enter the task: ")
        if task:
            self.tasks.append(task)
            print("Task added successfully.")
        else:
            print("Task cannot be empty!")

    def mark_complete(self):
        self.view_tasks()
        if self.tasks:
            try:
                task_num = int(input("Enter the task number to mark as complete: "))
                if 1 <= task_num <= len(self.tasks):
                    self.tasks[task_num - 1] += " ✔️"
                    print("Task marked as complete.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    def delete_task(self):
        self.view_tasks()
        if self.tasks:
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(self.tasks):
                    deleted_task = self.tasks.pop(task_num - 1)
                    print(f"Task '{deleted_task}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    def run(self):
        while True:
            self.show_menu()
            try:
                choice = int(input("\nEnter your choice: "))
                if choice == 1:
                    self.view_tasks()
                elif choice == 2:
                    self.add_task()
                elif choice == 3:
                    self.mark_complete()
                elif choice == 4:
                    self.delete_task()
                elif choice == 5:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please choose between 1 and 5.")
            except ValueError:
                print("Please enter a valid number.")

if __name__ == "__main__":
    app = ToDoList()
    app.run()