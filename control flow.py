# defining a function calculate discount that takes parameters original price and discount percentage
def calculate_discount(original_price, discount_percentage):
    # calculating discounted price
    discounted_price = original_price - (discount_percentage / 100) * original_price
    return discounted_price

# taking original price and discount percentage from user
original_price = float(input("Enter the original price:"))
discount_percentage = float(input("Enter the discount percentage:"))

# calling the function calculate discount with the given original price and discount percentage
discounted_price = calculate_discount(original_price, discount_percentage)

# displaying the discounted price in Rs
print("The Discounted Price Is: Rs",discounted_price)

# using conditional statements to categorize the item as low cost, moderate cost or hogh cost item
if discounted_price <= 50:
    print("Low-cost item.")
elif 50 <= discounted_price <= 100:
    print("Moderate-cost item.")
else:
    print("High-cost item.")