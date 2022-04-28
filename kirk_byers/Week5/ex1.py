'''1a. Create an ssh_conn function. This function should have three parameters: ip_addr, username, and password. The function should print out each of these three variables and clearly indicate which variable it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.
'''


def ssh_conn(ip_addr, username, password):
    print("IP Address {} Username {} Password {}".format(
        ip_addr, username, password))


# Using only positional arguments
ssh_conn('192.168.1.1', 'user1', 'password1')

# Using named arguments
ssh_conn(ip_addr='192.168.1.2', username='user2', password='password2')

# Using mix of positional and named arguments
ssh_conn('192.168.1.3', username='user3', password='password3')
