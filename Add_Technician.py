import random
import pandas as pd
import json


def add_tx():
    tx_list = []

    tx_add_number = int(input("Enter how many Tx you want to add :"))
    for i in range(tx_add_number):
        id = random.randint(100000 , 999999)
        name = input("enter tx name :")
        city = input("enter city name :")
        state = input("enter state name :")

        tx_list.append({
            "Tx_id" : id,
            "Tx_Name" : name,
            "Tx_city" : city,
            "Tx_state" : state
        })


    with open("Tx_details.json", "w") as file:
        json.dump(tx_list, file, indent=4)



add_tx()