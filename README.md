# cyb333-finalclass-project
# User Credentials Authenticator README

## Introduction
This project provides a basic implementation of a user credentials authenticator using Python, emphasizing the importance of secure password handling. While this is a rudimentary demonstration, it exemplifies core security principles like password hashing using bcrypt.

## Key Security Principles:
- **Never Store Passwords in Plain Text:** Use strong cryptographic hashing algorithms (e.g., bcrypt).
  
- **Avoid DIY Security:** Leverage established libraries and methodologies. Home-brewed security can be error-prone.
  
- **Secure Communication:** For web or network-based apps, always prefer HTTPS or other secure protocols.
  
- **Brute Force Mitigation:** Limit login attempts to deter brute force attacks.

## How to Use:
1. **Register:** Input a username and password to register. Passwords are hashed before storing.
   
2. **Login:** Input registered credentials. The program will authenticate by checking the hashed password.

3. **Exit:** Quit the application.

## Code Overview:
The code includes functions to register users (`register_user`) and authenticate them (`authenticate_user`). Passwords are hashed using `bcrypt` before storing them in an in-memory "database" (a dictionary called `users_db` for demonstration purposes).

## Before Running:
- This is a basic example. For production, integrate with a proper database, manage sessions, and implement rate-limiting.
  
- The code employs an in-memory dictionary for demonstration. Utilize a real database for storing hashed passwords in real-world applications.
  
- Ensure the `bcrypt` library is installed:
  ```bash
  pip install bcrypt
