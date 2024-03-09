def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

# Prompting the user to enter the original price and discount percentage of product
Actual_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculating the final price after applying the discount percentage.
final_price = calculate_discount(Actual_price, discount_percent)

# Printing the final price after applying the discount or the original price if no discount was applied
if final_price != Actual_price:
    print("Final price after applying discount:", final_price)
else:
    print("No discount applied. Actual price:", Actual_price)