for i in range(0,5):
    for j in range(0,5-i):
     if((i+j)%2==0):
        print(chr(65+j),end=" ")
     else:
        print(chr(97 +j),end =" ")
    print()    