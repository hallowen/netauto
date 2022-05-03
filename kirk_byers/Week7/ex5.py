'''3a. Create a YAML file that defines a list of interface names. Use the expanded form of YAML.

Use a Python script to read in this YAML list and print it to the screen.

The output of your Python script should be:
['Ethernet1', 'Ethernet2', 'Ethernet3', 'Ethernet4', 'Ethernet5', 'Ethernet6', 'Ethernet7', 'Management1', 'Vlan1']
'''
from unittest import loader
import yaml

with open("kirk_byers/Week7/interfaces.yaml") as f_interfaces:
    output = yaml.load(f_interfaces, Loader=yaml.BaseLoader)

print(output)
