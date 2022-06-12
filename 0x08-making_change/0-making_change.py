#!/usr/bin/python3
"""
Program to determin the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine
    the fewest number of coins needed to meet a given amount total.
    Return: least number of coins necessary to meet total.
    - If total is 0 or less, return 0
    - If total cannot be met by any number of coins you have, return -1
    - value of a coin will always be an integer greater than 0
    - coins is a list of the values of the coins in your possession
    """
    if total <= 0:
        return 0

    valNew = total + 1
    store = {0: 0}

    for i in range(1, total + 1):
        store[i] = valNew

        for coin in coins:
            immediate = i - coin
            if immediate < 0:
                continue

            store[i] = min(store[immediate] + 1, store[i])

    if store[total] == total + 1:
        return -1

    return store[total]
