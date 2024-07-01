import math
from typing import List
import sys
sys.setrecursionlimit(10**6)

# def alice_and_books():
#     n= int(input())
#     pages = list(map(int,input().split()))
#     print(pages[-1] + max(pages[:n-1]))
#
# for _ in range(int(input())):alice_and_books()
# fs
from collections import Counter
from collections import deque

# def tiredness():
#     n = int(input().strip())
#     m = int(input().strip())
#     mid = (n+m)//2;
#     def f(start,end):
#         dist = abs(start - end)
#         return (dist*(dist+1)//2)
#
#     ans = f(n,mid) + f(m,mid)
#     print(ans)
#
# tiredness()

# def f():
#     n = int(input())
#     s = input()
#     for i in range(n - 1):
#         if s[i] > s[i + 1]:
#             return "YES\n{} {}".format(i + 1, i + 2)
#
#     return "NO"
#
# print(f())

# BOGOSORT
def make_good_array(arr):
    arr.sort()
    print(" ".join(map(str, arr)))


n = int(input())
arr = list(map(int, input().split()))
make_good_array(arr)




def process_test_cases():
    t = int(input().strip())
    results = []
    for _ in range(t):
        a = input().strip()
        b = input().strip()
        result = min_length_substring_subsequence(a, b)
        results.append(result)

    for res in results:
        print(res)


# Example usage
# process_test_cases()


# def f():
#     n = int(input())
#     for i in range(n):
#         x,y = map(int,input().split())
#         print('YES' if y>=-1 else "NO")
# f()
def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]

    for i in range(0, n // 2, 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]

    for i in range(n):
        print(a[i], end=" ")
    print()


# main()
def max_final_value(a):
    c = 0
    for ai in a:
        if c + ai >= 0:
            c = c + ai
        else:
            c = -(c + ai)
    return c
# for _ in range(int(input())): max_final_value(int(input()))
# def check_hello(s):
#     target = "hello"
#     target_index = 0
#
#     for char in s:
#         if char == target[target_index]:
#             target_index += 1
#         if target_index == len(target):
#             print("YES")
#             return
#
#     print("NO")
#
# check_hello(input())
def even_odd():
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))

    even_count = 0
    odd_count = 0
    mass = []

    for i in range(n - 1):
        if arr[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if even_count == odd_count:
            mass.append(abs(arr[i] - arr[i + 1]))

    mass.sort()
    ans = 0

    for diff in mass:
        if diff <= b:
            b -= diff
            ans += 1
        else:
            break

    print(ans)


# even_odd()


# n = int(input().strip())
#
# k = 1
# while k * (k + 1) // 2 <= n:
#     k += 1
# k -= 1
# candies = []
# total = 0
# for i in range(1, k):
#     candies.append(i)
#     total += i
# candies.append(n - total)
# print(k)
# print(" ".join(map(str, candies)))

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


def kth_perfect_number(k):
    num = 19
    count = 0

    while count < k:
        if sum_of_digits(num) == 10:
            count += 1
            if count == k:
                return num
        num+=9

    return num
# n = int(input().strip())
# print(kth_perfect_number(n))


# def kefa_and_first_steps():
#     n = int(input())
#     arr = list(map(int,input().split()))
#     c, maxi = 1, 1
#     for i in range(n-1):
#         if(arr[i]<=arr[i+1]):
#             c+=1
#             maxi = max(c,maxi)
#         else:
#             c = 1
#     print(maxi)
#
# kefa_and_first_steps()
def update_queries():
    a = list(map(int, input().split()))
    b = list(input())
    c = list(map(int, input().split()))
    d = list(input())
    d.sort()
    c.sort()
    d_pointer = 0

    for i in range(a[1]):
        if i < a[1] - 1:
            if c[i + 1] == c[i]:
                continue
        b[c[i] - 1] = d[d_pointer]
        d_pointer += 1
    print(''.join(b))


# for _ in range(int(input())):update_queries()
"""max swaps in bubble sort n(n-1)/2 so even if one ele is sorted then less than n(n-1)/2 swaps needed"""
def cubes_count():
    n = int(input());
    arr = list(map(int,input().split()))
    for i in range(1,n):
        if(arr[i]>=arr[i-1]):
            print('YES')
            return

    print('NO')
# for _ in range(int(input())):cubes_count()
def forbidden_subsequence():
    S = input()
    T = input()
    counts = Counter(S)
    if T != 'abc':
        print(str(sorted(S)))
    elif 'a' not in S or 'b' not in S or 'c' not in S:
        print(str(sorted(S)))
    else:
        output = ''.join([
        'a' * counts['a'],'c' * counts['c'],'b' * counts['b'],''.join([char * counts[char] for char in sorted(counts.keys()) if char not in 'abc'])])
        print("".join(output),type(output))

# for _ in range(int(input())):forbidden_subsequence()

# def gcd_problem():
#     n= int(input());
#     if (n&1)==0:
#         print(f'{n-3} 2 1')
#     else:
#         print(f'{(n-1)//2 + 1} {(n-1)//2 - 1} 1' if ((n-1)//2)&1==0 else f'{(n-1)//2 + 2} {(n-1)//2 - 2} 1')
#
# for _ in range(int(input())):gcd_problem()
# def bakery():
#     n,a,b=map(int,input().split())
#     if b <= a:
#         max_profit = n * a
#     else:
#         max_profit = n * a
#         cnt = min(n, b - a)
#         max_profit -= cnt * a
#         max_profit += cnt * (b + b - cnt + 1) // 2
#     print(max_profit)
# for _ in range(int(input())):bakery()

#for n to be the power of 2
"""i % n == i & (n-1) Very imp """
# def f():
#     pattern = [[0, 1, 1, 0], [1, 0, 0, 1],[1, 0, 0, 1],[0, 1, 1, 0]]
#     n,m = map(int,input().split())
#     for i in range(n):
#         for j in range(m):
#             print(pattern[i&3][j&3],end=" ")
#         print()
# for _ in range(int(input())):f()
print(list(reversed([[1, 0, 0, 1],[0, 1, 1, 0]])))

def solve():
    n,m = map(int,input().split())
    grid = []
    maxi = {'r':0,'c':0}
    col = {'f':0,'l':0}
    for i in range(0,n):
        row = input().strip()
        count = row.count('#')
        if count>maxi['c']:
            maxi['c'] = count
            maxi['r'] = i
            col['f'] = row.find('#')
            col['l'] = row.rfind('#')
        grid.append(row)

    rows = maxi['r']+1
    cols = ((col['l']+col['f'])//2) + 1
    print(f'{rows} {cols}')
# T = int(input())
# for _ in range(T):
#     solve()






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


# def solve():
#
#     n, a, b, c = map(int, input().split())
#     m = [0]*(n+1)
#     m[0] = 0
#     for i in range(1,n+1):
#         maximum = max((m[i - a] + 1) if i - a >= 0 else -float('inf'),
#                       (m[i - b] + 1) if i - b >= 0 else -float('inf'),
#                       (m[i - c] + 1) if i - c >= 0 else -float('inf'))
#         m[i] = maximum
#
#     print(m[n])
#
# solve()
# for _ in range(int(input())): a, b = input().split(); print(f'{b[0] + a[1:]} {a[0] + b[1:]}')

#
def count_good_prefixes(a):
    n = len(a)
    prefix_sum = 0
    good_prefix_count = 0

    for i in range(n):
        prefix_sum += a[i]
        # Check if there exists an element a[j] such that a[j] = prefix_sum - a[j]
        for j in range(i + 1):
            if a[j] == prefix_sum - a[j]:
                good_prefix_count += 1
                break  # We only need one such element to determine if the prefix is good

    return good_prefix_count

print(count_good_prefixes([1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 294967296]))
""" https://codeforces.com/contest/1985/problem/B Using most controversial Walrus operator := """
# print(*[n if (n:=int(input())) <= 3 else 2 for _ in range(int(input()))], sep='\n')

"""decimal to binary"""
"""110001
1100100"""
# print(int('1100101',2) - int('101000',2))
# print(bin(41)[2:])
# print(bin(100)[2:])

"""Bitwise"""
"""Mocha math"""

# def solve():
#     n = int(input())
#     arr = list(map(int,input().split()))
#     rslt = arr[0]
#     for num in range(1,n):
#         rslt&=arr[num]
#     print(rslt)
#
# T = int(input())
# for _ in range(T):
#     solve()

"""E Secret box"""
# def solve():
#     x,y,z,k = map(int,input().split())
#     ans = 0
#     for i in range(1,x+1):
#         for j in range(1,y+1):
#             if k%(i*j)==0 and (p:=k//(i*j)) <= z: ans = max(ans,(x-i+1)*(y-j+1)*(z-p+1))
#     print(ans)
#
#
# for _ in range(int(input())):
#     solve()


# def solve():
#     n = int(input())
#     line = input().strip()
#     numbers = list(map(int, line.split()))
#     print(numbers[0])
# T = int(input())
# for _ in range(T):
#     solve()

















