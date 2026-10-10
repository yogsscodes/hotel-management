import tkinter as tk
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college"
)

cur = db.cursor()


# Function to add student
def add_student():
    student_id = entry_id.get()
    name = entry_name.get()
    marks = entry_marks.get()

    if student_id == "" or name == "" or marks == "":
        result.config(text="Please enter all details")
        return

    cur.execute(
        "INSERT INTO student (student_id, name, marks) VALUES (%s, %s, %s)",
        (student_id, name, marks)
    )

    db.commit()
    result.config(text="Student added successfully")

    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_marks.delete(0, tk.END)


# Function to view students
def view_students():
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()

    result.config(text="")

    for row in rows:
        result.config(text=result.cget("text") + str(row) + "\n")


# Create main window
root = tk.Tk()
root.title("Student Management System")

# Student ID
tk.Label(root, text="Student ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

# Student Name
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

# Student Marks
tk.Label(root, text="Marks").pack()
entry_marks = tk.Entry(root)
entry_marks.pack()

# Add Student button
tk.Button(
    root,
    text="Add Student",
    command=add_student
).pack()

# View Students button
tk.Button(
    root,
    text="View Students",
    command=view_students
).pack()

# Result display
result = tk.Label(root, text="")
result.pack()

# Run application
root.mainloop()