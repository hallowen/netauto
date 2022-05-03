# Loading network configuration from YAML file.

import yaml

with open('yaml/network_config.yaml') as f_network_config:
    output = yaml.load(f_network_config, Loader=yaml.BaseLoader)

for device in output:
    device_type = output[device]['device_type']
    username = output[device]['username']
    password = output[device]['password']
    networks = output[device]['networks']
    print("{} {}".format('Device Type:', device_type))
    print("Username: {}".format(username))
    print("Password: {}".format(password))
    for network in networks:
        print(network)
