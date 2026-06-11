n = (int)(input("Enter your Number:"))
temp =n 
sq = n**2
sum =0
while(sq!=0):
 sum = sum + sq%10
 sq=sq//10

if(temp == sum):
  print("Neon Number")
else:
  print("Not a Neon Number ")
sum =0