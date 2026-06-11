import keyword
spe = " "
str  = input("Enter name: ")

if keyword.iskeyword(str) ==False:
    if str[0] not in spe and str[0] not in digit:
        for i in str[1:]:
            if i in spe :
                print("Not Valid")
                break
            else:
                print("valid variable")
        else:
            print("invalid ")
else:
    print("invalid due to reserved keyword")