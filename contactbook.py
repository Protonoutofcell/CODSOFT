import tkinter as tk
from tkinter import messagebox, ttk

class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Full Screen Contact Book")
        
        try:
            self.root.state('zoomed')
        except:
            
            self.root.attributes('-fullscreen', True)
        
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        self.contacts = []
        self.setup_ui()

    def setup_ui(self):
        self.root.configure(bg="#2b2b2b")

        self.root.columnconfigure(0, weight=1) 
        self.root.columnconfigure(1, weight=3)
        self.root.rowconfigure(0, weight=1)

        input_frame = tk.LabelFrame(self.root, text=" Contact Details ", padx=20, pady=20, 
                                   fg="white", bg="#3c3f41", font=('Arial', 12, 'bold'))
        input_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        
        input_frame.columnconfigure(1, weight=1)

        fields = [("Name:", "name"), ("Phone:", "phone"), ("Email:", "email"), ("Address:", "address")]
        self.entries = {}

        for i, (label_text, key) in enumerate(fields):
            tk.Label(input_frame, text=label_text, fg="white", bg="#3c3f41", font=('Arial', 10)).grid(row=i, column=0, sticky="w", pady=10)
            entry = tk.Entry(input_frame, bg="#2b2b2b", fg="white", insertbackground="white", font=('Arial', 11))
            entry.grid(row=i, column=1, sticky="ew", pady=10, padx=5)
            self.entries[key] = entry

        btn_container = tk.Frame(input_frame, bg="#3c3f41")
        btn_container.grid(row=4, column=0, columnspan=2, pady=30, sticky="ew")
        btn_container.columnconfigure((0,1), weight=1)

        tk.Button(btn_container, text="ADD CONTACT", bg="#4CAF50", fg="red", height=2, command=self.add_contact).grid(row=0, column=0, padx=5, sticky="ew")
        tk.Button(btn_container, text="UPDATE", bg="#2196F3", fg="red", height=2, command=self.update_contact).grid(row=0, column=1, padx=5, sticky="ew")
        
        tk.Button(input_frame, text="DELETE SELECTED", bg="#f44336", fg="red", height=2, command=self.delete_contact).grid(row=5, column=0, columnspan=2, sticky="ew", pady=5)
        tk.Button(input_frame, text="CLEAR FIELDS", bg="#757575", fg="red", height=2, command=self.clear_entries).grid(row=6, column=0, columnspan=2, sticky="ew", pady=5)

        list_frame = tk.Frame(self.root, bg="#2b2b2b")
        list_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(1, weight=1)

        tk.Label(list_frame, text="Search Contact (Name or Phone):", fg="#bbbbbb", bg="#2b2b2b").grid(row=0, column=0, sticky="w")
        self.ent_search = tk.Entry(list_frame, bg="#3c3f41", fg="white", font=('Arial', 14))
        self.ent_search.grid(row=1, column=0, sticky="ew", pady=(5, 15))
        self.ent_search.bind("<KeyRelease>", self.search_contact)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#313335", foreground="white", fieldbackground="#313335", rowheight=30, font=('Arial', 11))
        style.map("Treeview", background=[('selected', '#4b6eaf')])

        columns = ("name", "phone", "email", "address")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, anchor="center")

        self.tree.grid(row=2, column=0, sticky="nsew")
        self.tree.bind("<<TreeviewSelect>>", self.load_selected_contact)

        scroller = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroller.set)
        scroller.grid(row=2, column=1, sticky="ns")


    def add_contact(self):
        data = {k: v.get().strip() for k, v in self.entries.items()}
        if data["name"] and data["phone"]:
            self.contacts.append(data)
            self.refresh_list()
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Name and Phone are required!")

    def refresh_list(self, data_list=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
        target = data_list if data_list is not None else self.contacts
        for c in target:
            self.tree.insert("", tk.END, values=(c["name"], c["phone"], c["email"], c["address"]))

    def search_contact(self, event=None):
        query = self.ent_search.get().lower()
        results = [c for c in self.contacts if query in c['name'].lower() or query in c['phone']]
        self.refresh_list(results)

    def load_selected_contact(self, event):
        selected = self.tree.focus()
        if not selected: return
        vals = self.tree.item(selected, "values")
        self.clear_entries()
        self.entries["name"].insert(0, vals[0])
        self.entries["phone"].insert(0, vals[1])
        self.entries["email"].insert(0, vals[2])
        self.entries["address"].insert(0, vals[3])

    def update_contact(self):
        selected = self.tree.focus()
        if not selected: return
        idx = self.tree.index(selected)
        self.contacts[idx] = {k: v.get() for k, v in self.entries.items()}
        self.refresh_list()

    def delete_contact(self):
        selected = self.tree.selection()
        if not selected: return
        if messagebox.askyesno("Delete", "Remove selected contact?"):
            for item in reversed(selected): 
                idx = self.tree.index(item)
                del self.contacts[idx]
            self.refresh_list()
            self.clear_entries()

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()
