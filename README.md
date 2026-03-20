# Cloud-Based Identity and Access Management System for SaaS Platforms

## Project Title
Secure Multi-Tenant Identity and Access Management System using JWT

## Project Description
This project is a cloud-based Identity and Access Management (IAM) system designed for SaaS platforms. It provides secure authentication and role-based access control using JSON Web Tokens (JWT). The system supports multi-tenant architecture where different organizations can manage their users securely.

## Features
- User Registration
- User Login with JWT Authentication
- Role-Based Access Control (Admin/User)
- Protected API Endpoints
- Multi-Tenant Support (Tenant ID based)
- Secure Access using Tokens

## Technologies Used
- Python
- Flask
- SQLite Database
- Flask-JWT-Extended

## API Endpoints

### 1. Register User
POST /register

### 2. Login
POST /login

### 3. Admin Access
GET /admin

## How to Run the Project

1. Install dependencies:
pip install flask flask_sqlalchemy flask_jwt_extended

2. Run the application:
python app.py

3. Open in browser:
http://127.0.0.1:5000/

## Project Structure
- app.py → Main backend code
- database.db → Database file
- README.md → Project documentation

## Author
- Manpal
- UID: O23BCA110019
