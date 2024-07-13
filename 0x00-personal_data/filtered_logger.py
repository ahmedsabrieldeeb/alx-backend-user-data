#!/usr/bin/env python3
"""
This module contains a function for obfuscating sensitive data in log messages
"""
import logging
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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Redacting Formatter constructor """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format the record

        Args:
            record (logging.LogRecord): The record to format

        Returns:
            str: The formatted record
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
