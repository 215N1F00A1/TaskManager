# 🗂️ Task Manager

A web-based Task Management System built with Django for organizing tasks across multiple departments like HR, Technical, Marketing, and Training. It supports task creation, assignment, due dates, and tracking statuses.

---

## 🚀 Features

- 🔹 Create and manage tasks
- 🏢 Department-wise task organization (HR, Technical, Marketing, etc.)
- ✅ Status tracking (Not Started, In Progress, Completed, Blocked, On Hold)
- 👤 Assign tasks to team members
- 📅 Set due dates for tasks
- 🔍 Dashboard to view all tasks

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (default) / MySQL (optional)
- **Frontend:** HTML, CSS, Bootstrap (optional)
- **Version Control:** Git + GitHub

---

## 📂 Project Structure

taskmanager/
│
├── taskmanager/ # Main Django project settings
│
├── tasks/ # Main app: models, views, urls
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/
│ └── tasks/
│ └── *.html
│
├── db.sqlite3 # Default database
├── manage.py
└── requirements.txt # Python dependencies

yaml
Copy
Edit

---

## ⚙️ How to Run Locally

1. **Clone the repo:**

   ```bash
   git clone https://github.com/your-username/TaskManager.git
   cd TaskManager
Create a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run migrations:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Run the server:

bash
Copy
Edit
python manage.py runserver
Visit:
http://127.0.0.1:8000
