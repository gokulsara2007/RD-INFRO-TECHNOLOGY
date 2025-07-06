import json
import os

TASKS_FILE = "tasks.json"

# Load existing tasks if file exists
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks):
        status = "✔️" if task["completed"] else "❌"
        print(f"{idx + 1}. {task['title']} [{status}]")

# Add a task
def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "completed": False})
    print("Task added successfully!")

# Mark task as complete
def complete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"Deleted task: {deleted['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
