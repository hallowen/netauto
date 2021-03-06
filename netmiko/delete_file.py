# Deleting a file on remote device using netmiko

from netmiko import Netmiko

device_details = {
    "host": "192.168.0.33",
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "admin",
}

conn = Netmiko(**device_details)
output = conn.send_command_timing("delete bootflash:///filetodelete.txt")
conn.send_command("y\n")
print("File successfully deleted")
