
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Python Form Collection")
root.geometry("550x650")
root.configure(bg="#eaf2f8")

fields = []
fields =  []

def clear_form():
    for widget in form_frame.winfo_children():
        widget.destroy()
    fields.clear()

def create_form():
    clear_form()
    choice = form_type.get()

    if choice == "Registration Form":
        labels = ["Full Name", "Mobile Number", "Email", "Password"]
    elif choice == "Login Form":
        labels = ["Username", "Password"]
    elif choice == "Student Admission Form":
        labels = [
            "Student Name", "Father's Name", "Age",
            "Class / Course", "Mobile Number", "Address"
        ]
    elif choice == "Contact Form":
        labels = ["Name", "Email", "Subject", "Message"]
    else:
        labels = ["Field 1", "Field 2", "Field 3", "Field 4"]

    for label in labels:
        tk.Label(
            form_frame, text=label,
            bg="#ffffff", fg="#263238",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", padx=25, pady=(10, 2))

        if label == "Message" or label == "Address":
            entry = tk.Text(form_frame, height=3, width=42)
            entry.pack(padx=25, pady=3)
        else:
            entry = tk.Entry(form_frame, width=42, show="*" if label == "Password" else "")
            entry.pack(padx=25, pady=3)

        fields.append((label, entry))

    tk.Button(
        form_frame, text="Submit Form",
        command=submit_form,
        bg="#2471a3", fg="white",
        font=("Arial", 12, "bold"),
        width=20
    ).pack(pady=25)

def submit_form():
    data = {}

    for label, widget in fields:
        if isinstance(widget, tk.Text):
            value = widget.get("1.0", "end-1c").strip()
        else:
            value = widget.get().strip()

        if not value:
            messagebox.showwarning(
                "Missing Information",
                f"Please enter {label}."
            )
            return

        data[label] = value

    result = "\n".join(
        f"{label}: {value}"
        for label, value in data.items()
    )

    messagebox.showinfo("Form Submitted", result)

    # Save submitted information in a local text file.
    with open("form_data.txt", "a", encoding="utf-8") as file:
        file.write(result + "\n" + "-" * 30 + "\n")

title = tk.Label(
    root, text="PYTHON FORM COLLECTION",
    font=("Arial", 18, "bold"),
    bg="#eaf2f8", fg="#154360"
)
title.pack(pady=20)

tk.Label(
    root, text="Select Form Type:",
    font=("Arial", 12),
    bg="#eaf2f8"
).pack()

form_type = ttk.Combobox(
    root,
    values=[
        "Registration Form",
        "Login Form",
        "Student Admission Form",
        "Contact Form",
        "Custom Form"
    ],
    state="readonly",
    width=30
)
form_type.pack(pady=10)
form_type.current(0)

tk.Button(
    root, text="Create Form",
    command=create_form,
    bg="#148f77", fg="white",
    font=("Arial", 11, "bold")
).pack(pady=8)

form_frame = tk.Frame(root, bg="#ffffff")
form_frame.pack(fill="both", expand=True, padx=20, pady=15)

create_form()
root.mainloop()
