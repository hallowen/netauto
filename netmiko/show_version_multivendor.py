# Getting show version output from multivendor devices

from netmiko import Netmiko


device_details_cisco = {
    "host": "192.168.0.31",
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco"
}

device_details_srx = {
    "host": "192.168.0.32",
    "device_type": "juniper_junos",
    "username": "labuser",
    "password": "P@ssw0rd"
}

device_details_nxos = {
    "host": "192.168.0.33",
    "device_type": "cisco_nxos",
    "username": "admin",
    "password": "P@ssw0rd"
}

for device in [device_details_cisco, device_details_nxos, device_details_srx]:
    conn = Netmiko(**device)
    sh_version = conn.send_command('show version')
    print(sh_version)
