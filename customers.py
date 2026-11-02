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

print("--- Exercise 5: Lookup Table ---")



print("--- Exercise 6: List of Dicts ---")



print("--- Exercise 7: Nested Catalog ---")



print("--- Exercise 8: Sales by Region ---")



### Self-Assessment Questions ###
# 1) 



# 2) 