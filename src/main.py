import datetime
import time

tasks = []

def add_task():
    name = input("Task Name: ")
    date_str = input("Deadline (YYYY-MM-DD): ")
    try:
        clean_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        tasks.append({"title": name, "date": clean_date, "completed": False})
        print("Success.")
    except ValueError:
        print("Invalid date.")

def view_tasks():
    if not tasks:
        print("List empty.")
        return
    for i, t in enumerate(tasks, 1):
        status = "[X]" if t["completed"] else "[ ]"
        print(f"{i}. {status} {t['title']} | {t['date']}")

def mark_done():
    view_tasks()
    if not tasks: return
    try:
        index = int(input("Number: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("Updated.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a number.")

def show_urgent():
    today = datetime.date.today()
    found = False
    for t in tasks:
        days_left = (t["date"] - today).days
        if 0 <= days_left <= 3 and not t["completed"]:
            print(f"URGENT: {t['title']} ({days_left} days left)")
            found = True
    if not found:
        print("Nothing urgent.")

def delete_task():
    view_tasks()
    if not tasks: return
    try:
        index = int(input("Number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted {removed['title']}.")
    except ValueError:
        print("Enter a number.")

while True:
    print("\n1. Add Task \n2. View Tasks \n3. Mark Task Done \n4. Urgent Tasks \n5. Delete Task \n6. Exit")
    
    choice = input("> ")

    if not choice:
        time.sleep(0.1)
        continue

    if choice == "1": 
        add_task()
    elif choice == "2": 
        view_tasks()
    elif choice == "3": 
        mark_done()
    elif choice == "4": 
        show_urgent()
    elif choice == "5": 
        delete_task()
    elif choice == "6":
        print("Goodbye!")
        break
    else: 
        print("Invalid choice, try again.")
