import bcrypt

# A simple in-memory "database" (just for this demonstration)
users_db = {}


def register_user(username, password):
    """Register a new user."""
    if username in users_db:
        return "Username already exists."

    # Hash the password before storing it
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users_db[username] = hashed
    return "User registered successfully."


def authenticate_user(username, password):
    """Authenticate a user."""
    if username not in users_db:
        return False

    # Check the password against the hashed version in the database
    return bcrypt.checkpw(password.encode('utf-8'), users_db[username])


def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(register_user(username, password))
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if authenticate_user(username, password):
                print("Login successful!")
            else:
                print("Login failed!")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
