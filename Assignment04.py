products = []
n = int(input("Enter number of products: "))

for i in range(n):
    temp = {}

    name = input("Enter product name: ")
    stock = int(input("Enter stock quantity: "))
    
    temp["name"] = name
    temp["stock"] = stock
    
    products.append(temp)

print("\nAll products:")
for product in products:
    print(product["name"], "-", product["stock"])

print("\nProducts with stock less than 10:")
for product in products:
    if product["stock"] < 10:
        print(product["name"], "-", product["stock"])