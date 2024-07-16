#!/usr/bin/env python3
""" Module of Auth classes
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class Tempate """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth method """
        if path is None or excluded_paths is None:
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header method """
        if request is None:
            return None

        try:
            return request.headers.get('Authorization')
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """ current_user method """
        return None
