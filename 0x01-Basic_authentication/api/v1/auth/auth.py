#!/usr/bin/env python3
"""Auth class"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if the path requires authentication."""
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Check if path is in excluded_paths
        if path in excluded_paths:
            return False

        # Check if path with trailing slash is in excluded_paths
        if path.endswith("/") and path.rstrip("/") in excluded_paths:
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
