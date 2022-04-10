"""
3.  Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the lines until you have encountered the remote "System Name" and remote "Port id". Save these two items into variables and print them to the screen. You should extract only the system name and port id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your loop once you have retrieved these two items.
"""
C1 = C2 = False

with open("kirk_byers/Week3/show_lldp_neighbors_detail.txt") as f_sh_lldp_neig:
    lines = f_sh_lldp_neig.readlines()
    for line in lines:
        if "System Name" in line:
            line_split = line.split()
            system_name = line_split[2]
            print("System Name: {}".format(system_name))
            C1 = True

        elif "Port id" in line:
            line_split = line.split()
            port_id = line_split[2]
            print("Port ID: {}".format(port_id))
            C2 = True
        if C1 and C2:
            break
