# Creating a basic Jinj2 template and render it using Python

import jinja2

bgp_vars = {
    "local_as": "65000",
    "neighbor_ip": "2.2.2.2",
    "remote_as": "65000",
    "update_source": "loopback0",
}


bgp_config = """
router bgp {{ local_as }}
no bgp default ipv4 unicast
neighbor {{ neighbor_ip }} remote-as {{ remote_as }}
update-source {{ update_source }}
"""

t = jinja2.Template(bgp_config)

print(t.render(bgp_vars))
