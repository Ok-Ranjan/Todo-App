# StudySync - Todo App

A clean and lightweight **Todo Management Application** built to help students and professionals organize their tasks efficiently.

User can seamlessly create, update, status-toggle, and delete tasks dynamically.

---

## Features Checklist

* **Task Management**
    * Create new task with detailed titles and descriptions.
    * Update existing tasks.
    * Toggle status instantly (Mark as Completed or Uncompleted)
    * Secure deletion workflow using safe POST requests.

* **UI & Security**
    * Full CSRF protection on all form submissions.
    * Responsive layout styled with **Bootstrap** components.

---

## Built with

* **Backend Framework:** Django (Python)
* **Frontend styling:** HTML5, Bootstap 5
* **Database:** Sqlite3 (django default) 

## Getting Started

Follow these steps to get your local development environment up and running:

### 1. Clone the repository
```bash
git clone https://github.com
cd "StudySync"
```

### 2. Setup Virtual Environment
```bash
# Create the environment
python -m venv venv

# Activate it (Windows / Bash)
source venv/Scripts/activate
```

### 3. Install Dependencies & Run Databese Migrations
```bash
pip install -r requirements.txt
python manage.py migrate
```

### 4. Lunch the Development Server
```bash
python manage.py runserver
```

open your browser and navigate to `http://127.0.0` to explore the app!

---

## 