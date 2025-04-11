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
def test_router_log_analyzer_find_actions_find_lan_access_rejected_find(
    entries, entry_date, number_of_matches_expected
):
    returned_match_object = router_log_analyzer.find_actions.find_lan_access_rejected(
        entries, entry_date
    )

    assert len(returned_match_object) == number_of_matches_expected


@pytest.mark.parametrize(
    "entries, entry_date, number_of_matches_expected",
    [
        (
            ["no match to be found"],
            "Sunday, Oct 27,2024 12:14:11",
            0,
        ),  # no matches case
        (
            # 1 match case
            ["[DHCP IP: (10.0.0.11)] to MAC address AA:66:FF:00:99:72"],
            "Sunday, Oct 27,2024 12:14:11",
            1,
        ),
        (
            # 2 match case
            [
                "[DHCP IP: (10.0.0.11)] to MAC address AA:66:FF:00:99:72",
                "No Match in this string",
                "[DHCP IP: (10.0.0.23)] to MAC address FF:66:FF:00:FF:72",
            ],
            "Sunday, Oct 27,2024 12:14:15",
            2,
        ),
    ],
)
def test_router_log_analyzer_find_actions_find_unknown_macs(
    entries, entry_date, number_of_matches_expected
):
    returned_match_object = router_log_analyzer.find_actions.find_unknown_macs(
        entries, entry_date
    )

    assert len(returned_match_object) == number_of_matches_expected


@pytest.mark.parametrize(
    "entries, entry_date, number_of_matches_expected",
    [
        (
            ["no match to be found"],
            "Sunday, Oct 27,2024 12:14:11",
            0,
        ),  # no matches case
        (
            # 1 match case
            [
                "[Site blocked: www.website.com] from MAC Address 00:A0:00:EE:CF:00, Sunday, Oct 27,2024 12:18:00"
            ],
            "Sunday, Oct 27,2024 12:14:11",
            1,
        ),
        (
            # 2 match case
            [
                "[Site blocked: www.website.com] from MAC Address 00:A0:00:EE:CF:00, Sunday, Oct 27,2024 12:18:00",
                "No Match in this string",
                "[Site blocked: www.anotherwebsite.com] from MAC Address 00:A0:00:EE:CF:00, Sunday, Oct 27,2024 12:20:00",
            ],
            "Sunday, Oct 27,2024 12:14:15",
            2,
        ),
    ],
)
def test_router_log_analyzer_find_actions_find_site_blocked(
    entries, entry_date, number_of_matches_expected
):
    returned_match_object = router_log_analyzer.find_actions.find_site_blocked(
        entries, entry_date
    )

    assert len(returned_match_object) == number_of_matches_expected
