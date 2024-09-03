# This program computes the total price
# per the total number of books ordered
# for a specific purchase order.

numOfBooks = int(0)
subTotal = float()

SALESTAX = float(0.075)
SHIPPING = int(2)

subWithTax = int(0)
finalTotal = int(0)

# tells the user what the program does
print("This program calculates the total of a book order ")
print("including sales tax and shipping charges. ")
print(" ")

# asks user to input number of books in the order
numOfBooks = int(input("How many individual books are in the order? "))
numOfBooks = int(numOfBooks)
if numOfBooks <=0 :
    print (" ")
    print("Error: must be a whole number greater than zero. ")
    print(" ")
    numOfBooks = int(input("How many individual books are in the order? "))
    numOfBooks = int(numOfBooks)
else: numOfBooks >0
print("You entered: ", numOfBooks)
print(" ")

# asks user to input pre-tax subtotal of books
subTotal = (input("What is the subtotal price of the books? "))
subTotal = float(subTotal)
print("You entered: ", subTotal)
print(" ")
print(" ")

# computes the sales tax and adds to the subtotal
subWithTax = (subTotal * SALESTAX) + subTotal
print("The sales tax is 7.5% ")
print("and shipping costs $2 per book. ")

# adds $2 per book for individual shipping
finalTotal = subWithTax + (SHIPPING * numOfBooks)
finalTotal = round(finalTotal, 2)
print(" ")
print("...")
print(" ")

# prints total for subtotal, sales tax, and shipping price
print("The final total is: ","$", finalTotal)

