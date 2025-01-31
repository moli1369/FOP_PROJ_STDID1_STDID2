import tkinter as tk
from tkinter import messagebox
from user_management import register, login
from course_management import create_course, add_student_to_course

def student_login():
    user_id = entry_user_id.get()
    password = entry_password.get()
    user = login(user_id, password)
    if user:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid credentials")

def professor_login():
    user_id = entry_user_id.get()
    password = entry_password.get()
    user = login(user_id, password)
    if user and user['type'] == 'professor':
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid credentials")

def register_user():
    user_type = user_type_var.get()
    user_id = entry_user_id.get()
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    phone = entry_phone.get()
    if register(user_type, user_id, name, email, password, phone):
        messagebox.showinfo("Success", "Registration successful!")
    else:
        messagebox.showerror("Error", "User already exists")

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("LMS System")

# فیلدهای ورودی
tk.Label(root, text="User ID:").grid(row=0, column=0)
entry_user_id = tk.Entry(root)
entry_user_id.grid(row=0, column=1)

tk.Label(root, text="Password:").grid(row=1, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

tk.Label(root, text="Name:").grid(row=2, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=2, column=1)

tk.Label(root, text="Email:").grid(row=3, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1)

tk.Label(root, text="Phone:").grid(row=4, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=4, column=1)

# انتخاب نوع کاربر
user_type_var = tk.StringVar(value="student")
tk.Radiobutton(root, text="Student", variable=user_type_var, value="student").grid(row=5, column=0)
tk.Radiobutton(root, text="Professor", variable=user_type_var, value="professor").grid(row=5, column=1)

# دکمه‌ها
tk.Button(root, text="Login as Student", command=student_login).grid(row=6, column=0)
tk.Button(root, text="Login as Professor", command=professor_login).grid(row=6, column=1)
tk.Button(root, text="Register", command=register_user).grid(row=7, column=0, columnspan=2)

root.mainloop()