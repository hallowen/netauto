"""
2. Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this file. Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a separate variable.

Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1 is found, print out the string "Default gateway IP/Mac" and the corresponding IP address and MAC Address.

Using a conditional statement, also search for '10.220.88.30'. If this IP address is found, then print out "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.

Keep track of whether you have found both the Default Gateway and the Arista3 switch. Once you have found both of these devices, 'break' out of the for loop.
"""
C1 = C2 = False

with open("kirk_byers/Week3/show_arp.txt") as f_sh_arp:

    sh_arp_lines = f_sh_arp.readlines()

    for line in sh_arp_lines:

        f_sh_arp_split = line.split()

        if f_sh_arp_split[0] == "Protocol":
            continue
        ip_addr = f_sh_arp_split[1]
        mac_addr = f_sh_arp_split[3]

        if ip_addr == "10.220.88.1":
            print("Default gateway IP/Mac is {}/{}".format(ip_addr, mac_addr))
            C1 = True

        elif ip_addr == "10.220.88.30":
            print("Arista3 IP/Mac is {}/{}".format(ip_addr, mac_addr))
            C2 = True

        if C1 and C2:
            break
