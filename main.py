from Add_Technician import add_tx
import Assign_tx
import Complete_orders
from Create_order import create_order
import Generate_Report
import Log_out
import Mark_order_dispute
import Order_name
from search_orders import search_order
from Search_tx import search_Tx
from States_city import West_Bengal
import Update_payment
from view_orders import view_orders
import View_Technician


def wanted_choices(per):

    if per == 1:
        create_order()

    elif per == 2:
        search_order()

    elif per == 3:
        search_Tx()

    elif per == 4:
        view_orders()

    elif per == 5:
        add_tx()

    else:
        print("Enter a valid number")


choice = int(input("Enter your choice: "))

wanted_choices(choice)