"""Tests to cover the find actions functionality"""

# import pytest

import router_log_analyzer.find_actions


def test_router_log_analyzer_find_actions_find_lan_access_rejected():
    returned_match_object = router_log_analyzer.find_actions.find_lan_access_rejected(
        "todo", "02/20/2025"
    )

    assert False
