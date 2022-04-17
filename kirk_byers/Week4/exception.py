a = {"name": "Sandeep Suresh", "nationality": "Indian"}

try:
    print(a["name"])
except KeyError:
    print("Invalid key")
else:
    print("You have entered a correct key")
