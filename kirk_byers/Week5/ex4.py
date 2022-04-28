'''3. Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following format:

01:23:45:67:89:AB

This function should handle the lower-case to upper-case conversion.

It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.

The function should have one parameter, the mac_address. It should return the normalized MAC address

Single digit bytes should be zero-padded to two digits. In other words, this:

a:b:c:d:e:f

should be converted to:

0A:0B:0C:0D:0E:0F

Write several test cases for your function and verify it is working properly.
'''


def mac_addr_normalize(mac_addr):

    mac_addr_fixed = []
    mac_addr_merge = []
    mac_addr_final = []

    if ':' in mac_addr:
        mac_addr_split = mac_addr.split(':')

        for i in mac_addr_split:
            if len(i) < 2:
                mac_addr_fixed.append(i.zfill(2))
            else:
                mac_addr_fixed.append(i)

        mac_addr_final = ':'.join(mac_addr_fixed)

    elif '-' in mac_addr:
        mac_addr_split = mac_addr.split('-')

        for i in mac_addr_split:
            if len(i) < 2:
                mac_addr_fixed.append(i.zfill(2))
            else:
                mac_addr_fixed.append(i)

        mac_addr_final = ':'.join(mac_addr_fixed)
    elif '.' in mac_addr:
        mac_addr_split = mac_addr.split('.')
        for i in mac_addr_split:
            if len(i) < 4:
                mac_addr_fixed.append(i.zfill(4))
            else:
                mac_addr_fixed.append(i)
        for i in mac_addr_fixed:
            mac_addr_fixed_split_left = i[:2]
            mac_addr_fixed_split_right = i[2:]
            mac_addr_merge.append(mac_addr_fixed_split_left)
            mac_addr_merge.append(mac_addr_fixed_split_right)
        mac_addr_final = ':' . join(mac_addr_merge)
    return mac_addr_final


with open('kirk_byers/Week5/mac_addr.txt') as f_mac_addr:
    mac_addr_list = f_mac_addr.read().splitlines()

for mac_addr in mac_addr_list:
    print((mac_addr_normalize(mac_addr)).upper())
