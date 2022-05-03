'''1a. Use Jinja2 templating to render the following:
vlan
   name

Your template should be inside of your Python program for simplicity.

The output from processing your template should be as follows. This should be printed to stdout.
vlan 400
   name red400
'''

import jinja2

vlan_config = '''
vlan {{ vlan_num }}
name {{ vlan_name }}
'''

vlan_vars = {
    "vlan_num": "400",
    "vlan_name": "red400"
}

t = jinja2.Template(vlan_config)
output = t.render(vlan_vars)

print(output)
