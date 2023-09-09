import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    ip = ip.split(".")
    if len(ip) != 4:
        return False
    elif int(ip[0]) > 255 or int(ip[1]) > 255 or int(ip[2]) > 255 or int(ip[3]) > 255:
        return False
    elif int(ip[0]) < 0 or int(ip[1]) < 0 or int(ip[2]) < 0 or int(ip[3]) <0:
        return False

    else:
        return True



...


if __name__ == "__main__":
    main()