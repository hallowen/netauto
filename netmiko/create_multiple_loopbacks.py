# Creating multiple loopback addresses

from netmiko import Netmiko

device_details = {
    "host": "192.168.0.33",
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "admin",
}

conn = Netmiko(**device_details)

for i in range(1, 255):
    lo_name = "int lo " + str(i)
    lo_address = "ip address 1.1.1." + str(i) + " 255.255.255.255"
    commands = [lo_name, lo_address]
    output = conn.send_config_set(commands)
    print(output)
