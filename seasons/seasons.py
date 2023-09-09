import datetime
from datetime import date
import inflect
import sys

def main():

    day = input("Date of Birth: ")
    if validate(day):
        pass
    else:
        print("Invalid date")
        sys.exit(1)

    print(total_time(day))



def validate(day):
    try:
        day = day.split("-")
        datetime.date(int(day[0]),int(day[1]),int(day[2]))
        return True
    except IndexError:
        return False
    except ValueError:
        return False


def total_time(day):
    today = date.today()
    day = day.split("-")
    a = datetime.date(today.year,today.month,today.day)
    b = datetime.date(int(day[0]),int(day[1]),int(day[2]))
    c = a-b
    minutes = c.total_seconds() / 60
    minutes = round(minutes)
    p = inflect.engine()
    words = p.number_to_words(minutes)
    words = words.capitalize()
    words = words.replace(" and", "")
    return f"{words} minutes"










if __name__ == "__main__":
    main()