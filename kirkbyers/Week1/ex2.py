'''
2. Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its octets. Print out the octets in decimal, binary, and hex.

Your program output should look like the following:

​ $ python exercise2.py
Please enter an IP address: 80.98.100.240

    Octet1         Octet2         Octet3         Octet4
------------------------------------------------------------
      80             98             100            240
   0b1010000      0b1100010      0b1100100     0b11110000
     0x50           0x62           0x64           0xf0
------------------------------------------------------------

Four columns, fifteen characters wide, a header column, data centered in the column.
'''

ip_addr1 = input("Please enter an IP address ")

ip_addr1_list = ip_addr1.split(".")

oct1_dec = int(ip_addr1_list[0])
oct1_bin = bin(oct1_dec)
oct1_hex = hex(oct1_dec)

oct2_dec = int(ip_addr1_list[1])
oct2_bin = bin(oct2_dec)
oct2_hex = hex(oct2_dec)

oct3_dec = int(ip_addr1_list[2])
oct3_bin = bin(oct3_dec)
oct3_hex = hex(oct3_dec)

oct4_dec = int(ip_addr1_list[3])
oct4_bin = bin(oct4_dec)
oct4_hex = hex(oct4_dec)

print("\n")
print("{:^15}{:^15}{:^15}{:^15}".format(
    "Octet1", "Octet2", "Octet3", "Octet4"))
print("-"*60)
print("{:^15}{:^15}{:^15}{:^15}".format(
    oct1_dec, oct2_dec, oct3_dec, oct4_dec))
print("{:^15}{:^15}{:^15}{:^15}".format(
    oct1_bin, oct2_bin, oct3_bin, oct4_bin))
print("{:^15}{:^15}{:^15}{:^15}".format(
    oct1_hex, oct2_hex, oct3_hex, oct4_hex))
