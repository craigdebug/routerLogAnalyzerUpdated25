"""Tests to cover the find actions functionality"""

import pytest

import router_log_analyzer.find_actions


@pytest.mark.parametrize(
    "entries, entry_date, number_of_matches_expected",
    [
        (["no match to be found"], "02/20/2025", 0),  # no matches case
        (
            # 1 match case
            ["[WLAN access rejected: incorrect security] from MAC 55:CC:EA:DF:DD:AA"],
            "02/20/2025",
            1,
        ),
        (
            # 2 match case
            [
                "[WLAN access rejected: incorrect security] from MAC 55:CC:EA:DF:DD:AA",
                "No Match in this string",
                "[WLAN access rejected: incorrect security] from MAC 11:CC:EA:11:00:AA",
            ],
            "02/20/2025",
            2,
        ),
    ],
)
def test_router_log_analyzer_find_actions_find_lan_access_rejected_find_none(
    entries, entry_date, number_of_matches_expected
):
    returned_match_object = router_log_analyzer.find_actions.find_lan_access_rejected(
        entries, entry_date
    )

    assert len(returned_match_object) == number_of_matches_expected
