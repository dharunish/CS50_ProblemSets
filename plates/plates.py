def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    found_number = False
    if len(s) <= 6 and len(s) >= 2 and s[0].isalpha() and s[1].isalpha() and s[0] != 0:
        for c in s:
            if c.isalpha() or c.isnumeric():
                if c.isnumeric():
                    if found_number == False:
                        found_number = True
                        if c == "0":
                            return False

                if c.isalpha() and found_number == True:
                    return False
            else:
                return False
        return True
    return False








if __name__ == "__main__":
    main()