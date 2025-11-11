#Exercise 2 shopping cart program 

item = input("what item would you like to buy?:")
price =float(input("what is the price"))
quantity = int(input('how many would you like?:'))
total = price * quantity

print(F"you have bouth {quantity} x {item}/s")
print(F"your total is:${total}")

