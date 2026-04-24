import json
from pathlib import Path

try:
    from tabulate import tabulate
except ModuleNotFoundError:
    tabulate = None


def load_customers(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().strip()

    if not content:
        return []

    return json.loads(content)


def print_purchase_table(table_data):
    headers = [
        "item purchased",
        "selling price",
        "quantity",
        "cost to produce",
        "total item profit",
        "total item price",
    ]

    if tabulate:
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        return

    print(" | ".join(headers))
    print("-" * 95)
    for row in table_data:
        print(" | ".join(str(value) for value in row))


data_file = Path(__file__).with_name("data.json")
customers = load_customers(data_file)

if not customers:
    print(f"No customer data found in {data_file.name}.")
else:
    total_orders = 0
    total_items_sold = 0
    total_profit = 0

    for customer in customers:
        customer_name = customer.get("name", "Unknown Customer")
        purchases = customer.get("purchases", [])

        print(f"Customer Name: {customer_name}")
        table_data = []
        subtotal = 0

        for purchase in purchases:
            item_name = purchase.get("item_purchased", "Unknown Item")
            selling_price = purchase.get("selling_price", 0)
            quantity = purchase.get("quantity", 0)
            cost_to_produce = purchase.get("cost_to_produce", 0)

            item_profit = (selling_price - cost_to_produce) * quantity
            total_item_price = selling_price * quantity
            subtotal += total_item_price
            total_items_sold += quantity
            total_profit += item_profit
            table_data.append(
                [
                    item_name,
                    f"${selling_price:.2f}",
                    quantity,
                    f"${cost_to_produce:.2f}",
                    f"${item_profit:.2f}",
                    f"${total_item_price:.2f}",
                ]
            )

        tax = subtotal * 0.06
        processing_fee = 5.00
        order_total = subtotal + tax + processing_fee

        print_purchase_table(table_data)
        print(f"subtotal: ${subtotal:.2f}")
        print(f"tax (6%): ${tax:.2f}")
        print(f"processing fee: ${processing_fee:.2f}")
        print(f"order total: ${order_total:.2f}\n")
        total_orders += 1

    print(f"total orders processed: {total_orders}")
    print(f"total items sold: {total_items_sold}")
    print(f"total profit processed: ${total_profit:.2f}")
