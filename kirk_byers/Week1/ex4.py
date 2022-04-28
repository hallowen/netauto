'''
Create a show_version variable that contains the following

 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.

'''

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
sh_version_stripped = show_version.strip()
sh_version_list = sh_version_stripped.split()
dev_model = sh_version_list[1].strip()
dev_serial = sh_version_list[2].strip()

print('Cisco' in dev_model)
print('881' in dev_model)
print(f"Serial No: {dev_serial} Model No: {dev_model}")
