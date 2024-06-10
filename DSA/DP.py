from os import *
from sys import *
from collections import *
from math import *

from typing import *
from sys import stdin

"""https://leetcode.com/problems/house-robber/description/"""
"""Memoization"""
def rob(nums: List[int]) -> int:
    memo = {}
    def f(index):
        # condition 1
        if index==0:
            return nums[index]
        # condition 2
        if index in memo:
            return memo[index]
        # condition 3
        if index<0:
            return 0
        pick = f(index-2) + nums[index]

        not_pick = f(index-1)
        return max(pick,not_pick)
    return f(len(nums)-1)

# print(rob([104,209,137,52,158,67,213,86,141,110,151,127,238,147,169,138,240,185,246,225,147,203,83,83,131,227,54,78,165,180,214,151,111,161,233,147,124,143]))
"""--------------------------------------------------------------------------------------------------------------------------------------"""
# tabulation
def rob(nums: List[int]) -> int:
    dp = [0]*(len(nums)+1)
    dp[0] = nums[0]
    if len(nums)==1:return dp[0]
    dp[1] = max(nums[0],nums[1])
    for i in range(2,len(nums)):
        dp[i] = max(dp[i-1],dp[i-2] + nums[i])
    return dp[len(nums)-1]

"""--------------------------------------------------------------------------------------------------------------------------------------"""
# def maximumNonAdjacentSum(nums):
#     if not nums:
#         return 0
#
#     n = len(nums)
#     memo = [0] * n
#     memo[0] = nums[0]
#
#     for i in range(1, n):
#         memo[i] = max(nums[i], memo[i - 1])
#         if i - 2 >= 0:
#             memo[i] = max(memo[i], nums[i] + memo[i - 2])
#
#     return memo[-1]
#
# # Main.
# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split(" ")))
#     print(maximumNonAdjacentSum(arr))

"""frog jump dp"""
def frogJump(n: int, heights: List[int]) -> int:
    memo = {}
    def f(index):
        if index==0:
            return 0
        if index in memo:
            return memo[index]
        left = f(index-1) + abs(heights[index] - heights[index-1])
        right = float('inf')
        if index-1>0:
            right = f(index-2) + abs(heights[index] - heights[index-2])

        memo[index] = min(left, right)
        return memo[index]
    return f(len(heights)-1)
    pass

print(frogJump(4,[10,20,30,10]))