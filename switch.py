n = (int)(input("Enter your Number"))
while(1):
    print()
    print("1.Automorphic")
    print("2.SPY")
    print("3.Exit")
    
    ch= (int)(input("Enter your choice"))

    match(ch):
        case 1:
            sq = n ** 2
            if str(sq).endswith(str(n)):
             print("Yes, it is an Automorphic number")
            else:
             print("No, it is not an Automorphic number")
        case 2:
            sum =0
            product =1
            while(n!=0):
                sum =sum + n%10
                product = product * n%10
                n =n//10
            if (sum==product):
                print("Number is spy")
            else:
                print("Not a spy number")
        case 3:
            break
        case _:
            print("invalid")
                    



