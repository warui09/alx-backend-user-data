#!/usr/bin/env python3
"""SessionDBAuth class"""

from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """Implements SessionDBAuth class"""

    def create_session(self, user_id=None):
        """Creates and stores session ID"""

        session_id = super().create_session(user_id)
        if session_id:
            kwargs = {"user_id": user_id, "session_id": session_id}

            user_session = UserSession(**kwargs)
            user_session.save()
            return session_id

        return None

    def user_id_for_session_id(self, session_id=None):
        """Return user_id for a given session ID"""

        try:
            user_session = UserSessions.search({"session_id": session_id})
        except Exception:
            return None

        # check if session is valid
        expiration_time = user_session["created_at"] + timedelta(
            seconds=self.session_duration
        )
        if expiration_time < datetime.now():
            return None

        return user_session[0].user_id

    def destroy_session(self, request=None):
        """Destroy session"""

        session_id = self.session_cookie(request)

        try:
            session = UserSession.search({"session_id": session_id})
        except Exception:
            return False

        if session:
            session[0].remove()
            return True

        return False
