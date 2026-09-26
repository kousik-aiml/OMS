import json

def view_orders():

    with open("orders.json", "r") as file:
        orders = json.load(file)

    for order in orders:
        print("-----------------------------")
        print("Order ID:", order["order_id"])
        print("Service:", order["Order_name"])
        print("Price:", order["price"])
        print("State:", order["state"])
        print("City:", order["city"])


view_orders()