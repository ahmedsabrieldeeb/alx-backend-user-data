#!/usr/bin/env python3
""" This module contains a function for hashing passwords """

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password

    Args:
        password (str): The password to hash

    Returns:
        bytes: The hashed password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
