#!/usr/bin/env python3
"""Auth file"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password string"""

    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
