import sys

def main():
    while True:
        fraction = input("Fraction: ")
        try:
            amount = convert(fraction)
        except ZeroDivisionError:
            print("Cannot Divide by Zero")
            continue
        except ValueError:
            print("Not proper fraction format")
            continue

        result = gauge(amount)
        print(result)
        break


def convert(fraction):
    fraction = fraction.split("/")
    num = int(fraction[0])
    den = int(fraction[1])
    decimal = num/den
    decimal = (decimal*100)
    amount = round(decimal)

    if den != 0 and num > den:
        raise ValueError
    else:
        return amount



def gauge(amount):

        if amount >= 99:
            return "F"
        elif amount <= 1:
            return "E"
        else:
            return (f"{amount}%")





if __name__ == "__main__":
    main()
