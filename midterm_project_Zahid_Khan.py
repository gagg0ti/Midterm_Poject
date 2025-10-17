"""
Midterm Project - Dosa Restaurant Order Processor
Author: Zahid Arafat Khan
Reads orders JSON file and generates two files:
  - customers.json: maps phone numbers to customer names
  - items.json: maps item names to price and orders
Usage:
    python midterm_project_Zahid_Khan.py example_orders.json
"""

import json
import sys

if len(sys.argv) != 2:
    print("Usage: python midterm_project_Zahid_Khan.py [orders_file.json]")
    sys.exit(1)

orders_file = sys.argv[1]

try:
    with open(orders_file, "r") as f:
        orders = json.load(f)
except FileNotFoundError:
    print("File not found.")
    sys.exit(1)
except json.JSONDecodeError:
    print("Invalid JSON format.")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)

def phone_num_validation(phone_number):
    """Return True if phone number matches pattern xxx-xxx-xxxx where each x is a digit."""
    parts = str(phone_number).split('-')
    if len(parts) != 3:
        return False
    if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit() and len(parts[0]) == 3 and len(parts[1]) == 3 and len(parts[2]) == 4:
        return True
    else:
        return False

customers = {}
items = {}

for order in orders:
    name = order.get("name")
    phone = order.get("phone")
    if phone_num_validation(phone):
        customers[phone] = name
    for item in order.get("items", []):
        if not isinstance(item, dict):
            continue
        item_name = item.get("name")
        price = item.get("price")
        if item_name not in items:
            items[item_name] = {"price": price, "orders": 0}
        items[item_name]["orders"] += 1

with open("customers.json", "w") as f:
    json.dump(customers, f)

with open("items.json", "w") as f:
    json.dump(items, f)

print("Files created Successfully")