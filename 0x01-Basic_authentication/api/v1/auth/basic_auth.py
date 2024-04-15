#!/usr/bin/env python3
""" Basic Auth class"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def extract_base64_authorization_header(
        self, authorization_header: str) -> str:
        """ Decode base64 encoded string
        """

        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None
