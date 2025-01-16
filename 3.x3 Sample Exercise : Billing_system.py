# Basic python program to generate a bill

name = input("Enter Your Name: ")
item = input("Enter the Name of the Item: ")
quantity = int(input("Enter the Quantity of item: "))
price = int(input("Enter the Price of the Item: "))

print("*********************")
print("Name: ",name)
print("Item: ",item)
print("price: ",price)
print("Quantity: ",quantity)
print("Total: $",price*quantity)
print("*********************")
