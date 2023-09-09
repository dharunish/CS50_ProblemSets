answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = answer.lower()
if answer[0] == ' ' or answer[-1] == ' ':
    answer = answer.replace(' ', '')
if answer == "42":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer == "forty two":
    print("Yes")
else:
    print("No")