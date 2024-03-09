import re
password = input("Input your password: ")
x = True
while x:

    if len(password) < 6:
        break
    elif len(password) > 16:
        break
    elif not re.search('[A-Z]', password):
        print("Capitalize password")
        break
    elif not re.search('[0-9]', password):
        print("Password missing 0-9")
        break
    elif not re.search('[a-z]', password):
        print("Password must have lower case")
        break
    elif not re.search("[$#@]", password):
        print("Password should have [$#@]")
        break
    elif re.search('\r', password):
        break
    else:
        print("Valid password")
        x = False
if x:
    print("Not a valid password")
