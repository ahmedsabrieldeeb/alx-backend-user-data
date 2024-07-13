#!/usr/bin/env python3
"""
This module contains a function for obfuscating sensitive data in log messages
"""

from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscates sensitive data in a log message.

    Args:
        fields (List[str]): A list of field names to be obfuscated.
        redaction (str): The string to replace the sensitive data with.
        message (str): The log message to be obfuscated.
        separator (str): used to separate the fields in the log message.

    Returns:
        str: The obfuscated log message.

    """
    for field in fields:
        message = re.sub(f"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message
