from tabulate import tabulate
import csv
import sys
try:
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    test = sys.argv[1].split(".")
    if test[1] != "csv":
        print("Not a CSV file")
        sys.exit(1)
    else:
        with open(sys.argv[1]) as csv_file:
            reader = csv.reader(csv_file)
            rows = [row for row in reader]
            headers = rows[0]
            print(tabulate(rows[1:], headers, tablefmt="grid"))
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)

