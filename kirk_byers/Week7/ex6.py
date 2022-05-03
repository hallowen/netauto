import yaml
from pprint import pprint

with open("kirk_byers/Week7/interfaces2.yaml") as f_interfaces:
    output = yaml.load(f_interfaces, Loader=yaml.BaseLoader)

pprint(output)
