import math
n = (int)(input("Enter your Number"))
sum =0
temp =n
while n!=0:
  sum = sum + math.factorial(n%10)
  n =n//10
if sum==temp:
  print("Strong Number")
else:
  print("Not Strong number")


