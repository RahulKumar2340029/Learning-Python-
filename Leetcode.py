from os import *
from sys import *
from collections import *
from math import *
from typing import List


# class Solution(object):
#     def checkSubarraySum(self, nums, k):
#         if len(nums) == 1:
#             return False
#
#         presum = [0]*(len(nums)+1)
#         presum[0] = 0
#         for i in range(1,len(presum)):
#             presum[i] = presum[i-1] + nums[i-1]
#
#         r = 2;
#         while r < len(presum):
#             for i in range(0,r-2):
#                 if presum[r]%k==0 or (presum[r] - presum[i])%k==0:
#                     return True
#
#             r+=1
#
#         return False


# class Solution(object):
#     def checkSubarraySum(self, nums, k)->bool:
#         if len(nums) ==1:
#             return False
#
#         remainder_map = {0:-1}
#         n = len(nums)
#         current_sum = 0;
#         for i in range(n):
#             current_sum+=nums[i]
#             remainder = current_sum%k
#
#             if remainder in remainder_map:
#                 if i - remainder_map[remainder]>1:
#                     return True
#             else:
#                 remainder_map[remainder] = i
#
#         return False


# object creation ans main function
# nums = [2,4,3]
# k = 6
# first = Solution();
# ans = first.checkSubarraySum(nums,k)
# print(ans)


# class Solution(object):
#     def clearDigits(self, s):
#         stack = []
#         for i in range(0,len(s)):
#             if s[i].isdigit():
#                 stack.pop()
#             else:
#                 stack.append(s[i])
#         ans = ""
#         for ele in stack:
#             ans += ele
#         return ans
#
# first = Solution();
# ans = first.clearDigits("cb34")
# print(ans)
# class Solution:
#     def valueAfterKSeconds(self, n:int, k:int)->int:
#         MOD = 10**9 + 7
#         arr = [1] * n
#         presum = [0] * (n + 1)
#         while k > 0:
#             for i in range(1, n + 1):
#                 presum[i] = (presum[i - 1] + arr[i - 1]) % MOD
#             for i in range(n):
#                 arr[i] = presum[i + 1]
#
#             k -= 1
#         return arr[n-1]
# solve = Solution()
# ans = solve.valueAfterKSeconds(5,3)
# print(ans)

class Solution(object):
    def numberOfChild(self, n, k) -> int:
        if k < n:
            return k
        t = k // (n - 1)
        if (t & 1) == 0:
            return k % (n - 1)
        else:
            return n - k % (n - 1) - 1


def minSubarraySum(arr, n, k) -> int:
    i, j = 0, 0
    c_sum = 0
    min_sum = float('inf')
    while j < len(arr):
        c_sum += arr[j]
        if (j - i + 1 < k):
            j += 1
        else:
            min_sum = min(min_sum, c_sum)
            c_sum -= arr[i]
            i += 1
            j += 1

    return min_sum


ans = minSubarraySum([-21, 15, 14, 22, -4, 28, 24, -4, 14, -12, 3, -7, 22, -26, -28, 1, -11, 6, 6], 19, 9)


# print(ans)
#leetcode day 09-06-2024 challenge
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_map = {0: 1}
        n = len(nums)
        sum, result = 0, 0
        for i in range(0, n):
            sum += nums[i]
            rem = sum % k

            if rem < 0:
                rem += k

            if rem in remainder_map:
                result += remainder_map[rem]
                remainder_map[rem] += 1
            else:
                remainder_map[rem] = 1
        return result


if __name__ == '__main__':
    pass
