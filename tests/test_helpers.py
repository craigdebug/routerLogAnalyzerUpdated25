"""Tests to cover the helpers functionality"""

import re
import pytest

import router_log_analyzer.helpers


@pytest.mark.parametrize(
    "input_string, should_we_find_a_match",
    [
        ("10:10:BB:92:8F:AB", True),
        ("10:10:BB:92:8F:ab", True),
        ("AA:BB:CC:DD:EE:FF", True),
        ("aa:bb:CC:DD:EE:FF", True),
        ("Fred Flintstone", False),
        ("10:10:9BB:92:8F:AB", False),
        ("10:10:9B:92:8F:A", False),
        ("0:10:9B:92:8F:AB", False),
        ("10:10:ZZ:92:8F:AB", False),
        ("10.10.9B.92.8F.AB", False),
        ("10.99.1.5", False),
        (
            "[DHCP IP: (10.99.1.5)] to MAC address 1A:10:12:84:72:76, Sunday, Oct 27,2024 12:53:01 and 1A:12:12:88:78:76 is something",
            True,
        ),
    ],
)
def test_router_log_analyzer_helpers_search_for_mac_address(
    input_string, should_we_find_a_match
):
    returned_match_object = router_log_analyzer.helpers.search_for_mac_address(
        input_string
    )
    did_we_find_a_match = returned_match_object is not None
    assert did_we_find_a_match == should_we_find_a_match
