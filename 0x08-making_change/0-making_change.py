#!/usr/bin/python3
"""
Making Change Function with the few amount of coins
"""


def makeChange(coins: list, total: int) -> int:
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
    Returns: fewest number of coins needed to meet total
        - If total is 0 or < 0, return 0
        - If total cannot be met by any number of coins you have, return -1
        - Coins is a list of the values of the coins
        - The value of a coin will always be an integer greater than 0
        - You can assume you have an infinite number of each denomination
        of coin in the list
    """
    if total <= 0:
        return 0

    change = 0
    coins.sort(reverse=True)

    for coin in coins:
        temp_change = int(total / coin)
        total -= temp_change * coin
        change += temp_change
        if total == 0:
            return change
    if total != 0:
        return -1
