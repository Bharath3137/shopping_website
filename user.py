import re
import bcrypt
from logger import logger


class UserManager:

    def __init__(self, databasemanager):
        self.databasemanager = databasemanager
        self.current_user = None

    def register_user(self, username, email, hashed_password):
        hashed_password = bcrypt.hashpw(hashed_password.encode(), bcrypt.gensalt())
        hashed_password = hashed_password.decode()
        error = self.validate_username(username)

        if error:
            return error

        error = self.validate_email(email)

        if error:
            return error
        error = self.validate_password(hashed_password)
        if error:
            return error

        query = """SELECT * FROM users WHERE username = %s"""

        user = self.databasemanager.execute_query(query, (username,))
        if user:
            return "Username Already Exists"
        query = """SELECT * FROM users WHERE email = %s"""
        user = self.databasemanager.execute_query(query, (email,))

        if user:
            return "Email Already Exists"
        query = """INSERT INTO users(username, email, password, role) VALUES(%s, %s, %s, %s)"""

        self.databasemanager.execute_query(
            query, (username, email, hashed_password, "Customer")
        )

        return "Registration Successful"

    def login_user(self, email, password):

        query = """SELECT * FROM users WHERE email = %s"""

        user = self.databasemanager.execute_query(query, (email,))
        if not user:
            return "Invalid Email or Password"
        user = user[0]
        if not bcrypt.checkpw(password.encode(), user["password"].encode()):
            return "Invalid Email or Password"
        logger.info(f"{user['username']} logged in")
        self.current_user = user

        return "Login Successful"

    def get_current_user(self):
        return self.current_user

    def logout(self):

        if self.current_user is None:
            return "No User is Logged In"

        logger.info(f"{self.current_user['username']} logged out")

        self.current_user = None

        return "Logged Out Successfully"

    def validate_username(self, username):

        if len(username) < 3:
            return "Username must be at least 3 characters"

        if " " in username:
            return "Username cannot contain spaces"

        return None

    def validate_email(self, email):

        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not re.match(pattern, email):
            return "Invalid Email Format"

        return None

    def validate_password(self, password):

        if len(password) < 8:
            return "Password must be at least 8 characters"

        if not any(char.isupper() for char in password):
            return "Password must contain at least one uppercase letter"

        if not any(char.islower() for char in password):
            return "Password must contain at least one lowercase letter"

        if not any(char.isdigit() for char in password):
            return "Password must contain at least one digit"

        special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"

        if not any(char in special_characters for char in password):
            return "Password must contain at least one special character"

        return None
