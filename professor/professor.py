import random


def main():
    level = get_level()
    question = 0
    correct = 0
    while True:
        if question == 10:
            print(f"Score: {correct}")
            break
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        incorrect = 0
        while True:
            answer = input(f"{x} + {y} = ")
            answer = int(answer)
            if answer == z:
                correct = correct + 1
                question = question + 1
                break
            else:
                print("EEE")
                incorrect = incorrect + 1
            if incorrect == 3:
                print(f"{x} + {y} = {z}")
                question = question + 1
                break

def get_level():
    while True:
        level = input("Level: ")
        if level != "1" and level != "2" and level != "3":
            continue
        else:
            break
    level = int(level)
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        return x
    elif level == 2:
        x = random.randint(10, 99)
        return x
    elif level == 3:
        x = random.randint(100,999)
        return x




if __name__ == "__main__":
    main()



