
name = input ("camelCase: ")

for c in name:
    if c.isupper():
        c = c.replace(c, f"_{c.lower()}")
    print(c, end="")
print("")

