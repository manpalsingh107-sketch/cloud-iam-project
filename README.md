# Cloud-Based Identity and Access Management System for SaaS Platforms

## Project Title
Secure Multi-Tenant Identity and Access Management System using JWT

## Project Description
This project is a cloud-based Identity and Access Management (IAM) system designed for SaaS platforms. It provides secure authentication and role-based access control using JSON Web Tokens (JWT). The system supports multi-tenant architecture and ensures data isolation between tenants.

## Features
- User Registration
- Secure Login with JWT Authentication
- Role-Based Access Control (Admin/User)
- Multi-Tenant Support (Tenant Isolation)
- Password Hashing using bcrypt
- Audit Logging (User activity tracking)

## Technologies Used
- Python
- Flask
- SQLite
- Flask-JWT-Extended
- bcrypt

## API Endpoints

### Register User
POST /register

### Login
POST /login

### Admin Access
GET /admin

### Logs
GET /logs

## How to Run

1. Install dependencies:
pip install flask flask_sqlalchemy flask_jwt_extended bcrypt

2. Run:
python app.py

3. Open:
http://127.0.0.1:5000/

## Project Structure
- app.py → Backend logic
- database.db → Database
- README.md → Documentation

## Author
- Manpal
- UID: O23BCA110019
