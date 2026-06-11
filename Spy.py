n = (int)(input("Enter your Number"))
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

