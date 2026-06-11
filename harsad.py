n = (int)(input("Enter your Number"))
sum =0
temp =n
while n!=0:
    sum =sum+n%10
    n =n//10
if temp % sum==0:
    print("Number is harshad")
else:
    print("Number is Not harshad Number")