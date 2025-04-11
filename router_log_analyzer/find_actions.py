"""Contains the actions for finding events in the logs."""

import helpers
import recognizedmacs

debug = False


def find_lan_access_rejected(entries, entry_date):
    """Return information on entries where LAN access was rejected."""
    global debug

    wlan_accesses_rejected = {}

    # create a list of the "WLAN access rejected" entries
    findstr_access_rejected = "WLAN access rejected"
    list_access_rejected = [line for line in entries if findstr_access_rejected in line]
    if debug:
        print(findstr_access_rejected)
        print(list_access_rejected)
    # obtain all the mac addresses from the WLAN access rejected entries
    mac_addresses_wlan_access_rejected = set()
    for item in list_access_rejected:
        match = helpers.search_for_mac_address(item)
        mac_addresses_wlan_access_rejected.add(match.group())
        if debug:
            print(len(mac_addresses_wlan_access_rejected))
            print(mac_addresses_wlan_access_rejected)
    print("\n\tHere is a list MAC addresses that were rejected access...")
    if len(mac_addresses_wlan_access_rejected) == 0:
        print("\t\tNone")
    for address in mac_addresses_wlan_access_rejected:
        if address in recognizedmacs.recognizedmacaddresses:
            print(
                f"\t\tRejected - Recognized "
                f"{address} as "
                f"{str(recognizedmacs.recognizedmacaddresses.get(address))}"
            )
            wlan_accesses_rejected.update({entry_date: (address, "recognized")})
        else:
            print(f"\t\t!! Rejected - Did not recognize {address}")
            wlan_accesses_rejected.update({entry_date: (address, "not recognized")})

    return wlan_accesses_rejected


def find_site_blocked(entries, entry_date):
    """Return information on entries where a site was blocked."""
    global debug

    blocked_sites = {}

    # create a list of the "Site blocked:" entries
    findstr_site_blocked = "Site blocked:"
    list_site_blocked = [line for line in entries if findstr_site_blocked in line]
    if debug:
        print(findstr_site_blocked)
        print(list_site_blocked)
    print("\n\tHere is a list of Site Blocked entries...")
    if len(list_site_blocked) == 0:
        print("\t\tNone")
    else:
        for entry in list_site_blocked:
            print(f"\t\t{str(list_site_blocked)}")
            blocked_sites.update({entry_date: entry})

    return blocked_sites


def find_unknown_macs(entries, entry_date):
    """Return information on entries where unknown MACs connected."""
    global debug

    unknown_macs = {}

    # create a list of the "DHCP IP:" entries
    findstr_dhcp = "DHCP IP:"
    list_dhcp_ip = [line for line in entries if findstr_dhcp in line]
    if debug:
        print(findstr_dhcp)
        print(list_dhcp_ip)
    # obtain all the mac addresses from the DHCP entries
    mac_addresses_given_ip = set()
    for item in list_dhcp_ip:
        match = helpers.search_for_mac_address(item)
        mac_addresses_given_ip.add(match.group())
        if debug:
            print(mac_addresses_given_ip)
    # check if the mac addresses in the entries are in the recognized list
    print("\n\tNow checking MAC addresses that requested DHCP IP...")
    for address in mac_addresses_given_ip:
        if address in recognizedmacs.recognizedmacaddresses:
            print(
                "\t\tRecognized "
                + str(address)
                + " as "
                + str(recognizedmacs.recognizedmacaddresses.get(address))
            )
        else:
            print("\t\t!! Did not recognize " + address)
            unknown_macs.update({entry_date: address})

    return unknown_macs
