'''2. Using Python and Jinja2 templating generate the following OSPF configuration:
interface vlan 1
   ip ospf priority 100

router ospf 10
   passive-interface default
   no passive-interface Vlan1
   no passive-interface Vlan2
   network 10.10.10.0/24 area 0.0.0.0
   network 10.10.20.0/24 area 0.0.0.0
   network 10.10.30.0/24 area 0.0.0.0
   max-lsa 12000

The following items should be variables in your Jinja2 template:
​ospf_process_id
ospf_priority
ospf_active_interfaces (i.e. the non-passive interfaces)
ospf_area0_networks (the three networks that are specified as belonging to area0)

Your template should be in an external file.

Your template should also use a conditional to control whether this is output or not:
interface vlan 1
   ip ospf priority 100

If the 'ospf_priority variable is defined', then include that section. If 'ospf_priority' is not defined then only include the 'router ospf 10' section.

'''

import jinja2

ospf_config = '''
{%-if ospf_priority_enabled %}
interface vlan {{ vlan_id }}
   ip ospf priority {{ ospf_priority }}
{%- endif %}

router ospf {{ ospf_process_id }}
   passive-interface default
   {%- for intf in ospf_passive_intf %}
   no passive-interface {{ intf }}
   {%- endfor %}
   {%- for network in ospf_networks %}
   network {{ network }} area 0.0.0.0
   {%- endfor %}
   max-lsa {{ max_lsa }}
'''

vars_ospf = {
    "vlan_id": "1",
    "ospf_priority_enabled": True,
    "ospf_process_id": "10",
    "ospf_passive_intf": ['Vlan 1', 'Vlan 2'],
    "ospf_networks": ['192.168.10.0/24', '192.168.20.0/24', '192.168.30.0/24 '],
    "max_lsa": "1200"
}

t = jinja2.Template(ospf_config)

output = t.render(vars_ospf)
print(output)
