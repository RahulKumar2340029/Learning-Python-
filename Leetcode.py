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

# leetcode day 10-06-2024 challenge
def heightChecker( heights: List[int]) -> int:
    expected = sorted(heights)
    print(list(zip(expected,heights)))
    count = sum(a!=b for a,b in zip(expected,heights))

    return count

#leetcode day 11--6-2024 challenge
def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    ans = []
    count = defaultdict(int)
    for num in arr1:
        count[num]+=1

    for num in arr2:
        while count[num] > 0:
            ans.append(num)
            count[num]-=1

    for num in sorted(set(arr1) - set(arr2)):
        while count[num] > 0:
            ans.append(num)
            count[num]-=1


    return ans

# leetcode day 12-06-2024 Dutch National Flag algo
def sortColors(nums: List[int]) -> None:
    low,mid,high = 0,0,len(nums)-1
    while(mid <= high):
        if nums[mid] == 0:
            nums[mid],nums[low] = nums[low],nums[mid]
            mid+=1
            low+=1
        elif nums[mid] == 1:
            mid+=1
        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high-=1

arr = [2,0,2,1,1,0]
sortColors(arr)
print(arr)
# leetcode day 13-06-2024
"""https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/"""
# def minMovesToSeat(seats: List[int], students: List[int]) -> int:
#     count_seats,count_students = [0]*100,[0]*100
#     for ele in seats:

# leetcode 14-06-2024
def minIncrementForUnique(nums: List[int]) -> int:
    nums.sort()
    ans = 0
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            ans+=1
            nums[i]+=1
        elif nums[i] <  nums[i-1]:
            to_make_equal = abs(nums[i] - nums[i-1])
            ans+=to_make_equal+ 1
            nums[i]+=to_make_equal + 1

    return ans

print(minIncrementForUnique([1,2,2]))
# # 1 1 2 2 3 7
"""class BrowserHistory:"""
#     def __init__(self, homepage: str):
#         self.st1 = [homepage];
#         self.st2 = []
#
#     def visit(self, url: str) -> None:
#         self.st2.clear()
#         self.st1.append(url)
#     def back(self, steps: int) -> str:
#         while steps != 0 and len(self.st2)!=0:
#             self.st2.append(self.st1.pop())
#             steps-=1
#         return self.st1.pop()
#     def forward(self, steps: int) -> str:
#         while steps!=0 and len(self.st2)!=0:
#             self.st1.append(self.st2.pop())
#             steps-=1
#         self.st1.pop()

"""Method2 very intuitive"""
class Node:

    def __init__(self,value:str):
        self.value = value
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self,homepage:str):
        self.current = Node(homepage)

        def main():
            import sys
            input = sys.stdin.read
            data = input().split()

            n = int(data[0])
            blocks = list(map(int, data[1:n + 1]))

            end_pos = (n // 2) + (n % 2)

            for i in range(0, end_pos, 2):
                blocks[i], blocks[n - 1 - i] = blocks[n - 1 - i], blocks[i]

            print(" ".join(map(str, blocks)))

        if __name__ == "__main__":
            main()

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev is not None:
            steps-=1
            self.current = self.current.prev
        return self.current.value

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next is not None:
            steps-=1
            self.current = self.current.next

        return self.current.value


















# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)









if __name__ == '__main__':
    # print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))
    pass
