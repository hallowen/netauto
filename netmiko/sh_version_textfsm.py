# Getting show version ouput and parsing it using TextFSM

from netmiko import Netmiko
from pprint import pprint

device_details = {
    "host": "192.168.0.33",
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "admin",
    "global_delay_factor": 2,
}

conn = Netmiko(**device_details)
sh_version_parsed = conn.send_command("show version", use_textfsm=True)

pprint(sh_version_parsed)
