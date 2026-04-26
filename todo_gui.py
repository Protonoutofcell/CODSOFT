import tkinter as tk



def add_task():
    task = entry.get()
    if task.strip() != "" and task != "Enter Here":
        listbox.insert(tk.END, "☐ " + task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

def complete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = listbox.get(index)

       
        if task.startswith("☐"):
            new_task = task.replace("☐", "☑", 1)
            listbox.delete(index)
            listbox.insert(index, new_task)

            listbox.itemconfig(index, fg="green", font=("Arial", 16, "overstrike"))

        else:
            new_task = task.replace("☑", "☐", 1)
            listbox.delete(index)
            listbox.insert(index, new_task)

            listbox.itemconfig(index, fg="black", font=("Arial", 16))


root = tk.Tk()
root.title("To-Do List")
root.geometry("700x500")
root.configure(bg="blue")

tk.Label(root, text="To-Do List", font=("Arial", 22, "bold"),
         bg="blue").pack(pady=10)

main_frame = tk.Frame(root, bg="white")
main_frame.pack(fill="both", expand=True)

menu_frame = tk.Frame(main_frame, bg="black", bd=2, relief="solid")
menu_frame.pack(side="left", fill="y", padx=10, pady=10)

tk.Label(menu_frame, text="Menu", font=("Arial", 16, "bold"),
         bg="black").pack(pady=10)

tk.Button(menu_frame, text="Add Task", width=15, command=add_task)\
    .pack(pady=5)

tk.Button(menu_frame, text="Complete Task", width=15, command=complete_task)\
    .pack(pady=5)

tk.Button(menu_frame, text="Delete Task", width=15, command=delete_task)\
    .pack(pady=5)

right_frame = tk.Frame(main_frame, bg="black")
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

entry = tk.Entry(right_frame, font=("Arial", 14), bd=2, relief="solid")
entry.pack(pady=10, fill="x")

entry.insert(0, "ENTER HERE")

def clear_placeholder(event):
    if entry.get() == "ENTER HERE":
        entry.delete(0, tk.END)

entry.bind("<FocusIn>", clear_placeholder)

task_frame = tk.Frame(right_frame, bg="black", bd=2, relief="solid")
task_frame.pack(fill="both", expand=True)

tk.Label(task_frame, text="Tasks", font=("Arial", 14, "bold"),
         bg="black").pack()

scrollbar = tk.Scrollbar(task_frame)
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(task_frame, font=("Arial", 18),
                     yscrollcommand=scrollbar.set)

listbox.pack(fill="both", expand=True)

scrollbar.config(command=listbox.yview)

entry.bind("<Return>", lambda event: add_task())

root.mainloop()
