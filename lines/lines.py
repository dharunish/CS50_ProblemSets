import sys
try:
    test = sys.argv[1].split(".")
    if sys.argv[1] == "":
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif test[1] != "py":
        print("Not a Python file")
        sys.exit(1)
    else:
        with open(sys.argv[1]) as file:
            count = 0
            lines = file.readlines()
            for line in lines:
                line = line.replace(" ", "")
                if line == "\n" or line[0] == "#":
                    pass
                else:
                    count = count + 1
            print(count)
except FileNotFoundError:
    print("File does not exist")
except IndexError:
    print("Not a CSV file")
