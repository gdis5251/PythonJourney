lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blendon wood. 32 inches high x 40 incheswide x 30 inches deep. Red or white
"""
lovely_loveseat_price = 254.00

stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
stylish_settee_price = 180.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15


sales_tax = 0.088

customer_one_total = 0

customer_one_itemization = ""

# Customer One Buy Lovely Loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

# Buy Luxurious Lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

# Customer's tax 
customer_one_tax = customer_one_total * sales_tax

# Customer Totally need to pay 
customer_one_total += customer_one_tax

print("Customer One Items:") 
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)





