import os
import time

bids = {}
keep_running = True


def add_bid(name, amount):
    bids[name] = amount


def determine_winner(bids):
    bid_values = bids.values()
    max_value = max(bid_values)
    for key, value in bids.items():
        if value == max_value:
            print(f"Winner is {key} with amount {value}")


while keep_running:
    name = input("What is your name? : ")
    amount = int(input("What's your bid? : "))
    add_bid(name, amount)

    shall_continue = input("Are there any other bidders? yes/no : ").lower()
    if shall_continue == "no":
        keep_running = False
        determine_winner(bids)
    os.system("cls")
