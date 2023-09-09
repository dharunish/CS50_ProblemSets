import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    matches = re.search('(https?://(?:www\.)?youtu)be.com/embed/(.+)"', s)
    if matches:
        first,last = matches.groups()
        return (f"https://youtu.be/{last}")

    else:
        return None

if __name__ == "__main__":
    main()


