import json

def search_order():

    search_id = int(input("Enter Order ID: "))

    with open("orders.json", "r") as file:
        orders = json.load(file)

    for order in orders:

        if order["order_id"] == search_id:

            print("\nOrder Found!")
            print("--------------------------")
            print("Order ID:", order["order_id"])
            print("Service:", order["Order_name"])
            print("Price:", order["price"])
            print("State:", order["state"])
            print("City:", order["city"])

            return

    print("\nOrder not found!")

search_order()