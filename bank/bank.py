

def main():
    answer = input("Greeting: ")
    print(f"${value(answer)}")


def value(answer):
    answer = answer.split()
    if answer[0] == "Hello" or answer[0] == "Hello,":
        return 0
    elif answer[0][0] == "H":
        return 20
    elif answer[0][0] != "H":
        return 100


if __name__ == "__main__":
    main()
