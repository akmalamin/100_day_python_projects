"""
To-Do List Manager
A command-line application to manage tasks with add, view, mark complete, and delete operations.
"""


def add_task(tasks):
    """Add a new task to the list."""
    description = input("Enter task description: ")
    new_task = {
        "description": description,
        "completed": False
    }
    tasks.append(new_task)
    print(f"✅ Task '{description}' added!")


def view_tasks(tasks):
    """Display all tasks with their status."""
    if len(tasks) == 0:
        print("📭 No tasks yet!")
        return

    print("\n📋 Your To-Do List:")
    print("-" * 40)

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. [{status}] {task['description']}")

    print("-" * 40)


def mark_complete(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to mark complete: "))
        index = task_number - 1

        if index < 0 or index >= len(tasks):
            print("❌ Invalid task number!")
            return

        tasks[index]["completed"] = True
        print(f"✅ Task '{tasks[index]['description']}' marked complete!")

    except ValueError:
        print("❌ Please enter a valid number!")


def delete_task(tasks):
    """Delete a task from the list."""
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to delete: "))
        index = task_number - 1

        if index < 0 or index >= len(tasks):
            print("❌ Invalid task number!")
            return

        task_description = tasks[index]["description"]
        del tasks[index]
        print(f"✅ Task '{task_description}' deleted!")

    except ValueError:
        print("❌ Please enter a valid number!")


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("✅ To-Do List Manager")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("=" * 40)


def main():
    """Main program loop."""
    tasks = []
    print("✅ Welcome to To-Do List Manager!")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\n👋 Goodbye! Thanks for using To-Do List Manager!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-5.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()