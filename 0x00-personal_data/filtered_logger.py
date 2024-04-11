#!/usr/bin/env python3
"""task 0 solution"""

import re


def filter_datum(
        fields: list, redaction: str, message: str, separator: str) -> str:
    """Returns a log message obfuscated"""
    return re.sub(
        r"({0}=)([^{1}]+)".format("|".join(fields), separator),
        r"\1{0}".format(redaction), message,)
