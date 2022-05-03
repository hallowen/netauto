import jinja2

fruits = ["Mango", "Orange", "Banana", "Guava"]

vars = {"fruits": fruits}

with open("jinja2/fruits.j2") as f_fruits:
    fruits_details = f_fruits.read()

t = jinja2.Template(fruits_details)
output = t.render(vars)
print(output)
