"""Helper functionality for this program."""

import re


def search_for_mac_address(input_text):
    """Return a regex match object for a MAC address"""
    search_pattern_mac_address = "((?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2}))"
    return re.search(search_pattern_mac_address, input_text)
