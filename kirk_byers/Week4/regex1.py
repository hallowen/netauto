import re

with open("devnet/kirk_byers/Week4/show_version.txt") as f_sh_version:
    sh_version_list = f_sh_version.readlines()

# Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 15.0(2)SE4, RELEASE SOFTWARE (fc1)

line = sh_version_list[1].strip()
match = re.search(
    r".*, (?P<device_model>.*) Software \((?P<device_software_base>\w{1,5}\-\w{1,9}\-\w)\)",
    line,
)
values = match.groupdict()
print(values)
