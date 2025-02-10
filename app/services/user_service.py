from app.models.user import User
from app.repository.user_repository import UserRepository
from flask_bcrypt import Bcrypt

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.bcrypt = Bcrypt()

    def register_user(self, username, email, password):
        if self.user_repository.get_user_by_username(username):
            raise ValueError("Username already exists")
        password = self.bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username, email, password)
        self.user_repository.create_user(user)

    def login_user(self, username, password):
        user = self.user_repository.get_user_by_username(username)
        if user and self.bcrypt.check_password_hash(user.password, password):
            return user
        raise ValueError("Invalid credentials")
