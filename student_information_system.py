import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# --- Data Handling ---
DATA_FILE = "student_data.json"

def load_data():
    """Loads student data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_data(data):
    """Saves student data to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- CLI Mode ---

def add_student_cli(data):
    """Adds a new student record in CLI mode."""
    student_id = input("Enter Student ID: ")
    if student_id in data:
        print("Error: Student ID already exists.")
        return
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    try:
        marks_str = input("Enter marks (comma-separated): ")
        marks = [int(mark.strip()) for mark in marks_str.split(',')]
    except ValueError:
        print("Error: Invalid marks. Please enter numbers only.")
        return

    data[student_id] = {
        "name": name,
        "department": department,
        "marks": marks
    }
    save_data(data)
    print("Student added successfully!")

def view_students_cli(data):
    """Displays all student records in CLI mode."""
    if not data:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for student_id, info in data.items():
        print(f"ID: {student_id}, Name: {info['name']}, Dept: {info['department']}, Marks: {info['marks']}")
    print("-----------------------\n")


def update_student_cli(data):
    """Updates an existing student record in CLI mode."""
    student_id = input("Enter Student ID to update: ")
    if student_id not in data:
        print("Error: Student ID not found.")
        return

    print(f"Current data: {data[student_id]}")
    name = input(f"Enter new name (or press Enter to keep '{data[student_id]['name']}'): ")
    department = input(f"Enter new department (or press Enter to keep '{data[student_id]['department']}'): ")
    marks_str = input(f"Enter new marks (comma-separated, or press Enter to keep '{data[student_id]['marks']}'): ")

    if name:
        data[student_id]['name'] = name
    if department:
        data[student_id]['department'] = department
    if marks_str:
        try:
            data[student_id]['marks'] = [int(mark.strip()) for mark in marks_str.split(',')]
        except ValueError:
            print("Error: Invalid marks. Update failed.")
            return

    save_data(data)
    print("Student record updated successfully!")


def delete_student_cli(data):
    """Deletes a student record in CLI mode."""
    student_id = input("Enter Student ID to delete: ")
    if student_id in data:
        del data[student_id]
        save_data(data)
        print("Student deleted successfully!")
    else:
        print("Error: Student ID not found.")

def cli_mode():
    """Runs the command-line interface for the SIS."""
    student_data = load_data()
    while True:
        print("\n--- Student Information System (CLI) ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student_cli(student_data)
        elif choice == '2':
            view_students_cli(student_data)
        elif choice == '3':
            update_student_cli(student_data)
        elif choice == '4':
            delete_student_cli(student_data)
        elif choice == '5':
            print("Exiting CLI mode.")
            break
        else:
            print("Invalid choice. Please try again.")

# --- GUI Mode ---

class StudentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Information System")
        self.geometry("600x400")
        self.configure(bg="#f0f0f0")

        self.data = load_data()

        # --- Frames ---
        control_frame = tk.Frame(self, bg="#d0d0d0", padx=10, pady=10)
        control_frame.pack(side=tk.LEFT, fill=tk.Y)

        display_frame = tk.Frame(self, bg="#f0f0f0", padx=10, pady=10)
        display_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # --- Widgets ---
        tk.Label(control_frame, text="Student ID:", bg="#d0d0d0").grid(row=0, column=0, sticky="w", pady=2)
        self.id_entry = tk.Entry(control_frame)
        self.id_entry.grid(row=0, column=1, pady=2)

        tk.Label(control_frame, text="Name:", bg="#d0d0d0").grid(row=1, column=0, sticky="w", pady=2)
        self.name_entry = tk.Entry(control_frame)
        self.name_entry.grid(row=1, column=1, pady=2)

        tk.Label(control_frame, text="Department:", bg="#d0d0d0").grid(row=2, column=0, sticky="w", pady=2)
        self.dept_entry = tk.Entry(control_frame)
        self.dept_entry.grid(row=2, column=1, pady=2)

        tk.Label(control_frame, text="Marks (comma-sep):", bg="#d0d0d0").grid(row=3, column=0, sticky="w", pady=2)
        self.marks_entry = tk.Entry(control_frame)
        self.marks_entry.grid(row=3, column=1, pady=2)

        # --- Buttons ---
        button_style = {"bg": "#4CAF50", "fg": "white", "relief": "raised", "borderwidth": 2, "width": 15}
        tk.Button(control_frame, text="Add Student", command=self.add_student, **button_style).grid(row=4, column=0, columnspan=2, pady=5)
        tk.Button(control_frame, text="Update Student", command=self.update_student, **button_style).grid(row=5, column=0, columnspan=2, pady=5)
        tk.Button(control_frame, text="Delete Student", command=self.delete_student, **button_style).grid(row=6, column=0, columnspan=2, pady=5)
        tk.Button(control_frame, text="Clear Fields", command=self.clear_fields, **button_style).grid(row=7, column=0, columnspan=2, pady=5)


        # --- Display Area ---
        self.student_list = tk.Listbox(display_frame, bg="white", selectbackground="#a6a6a6")
        self.student_list.pack(fill=tk.BOTH, expand=True)
        self.student_list.bind('<<ListboxSelect>>', self.on_student_select)


        self.refresh_list()

    def refresh_list(self):
        self.student_list.delete(0, tk.END)
        for student_id, info in self.data.items():
            self.student_list.insert(tk.END, f"{student_id}: {info['name']}")

    def add_student(self):
        student_id = self.id_entry.get()
        name = self.name_entry.get()
        department = self.dept_entry.get()
        marks_str = self.marks_entry.get()

        if not all([student_id, name, department, marks_str]):
            messagebox.showerror("Error", "All fields are required.")
            return

        if student_id in self.data:
            messagebox.showerror("Error", "Student ID already exists.")
            return

        try:
            marks = [int(mark.strip()) for mark in marks_str.split(',')]
        except ValueError:
            messagebox.showerror("Error", "Invalid marks format.")
            return

        self.data[student_id] = {"name": name, "department": department, "marks": marks}
        save_data(self.data)
        self.refresh_list()
        self.clear_fields()
        messagebox.showinfo("Success", "Student added successfully!")

    def update_student(self):
        selected = self.student_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Please select a student to update.")
            return
        
        selected_item = self.student_list.get(selected)
        student_id = selected_item.split(':')[0]

        name = self.name_entry.get()
        department = self.dept_entry.get()
        marks_str = self.marks_entry.get()
        
        if not all([name, department, marks_str]):
            messagebox.showerror("Error", "All fields are required for an update.")
            return

        try:
            marks = [int(mark.strip()) for mark in marks_str.split(',')]
        except ValueError:
            messagebox.showerror("Error", "Invalid marks format.")
            return

        self.data[student_id] = {"name": name, "department": department, "marks": marks}
        save_data(self.data)
        self.refresh_list()
        self.clear_fields()
        messagebox.showinfo("Success", "Student updated successfully!")


    def delete_student(self):
        selected = self.student_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Please select a student to delete.")
            return

        selected_item = self.student_list.get(selected)
        student_id = selected_item.split(':')[0]
        
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete student {student_id}?"):
            del self.data[student_id]
            save_data(self.data)
            self.refresh_list()
            self.clear_fields()
            messagebox.showinfo("Success", "Student deleted successfully!")

    def on_student_select(self, event):
        selected = self.student_list.curselection()
        if not selected:
            return

        selected_item = self.student_list.get(selected)
        student_id = selected_item.split(':')[0]
        student_info = self.data.get(student_id)

        if student_info:
            self.clear_fields()
            self.id_entry.insert(0, student_id)
            self.name_entry.insert(0, student_info['name'])
            self.dept_entry.insert(0, student_info['department'])
            self.marks_entry.insert(0, ", ".join(map(str, student_info['marks'])))

    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.dept_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)

def gui_mode():
    """Runs the graphical user interface for the SIS."""
    app = StudentApp()
    app.mainloop()

# --- Main Program ---
def main():
    """Main function to choose between CLI and GUI modes."""
    while True:
        print("\nWelcome to the Student Information System")
        print("1. Command-Line Interface (CLI)")
        print("2. Graphical User Interface (GUI)")
        print("3. Exit")
        choice = input("Choose your mode: ")

        if choice == '1':
            cli_mode()
        elif choice == '2':
            gui_mode()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
