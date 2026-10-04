def check_password(pwd):
    has_upper=False
    has_digit=False
    has_special=False

    for i in range(len(pwd)):
        if 65<=ord(pwd[i])<=90:
            has_upper=True
            break
    if not has_upper:
        print("missing condition: upper case letter!!")

    for i in range(len(pwd)):
        if 48<=ord(pwd[i])<=57:
            has_digit=True
            break
    if not has_digit:
            print("missing condition: atleast one digit required!!")

#twist#
    for i in range(len(pwd)):
        if not pwd[i].isalnum():
            has_special = True
            break

    if not has_special:
        print("Missing condition: At least one special character is required!")


    if len(pwd) < 8:
        print("Missing condition: password must be at least 8 characters!!")

    if len(pwd)>=8 and has_upper and has_digit:
        print( "Strong")
    else:
        print( "Weak")

    


password=input("Enter your password here : ")
check_password(password)
    






