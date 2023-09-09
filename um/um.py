import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    start = re.findall(r"^um(\W|$)", s)
    end = re.findall(r"\Wum$",s)
    middle = re.findall(r"\Wum\W", s)
    return len(start+end+middle)




if __name__ == "__main__":
    main()