# Convert Python date to JSON
import json

routers = {"R1": {
    "username": "cisco",
    "password": "password",
    "device_type": "cisco_ios"
},
    "R2": {
    "username": "cisco",
    "password": "password",
    "device_type": "cisco_nxos"
}
}

output = json.dumps(routers)
print(output)
