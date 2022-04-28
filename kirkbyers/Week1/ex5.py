'''
You have the following three variables from the arp table of a router:

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS" mappings. The output should look like following:

             IP ADDR          MAC ADDRESS
-------------------- --------------------
        10.220.88.29       5254.abbe.5b7b
        10.220.88.30       5254.ab71.e119
        10.220.88.32       5254.abc7.26aa

Two columns, 20 characters wide, data right aligned, a header column.

'''
mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac1_split = mac1.split()
mac1_addr = mac1_split[1]
mac1_mac = mac1_split[3]

mac2_split = mac2.split()
mac2_addr = mac2_split[1]
mac2_mac = mac2_split[3]

mac3_split = mac3.split()
mac3_addr = mac3_split[1]
mac3_mac = mac3_split[3]

print("{:>20}{:>20}".format("IP ADDR", "MAC ADDRESS"))
print('-'*20 + " " + "-"*19)
print("{:>20}{:>20}".format(mac1_addr, mac1_mac))
print("{:>20}{:>20}".format(mac2_addr, mac2_mac))
print("{:>20}{:>20}".format(mac3_addr, mac3_mac))
