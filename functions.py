#Question 1

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
#Question 2
 
 #prompt user for input

price = float(input("Enter the original price:"))
discount_percent = float (input("Enter the discount percentage:"))

#calculate the final price after discount
final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print("final price after discount is:", final_price)
else:
    print("No discount applied. The price remains:", final_price)    
    
