from PIL import Image, ImageOps
import sys
import os


if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

elif os.path.isfile(sys.argv[1]) == False:
    print("Input does not exist")
    sys.exit(1)
first = sys.argv[1]
second = sys.argv[2]
first = first.split(".")
second = second.split(".")
if (first[1] != "png" and first[1] != "jpg") or (second[1] != "png" and second[1] != "jpg"):
    print("Invalid input")
    sys.exit(1)
elif first[1] != second[1]:
    print("Input and output have different extensions")
    sys.exit(1)
else:
    before = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    before = ImageOps.fit(before, shirt.size)
    before.paste(shirt,shirt)
    before.save(sys.argv[2])



