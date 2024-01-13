# defining a dictionary containing information about a customer
customer_info = {'Name': 'Abdullah','Age':30,'Purchase History': ['Cloths', 'Shoes', 'Books','Food']}

# extracting name of the customer and displaying it
customer_name = customer_info['Name']
print("Customer's Name:", customer_name)

# extracting purchase history of the customer and displaying his second purchase
purchase_history = customer_info['Purchase History']
second_purchase = purchase_history[1]
print("Second Purchase: {second_purchase}")