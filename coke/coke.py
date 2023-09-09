
due = 50

while due > 0:
        print(f"Amount Due: {due}")
        money = int(input("Insert Coin: "))
        if money == 25 or money == 10 or money == 5:
            due = due - money

print(f"Change Owed: {due*-1}")


