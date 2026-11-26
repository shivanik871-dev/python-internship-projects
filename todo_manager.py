import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        if not os.path.exists(FILE_NAME):
            return []
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Error reading file, starting with empty list.")
        return []

def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as f:
            json.dump(tasks, f, indent=4)
    except IOError:
        print("Error saving tasks!")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
        return
    print("\n--- Your To-Do List ---")
    for i, t in enumerate(tasks, 1):
        status = "✅ Done" if t["done"] else "❌ Pending"
        tag = f"[{t['tag']}]" if t.get("tag") else ""
        due = f"Due: {t['due']}" if t.get("due") else ""
        print(f"{i}. {t['title']} {tag} {due} - {status}")

def add_task(tasks):
    title = input("Enter task: ")
    tag = input("Enter tag (optional, press Enter to skip): ")
    due = input("Enter due date (optional, e.g. 25-11-2026): ")
    tasks.append({"title": title, "done": False, "tag": tag, "due": due})
    save_tasks(tasks)
    print("Task added!")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['title']}")
    except (ValueError, IndexError):
        print("Invalid task number!")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Marked as done!")
    except (ValueError, IndexError):
        print("Invalid task number!")

# Main Menu Loop
tasks = load_tasks()

while True:
    print("\n===== TO-DO MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Choose (1-5): ")
    
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        mark_done(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        print("Goodbye! Tasks saved.")
        break
    else:
        print("Invalid choice!")