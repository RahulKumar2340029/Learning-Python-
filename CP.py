from typing import List
import sys
sys.setrecursionlimit(10**6)

def mydecorator(function):

    def wrapper():
        print("Hello I am decorating")
        function()

    return wrapper

# method 1
# def hello_world():
#     print("Hello world!")
#
# mydecorator(hello_world)()

# method 2
@mydecorator
def hello_world():
    print("Hello world")

hello_world()

# function
# def solve():
#     n = int(input())
#     input_arr = input()
#     arr = [int(x) for x in input_arr.split()]
#     if len(arr)<3:
#         print('NO')
#     a = arr[0]
#     b = arr[1]
#     c = arr[2]
#     d = arr[n-1]
#
#     if a == d:
#         print("NO")
#         return
#     print("YES")
#     char_list = ['R']
#     for i in range(1, n):
#         char_list.append('B')
#     result = "".join(char_list)
#     print(result)


def numSteps(s: str) -> int:
    v = int(s,2)
    count = 0
    while v>1:
        if (v&1)==1:
            v+=1
        else:
            v//=2
        count+=1
    return count


# def solve(n):
#
#     sum = n
#     while n != 1:
#         sum+=(n//2)
#         n=n//2
#     print(sum)
# t = int(input())
# for i in range(0,t):
#     n = int(input())
#     solve(n)
# print(numSteps("1111011110000011100000110001011011110010111001010111110001"))
# solve()
# t = int(input())
# for i in range(0,t):
#     solve()

# missing coin sum queries vivek gupta
prefix = [0]
# def solve(arr:List[int])->int:
#     arr.sort()
#     count = 1
#     for i in range(1,len(arr)):
#
#         ele = arr[i-1]
#         prefix.append(ele)
#         for j in range(0,len(prefix)):
#             prefix.append(ele + prefix[j])
#
#     prefix.sort()
#     for i in range(1,max(prefix)):
#         if i not in prefix:
#             print(i)
#             return

# solve([2 ,9, 1, 2, 7])
# print(prefix)

# codeforces global round 26B
"""case1: last digit must be 1
case2 first digit must be bw 0 to 8
rest all no from ind 1 to n-2 must be non zero because in
smallest case also there must be one carry so become 0 at any index
5+5 must be there which includes 1 as carry so 5+4 and again 4 is not a large no"""


# def check_number():
#     n = input()
#
#     if n[0] != '1' or n[-1] == '9':
#         print('NO')
#         return
#
#     if '0' not in n[1:-1]:
#         print('YES')
#     else:
#         print('NO')
#
#
#
# T = int(input())
# for _ in range(T):
#     check_number()

# def solve(s):
#     print('YES' if any(c in s for c in 'HQ9') else 'NO')
#
# s = (input())
# solve(s)

# --------------------------------------------------------------------------------------------------------------------#
# cut ribbons codeforces
def f(length,a,b,c):
    if length==0:
        return 0
    if length < 0:
        return -float('inf')
    maximum = max(f(length-a,a,b,c),f(length-b,a,b,c),f(length-c,a,b,c)) + 1
    return maximum


def solve():

    n, a, b, c = map(int, input().split())
    m = [0]*(n+1)
    m[0] = 0
    for i in range(1,n+1):
        maximum = max((m[i - a] + 1) if i - a >= 0 else -float('inf'),
                      (m[i - b] + 1) if i - b >= 0 else -float('inf'),
                      (m[i - c] + 1) if i - c >= 0 else -float('inf'))
        m[i] = maximum

    print(m[n])

solve()









