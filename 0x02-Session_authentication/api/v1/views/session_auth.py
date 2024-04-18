#!/usr/bin/env python3
"""view for all routes for the Session authentication"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from api.v1.app import auth


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login() -> str:
    """Login a user"""

    email = request.form.get("email")
    passwd = request.form.get("password")

    if email is None or len(email) == 0:
        return jsonify({"error": "email missing"}), 400

    if passwd is None or len(passwd) == 0:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if user is None or len(user) <= 0:
        return jsonify({"error": "no user found for this email"}), 404

    if user[0].is_valid_password(passwd):
        from api.v1.app import auth

        session_id = auth.create_session(getattr(users[0], "id"))
        response = jsonify(user[0].to_json())
        response.set_cookie(os.getenv("SESSION_NAME"), session_id)
        return response
    else:
        return jsonify({"error": "wrong password"}), 401


@app_views.route(
    "/api/v1/auth_session/logout", methods=["DELETE"], strict_slashes=False
)
def logout() -> str:
    """Logout user"""

    if auth.destroy_session(request):
        return jsonify({})

    abort(404)
