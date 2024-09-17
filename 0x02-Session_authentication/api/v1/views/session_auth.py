#!/usr/bin/env python3
"""Session authentication views"""

import os
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth() -> str:
    """ POST /api/v1/auth_session/login

    Return:
        - User object JSON represented
        - 400 if email is missing
        - 400 if password is missing
        - 404 if no user found for the email
        - 401 if the password is wrong
    """

    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400

    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(user[0].id)
    session_name = os.getenv('SESSION_NAME')
    response = jsonify(user[0].to_json())
    response.set_cookie(session_name, session_id)

    return response
