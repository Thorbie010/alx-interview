#!/usr/bin/python3
""" A script for Prime Game."""


def isWinner(x, nums):
    """Function to determine the winner in a prime game between two players."""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    sieve = [True] * (max_num + 1)

    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_num + 1, i):
                sieve[j] = False

    prime_counts = [0] * (max_num + 1)
    count = 0
    for i in range(2, max_num + 1):
        if sieve[i]:
            count += 1
        prime_counts[i] = count

    player1_wins = sum(1 for n in nums if prime_counts[n] % 2 == 1)
    if player1_wins * 2 == len(nums):
        return None
    elif player1_wins * 2 > len(nums):
        return "Maria"
    else:
        return "Ben"
