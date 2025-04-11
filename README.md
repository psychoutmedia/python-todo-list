✅ Python CLI Todo List App
A simple, interactive command-line To-Do list manager built with Python.
Add, view, edit, complete, and delete your tasks — with persistent storage using a JSON file.

📦 Features
📝 Add new Todo items

👀 View all tasks

✅ Mark tasks as completed

🧽 Remove completed or unwanted tasks

✏️ Edit existing tasks

💾 Persistent storage via todo_data.json

🚀 Getting Started
Prerequisites
Python 3.x installed

No external libraries required (uses only os and json)

Run the App
bash
Copy
Edit
python todo.py
Replace todo.py with the actual file name if different.

🧠 How It Works
Tasks are saved as a list of dictionaries in a todo_data.json file like so:

json
Copy
Edit
[
{
"task": "Buy groceries",
"completed": false
},
{
"task": "Read 10 pages of a book",
"completed": true
}
]
When you run the program again, it automatically loads your existing todos from the file.

📘 Menu Options
text
Copy
Edit
-----The Python CLI Todo List Application -----

1. View all Todo's
2. Add a new Todo
3. Mark Todo as completed
4. Remove a Todo
5. Edit Todo
6. Save and Exit

📁 File Structure
bash
Copy
Edit
todo.py # Main Python file
todo_data.json # Automatically created/updated with your tasks

🧑‍💻 Author
M.Stephenson
