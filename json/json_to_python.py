# Importing JSON to Python
import json

with open("json/network_config.json") as f_json:
    output = json.load(f_json)

print(output)
