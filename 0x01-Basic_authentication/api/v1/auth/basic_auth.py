#!/usr/bin/env python3
""" Basic Auth class"""

from api.v1.auth.auth import Auth
import base64


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
