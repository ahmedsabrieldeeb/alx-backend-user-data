#!/usr/bin/env python3
""" Module of BasicAuth class """
from .auth import Auth
import base64

from typing import Tuple, TypeVar


class BasicAuth(Auth):
    """ BasicAuth class """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extracting the base64 part of Authorization header

        Args:
            authorization_header (str): Authorization header

        Returns:
            str: base64 part of Authorization header
            None: otherwise
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if authorization_header[:6] != "Basic ":
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decoding the base64 part of Authorization header

        Args:
            base64_authorization_header (str): base64 part to be encoded

        Returns:
            str: decoded base64 part
            None: otherwise
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            return base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """ Extracting user credentials from decoded base64 part

        Args:
            decoded_base64_authorization_header (str): decoded base64 part

        Returns:
            Tuple[str, str]: user credentials
            Tuple[None, None]: otherwise
        """
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
            self,
            user_email: str, user_pwd: str) -> TypeVar('User'):  # type: ignore
        """ User object from credentials

        Args:
            user_email (str): user email
            user_pwd (str): user password

        Returns:
            TypeVar('User'): User object
            None: user not found, no db nor file, wrong data
        """
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        from models.user import User

        try:
            user = User.search(attributes={"email": user_email})
        except Exception:
            return None

        if len(user) != 1:
            return None

        if not user[0].is_valid_password(user_pwd):
            return None

        return user[0]
