#!/usr/bin/env python3
"""Auth class"""

from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if the path requires authentication."""
        if path is None:
            return True

        if path == "/api/v1/status" or "/api/v1/auth_session/login":
            return False

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        for excluded_path in excluded_paths:
            if excluded_path.endswith("*") and path.startswith(excluded_path[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get authorization headers"""
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar("User"):
        """Get current user"""
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""

        if request is None:
            return None

        cookie_name = os.getenv("SESSION_NAME")
        return request.cookies.get(cookie_name, None)
