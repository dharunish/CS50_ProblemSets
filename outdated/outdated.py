
dates = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}

while True:
    date = input("Date: ")
    date = date.replace('"', "")
    if date[0].isnumeric() or date[0] == " ":
        day = date.split()
        if len(day) > 2:
              continue
        day = date.replace(" ", "")
        day = day.split("/")
        if int(day[0]) > 12:
              continue
        if int(day[1]) > 31:
              continue
        if len(day[0]) == 1:
                day[0] = f"0{day[0]}"
        if len(day[1]) == 1:
                day[1] = f"0{day[1]}"
        print(f"{day[2]}-{day[0]}-{day[1]}")
        break


    else:
        day = date.split(" ")
        if len(day) != 3:
              continue
        if day[1][-1] != ",":
            continue
        day[1] = day[1].replace(",", "")
        if day[0] in dates:
                day[0] = dates[day[0]]
        else:
            continue

        if int(day[1]) > 31:
              continue
        if len(day[1]) == 1:
                day[1] = f"0{day[1]}"
        print(f"{day[2]}-{day[0]}-{day[1]}")
        break
