#!/usr/bin/env python3
"""Test file"""

import requests
from user import User
from auth import Auth

AUTH = Auth()

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
BASE_URL = "http://0.0.0.0:5000"
reset_token = None


def register_user(email: str, password: str) -> None:
    """Test register user function"""

    url = f"{BASE_URL}/users"
    data = {"email": email, "password": password}
    res = requests.post(url, data)
    assert res.status_code == 200
    res = requests.post(url, data)
    assert res.status_code == 400
    assert res.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Test login with wrong password"""

    url = f"{BASE_URL}/sessions"
    data = {"email": email, "password": password}
    res = requests.post(url, data)
    assert res.status_code == 401


def log_in(email: str, password: str) -> str:
    """Test login with correct password"""

    url = f"{BASE_URL}/sessions"
    data = {"email": email, "password": password}
    res = requests.post(url, data)
    assert res.status_code == 200
    assert res.json() == {"email": "guillaume@holberton.io", "message": "logged in"}


def profile_unlogged() -> None:
    """Test unlogged profile"""

    url = f"{BASE_URL}/profile"
    res = requests.get(url)
    assert res.status_code == 200


def profile_logged(session_id: str) -> None:
    """Test logged profile"""

    url = f"{BASE_URL}/profile"
    data = {"session_id": session_id}
    res = requests.get(url, data)
    assert res.status_code == 200


def log_out(session_id: str) -> None:
    """Test log out"""

    url = f"{BASE_URL}/sessions"
    data = {"session_id": session_id}
    res = requests.delete(url, data)
    assert res.status_code == 403


def reset_password_token(email: str) -> str:
    """Test reset password token endpoint"""

    url = f"{BASE_URL}/reset_password"
    data = {"email": email}
    res = requests.post(url, data)
    assert res.status_code == 200
    reset_token = res.json()["reset_token"]
    assert reset_token != None


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test update password endpoint"""

    url = f"{BASE_URL}/reset_password"
    data = {"email": email, "reset_token": reset_token, "new_password": new_password}
    res = requests.put(url, data)
    assert res.status_code == 200
    assert res.json() == {
        "email": "guillaume@holberton.io",
        "message": "Password updated",
    }


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
