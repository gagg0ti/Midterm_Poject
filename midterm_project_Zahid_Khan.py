import json
import sys

if len(sys.argv) != 2:
    print("Provide path to json file ")
    sys.exit(1)

orders_file = sys.argv[1]

try:
    with open(orders_file, "r") as f:
        orders = json.load(f)
except Exception as e:
    print(e)
    sys.exit(1)

def phone_num_validation(phone):
    # Accept anything that can be turned into a string, then validate
    parts = str(phone).split('-')
    if len(parts) != 3:
        return False
    if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit() and len(parts[0]) == 3 and len(parts[1]) == 3 and len(parts[2]) == 4:
        return  True
    else:
        return False

customers = {}  # phone -> name
items = {}      # item_name -> {"price": number, "orders": number}

for order in orders:
    # customers
    name = order.get("name")
    phone = order.get("phone")
    if phone_num_validation(phone):
        customers[phone] = name

print(customers)

print("END")