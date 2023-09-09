import random
while True:
    level = input("Level: ")
    if level.isnumeric():
        level = int(level)
        if level < 0:
            continue
        number = random.randint(0,level)
        break
    else:
        continue
while True:
    guess = input("Guess: ")
    if guess.isnumeric():
        guess = int(guess)
        if guess > level:
            continue
        elif guess < 0:
            continue
        if number > guess:
            print("Too small!")
        elif number < guess:
            print("Too large!")
        elif number == guess:
            print("Just right!")
            break
    else:
        continue