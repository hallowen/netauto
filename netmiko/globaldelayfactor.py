# Setting delay factor globally

from netmiko import Netmiko

device_details = {
    "host": "192.168.0.33",
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "admin",
    "global_delay_factor": 2,
}

conn = Netmiko(**device_details)
output = conn.send_command("copy run start")

print(output)
