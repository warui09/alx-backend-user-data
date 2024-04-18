#!/usr/bin/env python3
"""SessionExpAuth class"""

from .session_auth import SessionAuth
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """Class SessionExpAuth"""

    def __init__(self) -> None:
        """Overload parent init method"""

        super().__init__()
        try:
            self.session_duration = os.getenv("SESSION_DURATION")
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Create a Session ID"""

        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        self.user_id_by_session_id[session_id] = {
            "user_id": user_id,
            "created_at": datetime.now(),
        }

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Get user_id from session_id"""

        if session_id is None or self.user_id_by_session_id.get(session_id) is None:
            return None

        session_dict = self.user_id_by_session_id[session_id]
        if self.session_duration <= 0:
            return session_dict.get("user_id")

        if session_dict.get("created_at") is None:
            return None

        expiration_time = session_dict["created_at"] + timedelta(
            seconds=self.session_duration
        )
        if expiration_time < datetime.now():
            return None

        return session_dict["user_id"]
