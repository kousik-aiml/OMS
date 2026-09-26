from random import randint, choice
import json
from States_city import West_Bengal
from Order_name import order


def create_order():

    order_list = []

    number_of_orders = int(
        input("Enter how many orders you want to create: ")
    )

    for i in range(number_of_orders):

        order_id = randint(100000, 999999)

        city = choice(West_Bengal)

        # Random service name + price
        ord_name, price = choice(list(order.items()))

        new_order = {
            "order_id": order_id,
            "Order_name": ord_name,
            "price": price,
            "state": "West Bengal",
            "city": city
        }

        order_list.append(new_order)

        print("Order created successfully")

    # Save orders
    with open("orders.json", "w") as file:
        json.dump(order_list, file, indent=4)

    print("\nOrders saved successfully!")
    print(order_list)


create_order()