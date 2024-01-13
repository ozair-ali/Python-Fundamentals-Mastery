# defining a function calculate discount that takes parameters original price and discount percentage
def calculate_discount(original_price, discount_percentage):
    # calculating discounted price
    discounted_price = original_price - (discount_percentage / 100) * original_price
    return discounted_price

# calling the function calculate discount with an original price and discount percentage
discounted_price = calculate_discount(10000,10)

# displaying the discounted price in Rs
print("The Discounted Price Is: Rs",discounted_price)