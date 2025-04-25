# E-commerce with FastAPI
This is an API for a hardware store e-commerce where you can perform CRUD operations, user registration with JWT and possibly implement a payment gateway.

## The functionalities to take into account will be the following:

- ⚡ FastAPI for the Python backend API.
- 🧰 SQLModel for the Python SQL database interactions (ORM).
- 🔍 Pydantic, used by FastAPI, for the data validation and settings management.
- 💾 PostgreSQL as the SQL database.

## The following functionalities will be added as the project progresses:

- 🐋 Docker Compose for development and production.
- 🔒 Secure password hashing by default.
- 🔑 JWT (JSON Web Token) authentication.
- 📫 Email based password recovery.
- ✅ Tests with Pytest.
- 🚢 Deployment instructions using Docker Compose, including how to set up a frontend Traefik proxy to handle automatic HTTPS certificates.
- 🏭 CI (continuous integration) and CD (continuous deployment) based on GitHub Actions.

## Below are the steps to run the server.

### Create and Activate a Virtual Environment¶
When you start working on a Python project for the first time, create a virtual environment inside your project.

```bash
# Create the venv
python -m venv .venv

# Activate the venv
source .venv/bin/activate
```

### Install project dependencies

```bash
pip install -r requirements.txt
```

