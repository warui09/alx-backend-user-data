#!/usr/bin/env python3
"""view for all routes for the Session authentication"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login() -> str:
    """Login a user"""

    email = request.form.get("email")
    passwd = request.form.get("password")

    if email is None:
        return jsonify({"error": "email missing"}), 400

    if passwd is None:
        return jsonify({"error": "password missing"}), 400

    user = User.search(email)
    if user is None:
        return jsonify({"error": "no user found for this email"}), 404

    if user.is_valid_password(passwd):
        from api.v1.app import auth

        sessiond_id = auth.create_session(getattr(users, "id"))
        response = jsonify(user.to_json())
        response.set_cookie(os.getenv("SESSION_NAME"), sessiond_id)
        return response
    else:
        return jsonify({"error": "wrong password"}), 401
