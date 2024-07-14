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


def is_valid(hashed_password: bytes, password: str) -> bool:
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False
