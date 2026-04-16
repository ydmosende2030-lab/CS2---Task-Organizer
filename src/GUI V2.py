import tkinter as tk
from tkinter import messagebox, colorchooser
import json
from datetime import datetime

SAVE_FILE = 'tasks_data.json'

#theme
theme = {
    "bg": "#2b2d31",
    "card": "#313338",
    "accent": "#89b4fa",
    "text": "#e0e0e0",
    "muted": "#a6adc8"
}

urgency_colors = {
    "Urgent": "#d16d6d",       # muted red
    "Close": "#d1b56d",        # muted yellow
    "Safe": "#7fb77e",         # muted green
    "No Priority": "#cdd6f4"
}

# --
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

#functions
def refresh_list():
    listbox.delete(0, tk.END)
    tasks = sort_tasks(load_tasks())

    for t in tasks:
        display_text = f"{t['task']} | Due: {t['deadline']} | {t['progress']}"
        listbox.insert(tk.END, display_text)

        idx = listbox.size() - 1
        color = urgency_colors.get(t.get('urgency', "No Priority"))
        listbox.itemconfig(idx, {'fg': color})

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
    clear_fields()
    refresh_list()

def complete_task_gui():
    try:
        selection = listbox.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "Select a task.")
            return

        selected_text = listbox.get(selection[0])
        task_name = selected_text.split(" | ")[0]

        tasks = load_tasks()
        tasks = [t for t in tasks if t['task'] != task_name]

        save_tasks(tasks)
        refresh_list()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_fields():
    entry_task.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_prog.delete(0, tk.END)
    urgency_var.set("Safe")

#change background
def change_bg():
    color = colorchooser.askcolor(title="Choose Background")[1]
    if color:
        theme["bg"] = color
        apply_theme()

def apply_theme():
    root.config(bg=theme["bg"])
    for frame in [input_frame, btn_frame]:
        frame.config(bg=theme["bg"])

    for widget in root.winfo_children():
        try:
            widget.config(bg=theme["bg"], fg=theme["text"])
        except:
            pass

#main interface
root = tk.Tk()
root.title("Task Organizer")
root.geometry("520x680")
root.config(bg=theme["bg"])

#title
tk.Label(root, text="Task Organizer",
         font=("Segoe UI", 20, "bold"),
         bg=theme["bg"], fg=theme["accent"]).pack(pady=15)

#input Frame
input_frame = tk.Frame(root, bg=theme["bg"])
input_frame.pack(pady=10)

def styled_label(parent, text, row):
    tk.Label(parent, text=text, bg=theme["bg"], fg=theme["muted"],
             font=("Segoe UI", 10)).grid(row=row, column=0, sticky="w", pady=3)

def styled_entry(parent, row):
    e = tk.Entry(parent, width=30, relief="flat",
                 bg=theme["card"], fg=theme["text"],
                 insertbackground="white")
    e.grid(row=row, column=1, pady=3, ipady=4)
    return e

styled_label(input_frame, "Task Name:", 0)
entry_task = styled_entry(input_frame, 0)

styled_label(input_frame, "Deadline (DD/MM/YYYY):", 1)
entry_date = styled_entry(input_frame, 1)

styled_label(input_frame, "Progress:", 2)
entry_prog = styled_entry(input_frame, 2)

#dropdown
styled_label(input_frame, "Urgency:", 3)
urgency_var = tk.StringVar(value="Safe")

urgency_menu = tk.OptionMenu(input_frame, urgency_var,
                             "Urgent", "Close", "Safe", "No Priority")
urgency_menu.config(bg=theme["card"], fg=theme["text"], width=25, relief="flat")
urgency_menu.grid(row=3, column=1, pady=5)

#listbox
tk.Label(root, text="Tasks",
         bg=theme["bg"], fg=theme["accent"],
         font=("Segoe UI", 11, "bold")).pack()

listbox = tk.Listbox(root, width=60, height=12,
                     bg=theme["card"], fg=theme["text"],
                     selectbackground="#44475a",
                     relief="flat")
listbox.pack(pady=10, padx=20)

#buttons
btn_frame = tk.Frame(root, bg=theme["bg"])
btn_frame.pack(pady=10)

def styled_button(parent, text, command, row, col):
    tk.Button(parent, text=text, command=command,
              bg=theme["card"], fg=theme["text"],
              activebackground=theme["accent"],
              relief="flat", width=16)\
        .grid(row=row, column=col, padx=5, pady=5)

styled_button(btn_frame, "Add Task", add_task_gui, 0, 0)
styled_button(btn_frame, "Mark Done", complete_task_gui, 0, 1)
styled_button(btn_frame, "Refresh", refresh_list, 1, 0)
styled_button(btn_frame, "Change Background", change_bg, 1, 1)

tk.Button(root, text="Exit", command=root.destroy,
          bg="#c97b7b", fg="white", relief="flat",
          width=20).pack(pady=10)

refresh_list()
root.mainloop()
