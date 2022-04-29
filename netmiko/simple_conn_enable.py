# Connecting to a Cisco IOS device and configuring commands. Enable password used in this case.

from netmiko import Netmiko

device_details = {
    "host": "192.168.0.31",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
    "secret": "cisco"
}

conn = Netmiko(**device_details)

config_commands = ['line console 0', 'logging sync', 'do write']
conn.enable()
conn.send_config_set(config_commands=config_commands)
