import re 

name = input("what is your name: ")


if matches := re.search(r"^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(name)