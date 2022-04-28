# Identify vendor details from MAC address

'''
Possible MAC address formats
MM:MM:MM:SS:SS:SS
MM-MM-MM-SS-SS-SS
MMM.MMM.SSS.SSS
'''
from email import header
from gettext import find
from mac_vendor_lookup import MacLookup, BaseMacLookup
from tabulate import tabulate

BaseMacLookup.cache_path = './macfinder/vendor_macs.txt'
mac = MacLookup()
mac.update_vendors()
mac_vendors_found = []

headers = ['MAC Address', 'Vendor']
with open('macfinder/mac_address.txt') as f_mac_addr:
    mac_addr_list = f_mac_addr.read().splitlines()


def find_mac(mac_addr):
    mac_vendors_found.append(mac.lookup(mac_addr))
    return mac_vendors_found


for mac_addr in mac_addr_list:
    try:
        find_mac(mac_addr)
    except:
        print("Vendor Not Found")


table = zip(mac_addr_list, mac_vendors_found)
print(tabulate(table, headers=headers, tablefmt="grid"))
