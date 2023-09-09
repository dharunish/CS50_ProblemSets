food = {}
while True:
    try:
        item = input("")
        item = item.upper()

        if item in food:
            food[item] = food[item] + 1
        else:
            food[item] = 1

    except EOFError:
        break

a = sorted(food)

for c in a:
    print(f"{food[c]} {c}")

