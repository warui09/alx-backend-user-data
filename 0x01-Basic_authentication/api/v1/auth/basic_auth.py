#!/usr/bin/env python3
""" Basic Auth class"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(
            self, authorization_header: str
        ) -> str:
        """Decode base64 encoded string"""

        if authorization_header is None or not isinstance(
                authorization_header, str
            ):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
        ) -> str:
        """Decode value of a Base64 string base64_authorization_header"""

        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str
            ):
            return None

        try:
            decoded_bytes = base64.b64decode(
                base64_authorization_header, validate=True
            )
            return decoded_bytes.decode('utf-8')
        except:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
        ) -> (str, str):
        """Returns user email and password from Base64 decoded value"""

        try:
            email, passwd = decoded_base64_authorization_header.split(":")
            return (email, passwd)
        except:
            return (None, None)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
        ) -> TypeVar('User'):
        """Return User object"""
        
        if user_email is None or not isinstance(user_email, str):
            return None
        
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        
        try:
            user = User.search({"email": user_email})
            if user and user.is_valid_password(user_pwd):
                return user
            else:
                return None
        except Exception:
            return None
        
    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the User instance for a request"""

        header = self.authorization_header(request)
        auth_token = self.extract_base64_authorization_header(header)
        auth_token_decoded = self.decode_base64_authorization_header(auth_token)
        email, password = self.extract_user_credentials(auth_token_decoded)
        return self.user_object_from_credentials(email, password)
