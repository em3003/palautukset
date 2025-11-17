from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if self._user_repository.find_by_username(username) is not None:
            raise UserInputError("Invalid username: Already in use")

        #if not (3 <= len(username) and username.isalpha() and username.islower()):
        if not (re.match("^[a-z]{3,}$", username)):
            raise UserInputError("Invalid username: Should be at least three 'a-z' characters")
        
        if not (8 <= len(password) and any(not c.isalpha() for c in password)):
            raise UserInputError("Invalid password: Should be at least eight characters long and contain at least one character that isn't a letter")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
