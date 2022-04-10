"""
1. Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract all of the VLAN_ID, VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data structure to the screen. Your output should look as follows:
[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
"""
vlan_details = []

with open("kirk_byers/Week3/show_vlan.txt", "r") as f_sh_vlan:
    lines = f_sh_vlan.readlines()
    for line in lines:
        if "Et6," in line or "VLAN" in line or "-----" in line:
            continue
        else:
            line_split = line.split()
            vlan_id = line_split[0]
            vlan_name = line_split[1]
            vlan_tuple = (vlan_id, vlan_name)
            vlan_details.append(vlan_tuple)

print(vlan_details)
