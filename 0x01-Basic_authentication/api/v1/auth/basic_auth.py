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
