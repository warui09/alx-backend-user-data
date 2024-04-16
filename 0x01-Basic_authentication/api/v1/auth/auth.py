#!/usr/bin/env python3
"""Auth class"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Get authorized paths"""
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # handle slashes at end
        if path[-1] != "/":
            path = path + "/"

        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """Get authorization headers"""
        if request is None:
            return None

        authorization_header = request.headers.get("Authorization")
        return authorization_header

    def current_user(self, request=None) -> TypeVar("User"):
        """Get current user"""
        return None
