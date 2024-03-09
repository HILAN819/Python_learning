import json

# Function to add a new task


def add_task(tasks, title):
    task_id = len(tasks) + 1
    new_task = {"id": task_id, "title": title, "status": "To Do"}
    tasks.append(new_task)
    print(f"Task '{title}' added successfully!")

# Function to view all tasks


def view_tasks(tasks):
    print("Tasks:")
    for task in tasks:
        print(f"{task['id']}. {task['title']} - Status: {task['status']}")

# Function to update task status


def update_task_status(tasks, task_id, new_status):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = new_status
            print(f"Task {task_id} updated to '{new_status}' successfully!")
            return
    print(f"Task with ID {task_id} not found.")

# Function to delete a task


def delete_task(tasks, task_id):
    tasks[:] = [task for task in tasks if task['id'] != task_id]
    print(f"Task {task_id} deleted successfully!")

# Function to save tasks to a file


def save_tasks_to_file(tasks, file_path):
    with open(file_path, 'w') as file:
        json.dump(tasks, file)

# Function to load tasks from a file


def load_tasks_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        return []


# Main program
if __name__ == "__main__":
    tasks_file_path = "tasks.json"
    tasks = load_tasks_from_file(tasks_file_path)

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(tasks, title)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            new_status = input("Enter new status ('In Progress' or 'Done'): ")
            update_task_status(tasks, task_id, new_status)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks, task_id)
        elif choice == "5":
            save_tasks_to_file(tasks, tasks_file_path)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
