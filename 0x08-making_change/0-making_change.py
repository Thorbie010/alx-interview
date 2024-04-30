#!/usr/bin/python3
""" Script for Making Change."""


def makeChange(coins, total):
    """ Function to determine the fewest number of coins needed to
    meet a given amount total in a pile of coins of different values,"""

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coins_count = 0
    remaining_total = total
    for coin in coins:
        while remaining_total >= coin:
            remaining_total -= coin
            coins_count += 1

    return coins_count if remaining_total == 0 else -1
