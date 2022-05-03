# Converting Python to YAML
import yaml

routers = {
    "R1": {"device_type": "ios", "username": "cisco", "password": "password", "networks": ['192.168.1.1/32', '192.168.1.2/32', '192.168.1.3/32']},
    "R2": {"device_type": "nxos", "username": "cisco", "password": "password", "networks": ['192.168.2.1/32', '192.168.2.2/32', '192.168.2.3/32']}
}

output = yaml.dump(routers)

print(output)
