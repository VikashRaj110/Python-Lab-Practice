
bill = 0
items = 0

n = int(input("Enter number of items: "))

for i in range(n):
    print("Items :" ,i+1)
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    amount = quantity * price
    bill += amount
    items += quantity

    print(name, "cost of item =", amount)

print("Total items purchased:",items)
print("Total bill amount:" , bill)