"""This is a router log file analyzer tool."""

import os
import sys

from find_actions import find_lan_access_rejected, find_site_blocked, find_unknown_macs

debug = False
version = "2.0"

print()
print(f"*** Router Log Analyzer {version} ***")
print()

directory = "../tests/log_samples"

unknown_macs = {}
blocked_sites = {}
rejected_lan_accesses = {}

for logfile in os.scandir(directory):

    file_ext = os.path.splitext(logfile)[1].lower()
    if file_ext != ".eml":
        continue
    with open(logfile.path, "r") as file:
        log_entries = [line.rstrip("\n").split(",")[0] for line in file]

    if debug:
        print(log_entries)
        print()

    # get the log date
    findstr_date = "DATE:"
    list_date = [line for line in log_entries if findstr_date in line]
    if debug:
        print(findstr_date)
        print(list_date)
    print(f"\n*** Log dated {list_date[0]}")
    print(f"Filename: {str(logfile.path)}")

    unknown_macs.update(find_unknown_macs(log_entries, list_date[0]))

    print("")

    rejected_lan_accesses.update(find_lan_access_rejected(log_entries, list_date[0]))

    print("")

    blocked_sites.update(find_site_blocked(log_entries, list_date[0]))

print()
print("Analysis complete.\n\n")
print()

print()
print("Summary")
print("\tUnknown MACs")
for key, value in unknown_macs.items():
    print(f"\t{key}:  {value}")
print()
print("\tRejected LAN accesses")
for key, value in rejected_lan_accesses.items():
    print(f"\t{key}:  {value}")
print()
print("\tBlocked Sites")
for key, value in blocked_sites.items():
    print(f"\t{key}:  {value}")

print()
# inputValue = input("Would you like to delete log files? y for yes: ")
# if inputValue == "y" or inputValue == "Y":
#     for logfile in os.scandir(directory):
#         os.remove(logfile)
print("\n\n")

sys.exit()
