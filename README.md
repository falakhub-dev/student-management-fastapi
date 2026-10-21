# Student Management API

A Python backend application for managing student records using FastAPI and SQLite. This project implements CRUD (Create, Read, Update, Delete) operations and includes an optional AI-powered query feature using Ollama and LangChain.

## Project Overview

The Student Management API allows users to create, retrieve, update, and delete student records through REST API endpoints. SQLite is used for database storage, and FastAPI provides interactive API documentation.

The optional AI Query feature allows users to ask natural-language questions about student records using a locally running Ollama language model.

## Technologies Used

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn
- Ollama (optional AI feature)
- LangChain and LangChain Ollama (optional AI feature)

## Project Structure

```text
FastAPI/
├── app/
│   ├── routes/
│   │   ├── ai_query.py
│   │   ├── base.py
│   │   ├── create_student.py
│   │   ├── delete_student.py
│   │   ├── get_students.py
│   │   └── update_student.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
├── main.py
├── requirement.txt
├── README.md
└── .gitignore
```

## Features

- Create new student records.
- Retrieve all student records.
- Retrieve individual student records.
- Update existing student information.
- Delete student records.
- Store student information in an SQLite database.
- Provide interactive API documentation using Swagger UI.
- Optionally answer natural-language questions about student data using Ollama.

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd FastAPI
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirement.txt
```

## Running the Application

From the project root directory, run:

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

## API Documentation

Open the following URL in your browser to explore and test the endpoints:

`http://127.0.0.1:8000/docs`

### Main CRUD Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/students/` | Create a student |
| GET | `/students/` | Retrieve student records |
| GET | `/students/{student_id}` |