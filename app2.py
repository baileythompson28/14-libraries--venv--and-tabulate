import json
from tabulate import tabulate

with open("data.json") as d:
    customers = json.load(d)
total_orders = 0
total_items_sold = 0
total_profit = 0

for name in customers:
    print(f"customer: {name['name']}")
    table_data = []
    subtotal = 0

    for item in name['purchases']: #i can't tell if this is right, ig it is. nvm
        item_profit = (item['selling_price'] - item['cost_to_produce']) * item['quantity']
        total_item_price = item['selling_price'] * item['quantity']
        subtotal += total_item_price
        total_items_sold += item['quantity']
        total_profit += item_profit
    tax = subtotal * 0.06
    processingFee = 5.00
    orders = subtotal + tax + processingFee
    
    print(tabulate(table_data, headers=["item purchased", "selling price", "quantity", 
                                        "cost to produce", "total item profit", "total item price"], tablefmt="grid"))
    print(f"subtotal: ${subtotal:.2f}")
    print(f"tax (6%): ${tax:.2f}")
    print(f"processing fee: ${processingFee:.2f}")
    print(f"order total: ${orders:.2f}\n")
    total_orders += 1

print(f"total orders processed: {total_orders}")
print(f"total items sold: {total_items_sold}")
print(f"total profit processed: ${total_profit:.2f}")

