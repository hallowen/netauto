# Getting show version output

from netmiko import Netmiko

device_details = {
    "host": "192.168.0.31",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
    "secret": "cisco"
}

conn = Netmiko(**device_details)

sh_version = conn.send_command('show version')
print(sh_version)
