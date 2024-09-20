0x08. Making Change

Project Description
In this project, you will solve the classic Coin Change Problem using dynamic programming and greedy algorithms.
The goal is to determine the minimum number of coins needed to make a given total amount,
using a list of coin denominations. Your solution will focus on correctness and efficiency.

Problem Statement
0. Change comes from within
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given total amount.

Function Prototype:

def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to make up the given total.

    Args:
        coins (List[int]): List of coin denominations.
        total (int): The total amount to achieve.

    Returns:
        int: Fewest number of coins needed, or -1 if not possible.
    """

Requirements:
If total is 0 or less, return 0.
If total cannot be met by any number of coins, return -1.
coins is a list of integers representing the values of the coins.
Assume infinite supply of each denomination.
Time complexity will be considered for evaluation.


Example:
bash

$ ./0-main.py
7
-1

