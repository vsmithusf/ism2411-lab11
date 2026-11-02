# customers.py
# Author: Van Smith
# Module 11 Lab: Customer Dictionary & Lookup

print("--- Exercise 1: One Customer ---")
customer = {
    "name": "Alice", # Key : Value,
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

print("--- Exercise 2: Update and Add ---")
customer['phone'] = '555-5555' # Adding a new key-value pair to the dictionary
print(customer)
customer['tier'] = 'platinum' # Updating the value of an existing key
print(customer)
del customer['email'] # Deleting a key-value pair from the dictionary
print(customer)

print("--- Exercise 3: Safe Lookup ---")
print(customer.get('email', 'no email on file'))

# try:
#     print(customer["email"])
# except KeyError as error:
#     print("KeyError caught: ", error)

print("--- Exercise 4: Iterate ---")
for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, ":", customer[something])

# Iterating with .items() iterates directly over the key-value pairs as tuples, which unpacks them in the loop without extra look-ups.
# Iterating without .items() only interates over the keys, which means that you have to manually access the corresponding value inside 
# the loop instead.

print("--- Exercise 5: Lookup Table ---")
tier_discounts = {
    "bronze": 0,
     "silver": 0.05, 
     "gold": 0.1, 
     "platinum": 0.15
}

purchase = 300
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")

print("--- Exercise 6: List of Dicts ---")
customers = [ 
    {"name": "Bob", "tier": "silver", "ytd_spend": 1200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 2500},
    {"name": "David", "tier": "bronze", "ytd_spend": 500},
]
for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} off a $300 purchase")

print("--- Exercise 7: Nested Catalog ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product_name, product_details in catalog.items():
    if product_details["stock"] < 20:
        print(f"LOW STOCK: {product_name} -- only {product_details['stock']} left")

print("--- Exercise 8: Sales by Region ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount
print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")


### Self-Assessment Questions ###
# 1) Bracket notation should be used when you are sure the key exists and want to raise an error if it doesn't. A real-world example
# of this would be if missing a key is a real problem, such as with a password value.
# .get() notation should be used if a key might be missing and you want a safe default value to fall back to. A real-world example of
# this would be for an optional value, such as with an optional email or phone number value.

# 2) The summary dictionary from Exercise 8 reminds me of creating new columns with computations that use values from other columns.
# Using Python instead of Excel for larger datasets in this regard would be useful because it would then be more concise and easier to
# read and pick values from than an extremely large Excel table.