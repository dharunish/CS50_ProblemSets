#comment
def main():
    inp = input("What is the time? " )
    time = convert(inp)
    if time >= 7 and time <= 8:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time<= 19:
        print("dinner time")
    else:
        print("")

def convert(inp):
    time = inp.split(":")
    min = float(time[1]) / 60
    hour = float(time[0])
    time = (hour + min)
    return time

if __name__ == "__main__":
    main()