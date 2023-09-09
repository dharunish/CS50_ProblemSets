import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        raise ValueError


def std_format(s):
    if "PM" in s:
        try:
            test = s.replace("PM", "")
            test = test.replace(" ", "")
            test = test.split(":")
            if len(test) > 1 and int(test[1]) > 59:
                raise ValueError
            if len(test[0]) == 1:
                test[0] = (f"0{test[0]}")
            if (test[0] == '12' and (len(test) == 1 or test[1] == '00')):
                pass
            else:
                test[0] = 12 + int(test[0])
            s = (f"{test[0]}:{test[1]}")
        except IndexError:
            s = (f"{test[0]}:00")
    else:
        try:
            test = s.replace("AM", "")
            test = test.replace(" ", "")
            test = test.split(":")
            if len(test) > 1 and int(test[1]) > 59:
                raise ValueError
            if len(test[0]) == 1:
                test[0] = (f"0{test[0]}")
            if (test[0] == '12' and (len(test) == 1 or test[1] == '00')):
                test[0] = '00'
            s = (f"{test[0]}:{test[1]}")
        except IndexError:
            s = (f"{test[0]}:00")

    return s

def format(h,m,meridium):
    if (m == ''):
        m = '00'
    if(int(m) > 59):
        raise ValueError
    if(meridium == 'AM' and h == '12' and m == '00'):
        h = '0'
        m = '0'
    elif(meridium == 'PM') and int(h) != 12:
        h = int(h) + 12
    return(f"{int(h):02}:{int(m):02}")

def convert(s):
    matches = re.search(r"(\d+):?(\d*)\s(AM|PM)\sto\s(\d+):?(\d*)\s(PM|AM)",s)
    if matches:
        first_h,first_m,first_meridium,last_h, last_m, last_meridium = matches.groups()
        first = format(first_h, first_m, first_meridium)
        last  = format(last_h, last_m, last_meridium)
        return (f"{first} to {last}")
    else:
        raise ValueError



if __name__ == "__main__":
    main()