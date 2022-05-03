# Configure Interfaces and BGP on 2 NXOS devices
import jinja2
from netmiko import Netmiko

nxos_devices = ["192.168.0.104", "192.168.0.108"]

# Defining variables specific to devices
nxos_vars_nxos1 = {
    "lo_num": "0",
    "lo_address": "1.1.1.1/32",
    "e1_1_ip_address": "192.168.100.1/24",
    "bgp_local_as": "65000",
    "neighbor_address": "2.2.2.2",
    "bgp_remote_as": "65000",
    "update_src": "loo0",
    "local_subnet01": "1.1.1.1/32",
    "address_family_ipv6": False,
}

nxos_vars_nxos2 = {
    "lo_num": "0",
    "lo_address": "2.2.2.2/32",
    "e1_1_ip_address": "192.168.100.2/24",
    "bgp_local_as": "65000",
    "neighbor_address": "1.1.1.1",
    "bgp_remote_as": "65000",
    "update_src": "loo0",
    "local_subnet01": "2.2.2.2/32",
    "address_family_ipv6": True,
}


with open("jinja2/nxos_config.j2") as f_nxos_config:
    nxos_config = f_nxos_config.read()


t = jinja2.Template(nxos_config)

for device in nxos_devices:
    if device == "192.168.0.104":
        config_nxos1 = t.render(nxos_vars_nxos1)
        with open("jinja2/nxos1.txt", "w") as f_nxos1:
            f_nxos1.write(config_nxos1)
    elif device == "192.168.0.108":
        config_nxos2 = t.render(nxos_vars_nxos2)
        with open("jinja2/nxos2.txt", "w") as f_nxos2:
            f_nxos2.write(config_nxos2)

for device in nxos_devices:
    dev_details = {
        "host": device,
        "device_type": "cisco_nxos",
        "username": "admin",
        "password": "admin",
    }

    conn = Netmiko(**dev_details)
    if device == "192.168.0.104":
        conn.send_config_from_file("jinja2/nxos1.txt")
    elif device == "192.168.0.108":
        conn.send_config_from_file("jinja2/nxos2.txt")
