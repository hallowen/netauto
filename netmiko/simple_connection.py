# Connecting to a Cisco device using priv 15 user and printing the prompt

from netmiko import Netmiko

device_details = {
    "host": "192.168.0.31",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios"
}

conn = Netmiko(**device_details)
print(conn.find_prompt())
