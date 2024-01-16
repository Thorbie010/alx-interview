#!/usr/bin/python3
""" A script for minimum operations."""

def minOperations(n):
    if n <= 1:
        return 0

    # Initialize an array to store the minimum operations for each position
    dp = [float('inf')] * (n + 1)
    
    # Base case: 0 operations needed for an empty file
    dp[0] = 0
    
    # Iterate from 1 to n to fill the dp array
    for i in range(1, n + 1):
        # Try all possible factors of i
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                # Update the minimum operations for position i
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n] if dp[n] != float('inf') else 0