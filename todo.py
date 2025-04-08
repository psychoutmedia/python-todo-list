import os
import json

DATA_FILE = "todo_data.json"

def load_tasks():
    """Load tasks from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display the current list of tasks."""
    if not tasks:
        print("No Todo's found.")
        return
    for index, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['task']} - {status}")

def add_task(tasks):
    """Add a new task to the list."""
    task_text = input("Enter your new Todo: ")
    tasks.append({"task": task_text, "completed": False})
    print(f"Added Todo: {task_text}")

def mark_task_completed(tasks):
    """Mark a selected task as completed."""
    if not tasks:
        print("No Todos to mark.")
        return
    display_tasks(tasks)
    try:
        choice = int(input("Enter the Todo number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            print("Todo marked as completed.")
        else:
            print("Invalid Todo number.")
    except ValueError:
        print("Invalid input.")

def remove_task(tasks):
    """Remove a selected Todo task from the list."""
    if not tasks:
        print("No Todos to remove!")
        return
    display_tasks(tasks)
    try:
        choice = int(input("Enter the Todo number to remove: "))
        if 1 <= choice <= len(tasks):
            removed_task = tasks.pop(choice - 1)
            print(f"Removed Todo: {removed_task['task']}")
        else:
            print("Invalid Todo number.")
    except ValueError:
        print("Invalid input.")

def edit_task(tasks):
    """Edit a Todo task"""
    if not tasks:
        print("No Todos to Edit!")
        return
    display_tasks(tasks)
    try:
        choice = int(input("Enter the Todo number to Edit: "))
        if 1 <= choice <= len(tasks):
            edited_task = input("Enter the Updated Todo Description: ")
            tasks[choice - 1]["task"] = edited_task
            print("Edited Todo successfully.")
        else:
            print("Invalid Todo number.")
    except ValueError:
        print("Invalid input.")

def main():
    """Main function for Todo List App."""
    tasks = load_tasks()
    while True:
        print("\n-----The Python CLI Todo List Application -----")
        print("1. View all Todo's")
        print("2. Add a new Todo")
        print("3. Mark Todo as completed")
        print("4. Remove a Todo")
        print("5. Edit Todo")
        print("6. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            edit_task(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Todo's saved! Quitting")
            break
        else:
            print("Invalid choice, please try again.")

"""Entry Point check is script being run directly? """
if __name__ == "__main__":
    main()