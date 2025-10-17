import json
import sys

if len(sys.argv) != 2:
    print("Provide path to json file ")
    sys.exit(1)

orders_file = sys.argv[1]

try:
    with open(orders_file, 'r') as f:
        data = json.load(f)
except Exception as e:
    print(e)
    sys.exit(1)

print("END")