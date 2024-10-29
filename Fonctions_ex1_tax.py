def calculate_tax(price):
    price = price * 1.1
    return price


calculate_tax(100)

#ou :

def calculate_tax(price):
    tax_amount = 0.10 * price
    updated_price = price + tax_amount
    return updated_price
