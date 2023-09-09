
from pyfiglet import Figlet
import sys
import random
figlet = Figlet()

fontList = figlet.getFonts()
if len(sys.argv) < 2:

    f = random.choice(fontList)
elif sys.argv[1] != "-f" and sys.argv[1] != "--font":
    sys.exit("Invalid Usage")
else:

    f = sys.argv[2]




figlet.setFont(font=f)
s = input("Input: ")
print(figlet.renderText(s))

