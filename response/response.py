import validators

email = input("What is your email? ")
if validators.email(email) == True:
    print("Valid")
else:
    print("Invalid")





