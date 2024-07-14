#!/usr/bin/env python3
""" Module of BasicAuth class """
from .auth import Auth
import base64


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
