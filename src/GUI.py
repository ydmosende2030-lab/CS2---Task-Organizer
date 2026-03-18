import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

SAVE_FILE = 'tasks_data.json'



def load_tasks():
    try:
        with open(SAVE_FILE, 'r') as f:
            return json.load(f)
    except:
        return []


def save_tasks(tasks):
    with open(SAVE_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)


def sort_tasks(tasks):
    def task_key(task):
        if task.get('deadline'):
            try:
                return datetime.strptime(task['deadline'], '%d/%m/%Y')
            except:
                return datetime.max
        return datetime.max

    return sorted(tasks, key=task_key)


def refresh_list():
    listbox.delete(0, tk.END)
    tasks = load_tasks()
    sorted_tasks = sort_tasks(tasks)

    urgency_colors = {
        "Urgent": "#e74c3c",  # Red
        "Close": "#f1c40f",  # Yellow
        "Safe": "#2ecc71",  # Green
        "No Priority": "#ffffff"  # White
    }

    for t in sorted_tasks:
        display_text = f"{t['task']} | Due: {t['deadline']} | {t['progress']}"
        listbox.insert(tk.END, display_text)

        idx = listbox.size() - 1
        level = t.get('urgency', "No Priority")
        hex_color = urgency_colors.get(level, "#ffffff")

        listbox.itemconfig(idx, {'fg': hex_color})


def add_task_gui():
    name = entry_task.get()
    date = entry_date.get()
    prog = entry_prog.get()
    urgency_choice = urgency_var.get()

    if not name:
        messagebox.showwarning("Input Error", "Task name is required!")
        return

    tasks = load_tasks()
    tasks.append({
        'task': name,
        'deadline': date if date else "None",
        'progress': prog,
        'urgency': urgency_choice
    })

    save_tasks(sort_tasks(tasks))
    messagebox.showinfo("Success", f"Task categorized as: {urgency_choice}")
    clear_fields()
    refresh_list()


def complete_task_gui():
    try:
        selection = listbox.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "Select a task to mark as done.")
            return

        selected_text = listbox.get(selection[0])
        task_name = selected_text.split(" | ")[0]

        tasks = load_tasks()
        new_tasks = [t for t in tasks if t['task'] != task_name]

        save_tasks(new_tasks)
        messagebox.showinfo("Done", f"'{task_name}' removed from active list.")
        refresh_list()
    except Exception as e:
        messagebox.showerror("Error", f"Action failed: {e}")


def clear_fields():
    entry_task.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_prog.delete(0, tk.END)
    urgency_var.set("Safe")


root = tk.Tk()
root.title("Task Organizer")
root.geometry("500x650")
root.config(bg="#2c3e50")

tk.Label(root, text="Task Organizer", font=("Arial", 18, "bold"), bg="#2c3e50", fg="white").pack(pady=10)

input_frame = tk.Frame(root, bg="#2c3e50")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Task Name:", bg="#2c3e50", fg="white").grid(row=0, column=0, sticky="w")
entry_task = tk.Entry(input_frame, width=30)
entry_task.grid(row=0, column=1, pady=2)

tk.Label(input_frame, text="Deadline (DD/MM/YYYY):", bg="#2c3e50", fg="white").grid(row=1, column=0, sticky="w")
entry_date = tk.Entry(input_frame, width=30)
entry_date.grid(row=1, column=1, pady=2)

tk.Label(input_frame, text="Status/Progress:", bg="#2c3e50", fg="white").grid(row=2, column=0, sticky="w")
entry_prog = tk.Entry(input_frame, width=30)
entry_prog.grid(row=2, column=1, pady=2)

# Urgency Status Selection
tk.Label(input_frame, text="Urgency Status:", bg="#2c3e50", fg="white").grid(row=3, column=0, sticky="w")
urgency_var = tk.StringVar(root)
urgency_var.set("Safe")
urgency_options = [
    "Urgent",
    "Close",
    "Safe",
    "No Priority"
]
urgency_menu = tk.OptionMenu(input_frame, urgency_var, *urgency_options)
urgency_menu.config(width=25, bg="#34495e", fg="white")
urgency_menu.grid(row=3, column=1, pady=5)

tk.Label(root, text="Active Task Dashboard", bg="#2c3e50", fg="#3498db", font=("Arial", 10, "bold")).pack()
listbox = tk.Listbox(root, width=60, height=12, bg="#34495e", fg="white", font=("Courier", 10))
listbox.pack(pady=10, padx=20)

btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Task", command=add_task_gui, bg="#3498db", fg="white", width=15).grid(row=0, column=0,
                                                                                                     padx=5, pady=5)
tk.Button(btn_frame, text="Mark Done", command=complete_task_gui, bg="#2ecc71", fg="white", width=15).grid(row=0,
                                                                                                           column=1,
                                                                                                           padx=5,
                                                                                                           pady=5)
tk.Button(btn_frame, text="Refresh View", command=refresh_list, bg="#f1c40f", fg="black", width=15).grid(row=1,
                                                                                                         column=0,
                                                                                                         padx=5, pady=5)
tk.Button(btn_frame, text="Exit", command=root.destroy, bg="#e74c3c", fg="white", width=15).grid(row=1, column=1,
                                                                                                 padx=5, pady=5)

refresh_list()
root.mainloop()
