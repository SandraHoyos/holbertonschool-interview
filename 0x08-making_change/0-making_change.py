#!/usr/bin/python3
"""
Making Change Function with the few amount of coins
"""


def makeChange(coins: list, total: int) -> int:

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
