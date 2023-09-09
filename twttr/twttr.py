

def main():
    text = input("Input: ")
    text = shorten(text)
    print(text)


def shorten(text):
    for c in text:
        if c == "a" or c == "A" or c == "e" or c == "E" or c == "i" or c == "I" or c == "o" or c == "O" or c == "u" or c == "U":
            text = text.replace(c, "")

    return text


if __name__ == "__main__":
    main()