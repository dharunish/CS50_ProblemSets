file = input("File Name: ")
file = file.split(".")
file[-1] = file[-1].lower()
file[-1] = file[-1].replace(" ", "")
if len(file) > 1 and (file[-1] == "gif" or file[-1] == "png"):
    print(f"image/{file[-1]}")
elif len(file) > 1 and (file[-1] == "jpg" or file[-1] == "jpeg"):
    print("image/jpeg")
elif len(file) > 1 and (file[-1] == "pdf" or file[-1] == "zip"):
    print(f"application/{file[-1]}")
elif len(file) > 1 and file[-1] == "txt":
    print(f"text/plain")
else:
    print("application/octet-stream")