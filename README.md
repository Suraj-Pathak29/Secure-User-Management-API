# 🚀 FastAPI Backend with PostgreSQL & Docker

A robust, production-ready REST API built with **FastAPI**, containerized with **Docker**, and deployed on **Render Cloud**.

## 🛠️ Tech Stack
- **Framework:** FastAPI
- **Database:** PostgreSQL (SQLAlchemy ORM)
- **Validation:** Pydantic
- **Security:** Bcrypt (Password Hashing)
- **Deployment:** Docker & Render

## 📂 Project Structure
- `main.py`: Application entry point and routes.
- `models.py`: Database tables (User, Task).
- `schemas.py`: Pydantic models for data validation.
- `database.py`: Database connection logic (Cloud + Local support).

## ⚡ API Endpoints

### Users
- `POST /users/` - Create a new account.
- `GET /users/` - View all users.
- `DELETE /users/{id}` - Delete a user.

### Tasks
- `POST /tasks/` - Create a task.
- `GET /tasks/` - View my tasks.
- `DELETE /tasks/{id}` - Delete a task.

## 🏃‍♂️ How to Run Locally

### Using Docker (Recommended)
1. Clone the repo.
2. Run:
   ```bash
   docker-compose up --build
   ```
3. Open browser at http://localhost:8000/docs.

### Manual Setup
1. Create a virtual environment and install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Set up your local PostgreSQL database (learning_db).
3. Create a .env file with your DB credentials.
4. Run:
    ```bash
    uvicorn main:app --reload
    ```
