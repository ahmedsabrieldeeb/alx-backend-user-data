#!/usr/bin/env python3
""" Module of SessionAuth class """

from .auth import Auth
import base64
import uuid

from typing import Tuple, TypeVar


class SessionAuth(Auth):
    """ SessionAuth class """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a session ID

        Args:
            user_id (str): User ID

        Returns:
            str: Session ID
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Get a User ID from a Session ID

        Args:
            session_id (str): Session ID

        Returns:
            str: User ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Get a User instance from a Session ID

        Args:
            request (obj): request object

        Returns:
            obj: User instance
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)

        from models.user import User
        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """ Destroy a session

        Args:
            request (obj): request object

        Returns:
            bool: True if the session has been destroyed, False otherwise
        """
        if request is None:
            return False

        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False

        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_cookie]
        return True
