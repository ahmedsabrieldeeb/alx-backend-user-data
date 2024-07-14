#!/usr/bin/env python3
""" Module of BasicAuth class """
from .auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if authorization_header[:6] != "Basic ":
            return None

        return authorization_header[6:]
