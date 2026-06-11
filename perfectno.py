
n = (int)(input("Enter your Number"))
sum = 0
# temp = n 
for i in range (1,n):
    if n % i ==0:
        sum =sum + i;
if n == sum:
    print("Number is Perfect Number")
else:
    print("Number is Not Perfect Number")

    
