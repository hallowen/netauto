'''1b. Using a conditional in a Jinja2 template, generate the following output:
crypto isakmp policy 10
 encr aes
 authentication pre-share
 group 5
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic

The encryption of aes, and the Diffie-Hellman group should be variables in the template.

Additionally this entire ISAKMP section should only be added if the isakmp_enable variable is set to True.

Your template should be inside your Python program for simplicity.'''

import jinja2

crypto_config = '''crypto isakmp policy {{ isakmp_policy_num }}
 encr {{ isakmp_encr }}
 authentication {{ auth_type }}
 group {{ dh_group }}
{%- if isakmp_enable %}
crypto isakmp key {{ isakmp_key_name }} address {{ peer_address }} no x-auth
crypto isakmp keepalive {{ isakmp_keepalive }} periodic
{%- endif %}'''
crypto_vars = {
    "isakmp_policy_num": "10",
    "isakmp_encr": "aes",
    "auth_type": "pre-share",
    "dh_group": "5",
    "isakmp_enable": True,
    "isakmp_key_name": "my_key",
    "peer_address": "1.1.1.1",
    "isakmp_keepalive": "10"
}

t = jinja2.Template(crypto_config)

output = t.render(crypto_vars)

print(output)
