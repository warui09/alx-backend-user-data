#!/usr/bin/env python3
"""Auth file"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hash a password string"""

    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user"""

        # chech if user exists
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError("User <user's email> already exists")

        # save user
        if not user:
            hash_password = _hash_password(password)
            return self._db.add_user(email, hash_password)
