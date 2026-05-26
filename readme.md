# ✅ Todo List Django

A lightweight yet fully functional **Django-based task management application** designed for personal productivity and daily workflow organization. This app allows users to create, manage, and categorize tasks using a flexible tagging system, with real-time status toggling and a clean Bootstrap 5 interface.

---

## 🚀 Key Features

### 📋 Task Management Interface
Full lifecycle control over your tasks:

- Create tasks with optional deadlines  
- Update or delete existing tasks  
- View creation timestamps and due dates  
- Display all relevant task metadata in a clean list layout  

### 🔁 One-Click Status Toggle
Instant task completion control:

- Mark tasks as **Done** with a single click  
- **Undo** completion to revert task status  
- Tasks automatically reorder based on completion state  

### 🏷️ Flexible Tagging System
Organize tasks with a many-to-many tag structure:

- Assign multiple tags to any task  
- One tag can span multiple tasks  
- Full CRUD operations for tag management  

### 📊 Smart Task Ordering
Tasks are automatically sorted by:

- Status: **Not done** tasks always appear first  
- Recency: newer tasks appear before older ones within each group  

### 🛡️ Clean & Minimal Architecture
Straightforward Django patterns including:

- Class-Based Views (CBVs) throughout  
- Reusable base template with persistent sidebar  
- Bootstrap 5 responsive layout  

---

## 🛠️ Technology Stack

| Layer | Technology |
|--------|------------|
| **Backend** | Django 5.x |
| **Language** | Python 3.11+ |
| **Database** | SQLite (Development) |
| **Frontend** | Bootstrap 5 |
| **Testing** | Django Unit Testing |

---

## 📦 Local Installation & Setup

Follow these steps to run the application locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/todo-list-django.git
cd todo-list-django
```

### 2️⃣ Configure the Virtual Environment

#### Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Execute Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create an Admin Account

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

Open your browser and access:

```text
http://127.0.0.1:8000/
```

---

## 🧪 Running Tests

This repository includes automated test coverage validating:

- Task list page rendering  
- Correct task ordering (not done → done)  
- Toggle done/undo functionality and redirect behavior  
- Tag list page rendering  
- Task and tag CRUD operations  

To run the test suite:

```bash
python manage.py test
```

---

## 📂 Project Structure

```plaintext
todo-list-django/
│
├── todo_list/              # Global settings and root URL configuration
│
└── tasks/
    ├── forms.py            # Task and Tag forms
    ├── models.py           # Task and Tag models
    ├── tests.py            # Automated test suite
    ├── views.py            # Class-Based Views (CBVs) and toggle view
    ├── urls.py             # App URL routing
    └── templates/
        └── tasks/
            ├── base.html               # Shared layout with sidebar
            ├── task_list.html          # Home page — task listing
            ├── task_form.html          # Create / Update task
            ├── task_confirm_delete.html
            ├── tag_list.html           # Tag management page
            ├── tag_form.html           # Create / Update tag
            └── tag_confirm_delete.html
```

---

## 🎯 Project Goals

The purpose of **Todo List Django** is to provide a simple and extensible task management environment where users can:

- Organize daily tasks with clear status tracking  
- Categorize work using a flexible tag system  
- Stay focused with deadline visibility  
- Navigate a clean, distraction-free interface  

---

## 📄 License

This project is intended for **educational and portfolio purposes**.

Feel free to fork, modify, and expand upon it.

---

## 👨‍💻 Author

Developed as part of a professional Django portfolio focused on:

- Backend engineering  
- Task and productivity applications  
- Clean URL routing and CBV architecture  
- Automated testing practices
