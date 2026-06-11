import math
a = int(input("N: "))
print (a)
m = sum(math.factorial(int(i)) for i in str(a))
if a==m:
    print("Strong Number")
else:
    print("Not a Strong Number")
