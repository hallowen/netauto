'''4. Take the YAML file and corresponding data structure that you defined in exercise3b:
{'interfaces': {
    'Ethernet1': {'mode': 'access', 'vlan': 10},
    'Ethernet2': {'mode': 'access', 'vlan': 20},
    'Ethernet3': {'mode': 'trunk',
                  'native_vlan': 1,
                  'trunk_vlans': 'all'}
    }
}

From this YAML data input source, use Jinja templating to generate the following configuration output:

interface Ethernet1
  switchport mode access
  switchport access vlan 10
interface Ethernet2
  switchport mode access
  switchport access vlan 20
interface Ethernet3
  switchport mode trunk
  switchport trunk native vlan 1
  switchport trunk allowed vlan all

The following should all be variables in your Jinja template (the names may be different than below, but they should be variabilized and not be hard-coded in your template).
interface_name
switchport_mode
access_vlan
native_vlan
trunk_vlans

All your Jinja2 variables should be retrieved from your YAML file.

This exercise might be challenging.'''

import yaml
import jinja2

with open("kirk_byers/Week7/interfaces2.yaml") as f_interfaces:
    intf_details = yaml.load(f_interfaces, Loader=yaml.BaseLoader)

'''{'interfaces': {'Ethernet1': {'mode': 'access', 'vlan': '10'},
                'Ethernet2': {'mode': 'access', 'vlan': '20'},
                'Ethernet3': {'mode': 'trunk',
                              'native_vlan': '1',
                              'trunk_vlans': 'all'}}}'''

interfaces = intf_details['interfaces']

interface_template = '''
interface {{ interface_name }}
{%- if access_enabled %}
switchport mode access
switchport access vlan {{ vlan_id }}
{%- else %}
switchport mode trunk
switchport trunk native vlan {{ native_vlan }}
switchport trunk allowed vlan {{ trunk_vlans }}
{%- endif %}
'''
vlan_id = 1
native_vlan = 1
trunk_vlans = 'none'
# access_enabled = False

for interface in interfaces:
    interface_name = interface
    interface_mode = interfaces[interface]['mode']

    if(interface_mode == 'access'):
        access_enabled = True
        vlan_id = interfaces[interface]['vlan']
    else:
        access_enabled = False
        native_vlan = interfaces[interface]['native_vlan']
        trunk_vlans = interfaces[interface]['trunk_vlans']

    interface_vars = {
        "interface_name": interface_name,
        "interface_mode": interface_mode,
        "access_enabled": access_enabled,
        "vlan_id": vlan_id,
        "native_vlan": native_vlan,
        "trunk_vlans": trunk_vlans
    }
    t = jinja2.Template(interface_template)
    output = t.render(interface_vars)
    print(output)
