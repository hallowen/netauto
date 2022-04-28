'''1b. Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with a default value of 'cisco_ios'. Print all four of the function variables out as part of the function's execution.

Call the 'ssh_conn2' function both with and without specifying the device_type

Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using the **kwargs technique.
'''


def ssh_conn(ip_addr, username, password, device_type='router'):
    print(ip_addr, username, password, device_type)


# Calling the function by specifying the device_type
ssh_conn('192.168.1.1', 'user1', 'password', 'switch')

# Calling the function without specifying the device_type
ssh_conn('192.168.1.2', 'user2', 'password')

dev_details = {
    'ip_addr': '192.168.1.3',
    'username': 'user3',
    'password': 'password',
    'device_type': 'firewall'
}

# Using **kwargs to pass parameters from dictionary
ssh_conn(**dev_details)
