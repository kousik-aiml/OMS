import json

def search_Tx():

    search_id = int(input("Enter Tx ID: "))

    with open("Tx_details.json", "r") as file:
        tx_detail = json.load(file)

    for tx in tx_detail:

        if tx["Tx_id"] == search_id:

            print("\nOrder Found!")
            print("--------------------------")
            print("TX ID:", tx["Tx_id"])
            print("Name:", tx["Tx_Name"])
            print("City:", tx["Tx_city"])
            print("State:", tx["Tx_state"])


            return

    print("\nOrder not found!")

search_Tx()