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
