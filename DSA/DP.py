from os import *
from sys import *
from collections import *
from math import *

from typing import *
from sys import stdin

"""2D Dynamic Programming """
"""Triangle: https://leetcode.com/problems/triangle/description/"""
def minimumTotal(triangle: List[List[int]]) -> int:
        memo = {}
        def f(i,j):
            if i==len(triangle)-1: #can't exceed n-1 because if reaches there then base cond hit and prog stops
                return triangle[i][j]#why not minimum from last row ??
            if (i,j) in memo:
                return memo[(i,j)]
            p1 = f(i+1,j) + triangle[i][j]
            p2 = f(i+1,j+1) + triangle[i][j]
            memo[(i,j)]  = min(p1,p2)
            return memo[(i,j)]
        return f(0,0)


print(minimumTotal([[-10]]))




"""minimum path sum"""
def minPathSum(grid: List[List[int]]) -> int:
    """left to bottom right i.e 0 0 to m-1 , n-1"""
    memo = {}
    def f(m , n):
        if m==0 and n==0:
            return grid[0][0]
        if m<0 or n<0:
            return float('inf')
        if (m,n) in memo:
            return memo[(m,n)]
        up = grid[m][n] + f(m-1,n)
        left = grid[m][n] + f(m,n-1)
        memo[(m,n)] = min(up,left)
        return memo[(m,n)]
    return f(len(grid)-1,len(grid[0])-1)
# tabulation
def minPathSumII(grid:List[List[int]]) -> int:
    m,n= len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]

    for i in range(1,m):
        dp[0][i] = dp[0][i-1] + grid[0][i]

    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = min(dp[i-1][j] , dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]

print(minPathSum([[1,2,3],[4,5,6]]))
"""Unique pathII with obstacles -1"""
# def mazeObstacles(n, m, mat):
#     memo = {}
#     def f(i,j):
#         if i>=0 and j>=0 and mat[i][j]==-1:
#             return 0
#
#         if i<0 or j<0:
#             return 0
#         if i==0 and j==0:
#             return 1
#         # special memo
#         if (i,j) in memo:
#             return memo[(i,j)]
#         memo[(i,j)] =  f(i-1,j) + f(i,j-1)
#         return memo[(i,j)]
#     return f(n-1,m-1)
#     pass
# print(mazeObstacles())
"""count all path from (0,0) to (n-1,m-1): https://www.naukri.com/code360/library/count-all-number-of-paths-of-a-given-matrix"""
#using recursion
def countPaths1(i,j)->int:
    def f(m,n):
        if m==0 and n==0:
            return 1
        """i,j - > i-1,j and i,j-1"""
        if m<0 or n<0:
            return 0
        up = f(m-1,n)
        left = f(m,n-1)
        return up+left
    return f(i-1,j-1)
    pass
#memo
def countPath2(i, j):
    memo = {}
    def f(m,n):
        if m==0 and n==0:
            return 1
        if m<0 or n<0:
            return 0
        #special memo condition
        if (m,n) in memo:
            return memo[(m,n)]
        up = f(m-1,n)
        left = f(m,n-1)
        memo[(m,n)] = up + left
        return memo[(m,n)]
    return f(i-1,j-1)
    pass
#tabulation
# def countPath3(i, j):
#     dp = [[0 for _ in range(j + 1)] for _ in range(i + 1)]  # Corrected dimensions
#     for m in range(i + 1):
#         dp[m][0] = 0
#     for n in range(j + 1):
#         dp[0][n] = 0
#
#     dp[0][0] = 1
#     for m in range(1, i + 1):
#         for n in range(1, j + 1):
#             dp[m][n] = dp[m - 1][n] + dp[m][n - 1]
#
#     return dp[i][j]


# print(countPath3(3,2))


"""https://www.naukri.com/code360/problems/ninja-s-training_3621003?leftPanelTabValue=PROBLEM"""

#last performed for first is 3 which in no task performed as only 3 task are there with indices 0 1 2
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    def f(index,last_performed):
        #base condition 1
        if index == 0:
            maxi = -float('inf')
            for i in range(0,3):
                if i != last_performed:
                    maxi = max(maxi,points[0][i])
            return maxi

        maxi = -float('inf')
        for i in range(0,3):
            if i != last_performed:
                point = points[index][i] + f(index-1,i)
                maxi = max(maxi,point)

        return maxi
    return f(n-1,3)

    pass
#memoization
def ninjatraining(n: int, points: List[List[int]]) -> int:
    memo = {}
    def f(index,last):
        if index == 0:
            maxi = -float('inf')
            for i in range(0, 3):
                if i != last:
                    maxi = max(maxi, points[0][i])
            return maxi

        #special memo condition
        if (index,last) in memo:
            return memo[(index,last)]
        maxi = -float('inf')
        for i in range(0, 3):
            if i != last:
                point = points[index][i] + f(index - 1, i)
                maxi = max(maxi, point)
            memo[(index,last)] = maxi
        return memo[(index,last)]
    return f(n-1,3)


    pass
#tabulation
def ninjaTraning(n:int, points:List[List[int]])->int:
    dp = [[0 for _ in range(4)] for _ in range(4)]

    pass
print(ninjatraining(3,[[1,2,5],[3,1,1],[3,3,3]]))
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