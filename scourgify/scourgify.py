import csv
import sys
import os

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
elif os.path.isfile(sys.argv[1]) == False:
    print(f"Could not read {sys.argv[1]}")
    sys.exit(1)
else:
    with open(sys.argv[1]) as in_file, open(sys.argv[2], "w",newline="") as out_file:
        reader = csv.reader(in_file)
        writer = csv.writer(out_file)
        rows = [row for row in reader]
        header = 0
        for row in rows:
            if header == 0:
                header = 1
                writer.writerow(["first", "last", "house"])
            else:
                name = row[0].replace('""', "")
                name = name.replace(" ", "")
                name = name.split(",")
                writer.writerow([name[-1], name[0], row[1]])



