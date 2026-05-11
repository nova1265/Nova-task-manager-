import random
import time

tasks = []

def show_menu():
    print("\n===== NOVA TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Random Motivation")
    print("6. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYOUR TASKS:")
    for i, t in enumerate(tasks):
        status = "✓" if t["done"] else "✗"
        print(f"{i+1}. {t['task']} [{status}]")

def complete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to complete: "))
        tasks[num-1]["done"] = True
        print("Task completed!")
    except:
        print("Invalid input.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num-1)
        print(f"Deleted: {removed['task']}")
    except:
        print("Invalid input.")

def motivation():
    quotes = [
        "Keep learning every day.",
        "Small progress is still progress.",
        "Consistency beats motivation.",
        "Build. Break. Learn. Repeat.",
        "Dream big and start small."
    ]

    print("\n" + random.choice(quotes))

while True:
    show_menu()

    choice = input("Choose option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        motivation()

    elif choice == "6":
        print("Goodbye!")
        time.sleep(1)
        break

    else:
        print("Invalid choice.")
