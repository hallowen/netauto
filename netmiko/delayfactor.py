# Setting delay to commands which takes time to execute
from netmiko import Netmiko

device_details = {
    "host": "192.168.0.33",
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "admin",
}

conn = Netmiko(**device_details)

# Delay factor will multiply the current delay to itself thereby allowing more wait time for the command to execute
output = conn.send_command("copy run start", delay_factor=2)

print(output)
