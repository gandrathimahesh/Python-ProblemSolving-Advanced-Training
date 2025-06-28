#square root of a number

'''n=int(input())
c=n**0.5
print(int(c))'''


# with O(n)

'''n = int(input())
# Handle edge cases
if n == 0 or n == 1:
    print(n)
else:
    for i in range(1, (n // 2)):  
        if i * i == n:
            print(i)
            break
        elif i * i > n:
            print(i - 1)
            break'''

 
 
# with binary search

'''
n = int(input())
l = 1
r = n
while l <= r:
    m = (l + r) // 2
    if m * m == n:
        print(m)
        break
    elif m * m > n:
        r = m - 1    
    else:
        l = m + 1
else:
    print(r) 
'''

# rotating at n no.of times

'''l = [15, 18, 20, 22, 2, 5, 8, 10, 12, 13]
v = sorted(l)
c = 0
for i in range(len(l)):
    if l == v:
        print(c)
        break
    element = l.pop(0)  
    l.append(element)
    c += 1
else:
    print(-1)  
'''

# How many times rotated

'''n=[10,20,30,40,2,3,4,5,6,7,8,9]
l=0
r=len(n)-1
while(l<=r):
    m=(l+r)//2
    if n[m]>n[r]:
        l=m+1
    else:
        r=m
print(r)'''


# print peak elements O(n)
'''
arr = [2, 3, 4, 6, 3, 2, 1, 5, 8, 10, 1, 4, 2]
for i in range(1, len(arr) - 1): 
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        print(arr[i])'''

 # print peak elements O(log(n))
 #binary search

#  '''it is coming for first peak'''

# a=[2, 3, 4, 6, 3, 2, 1, 5, 8, 10, 1, 4, 2]
# l=0
# r=len(a)-1
# while l<=r:
#     m=(l+r)//2
#     if (a[l]>a[m]):
#         r=m-1
#     else:
#         l=m+1
# print(a[r])
# print(r)


'''a=[]
l=0
r=len(a)-1
while l<r:
    m=(l+r)/2
    if a[m]>a[m-1] and a[m]>a[m+1]:

           '''


#koko eating banana leetcode

'''from math import ceil
h=8
n=[3,6,7,11]
k=4
s=0
for i in n:
    s+=(ceil(i/k))
    if s>h:
        print("not possible")
        break
else:
    print("Possible")'''


""" import math 
a=[30,11,23,4,20]
h=5
k=1
while(1):
    s=0
    for i in a:
        s=s+math.ceil(i/k)
        if s>h:
            k=k+1
            break
    else:
        print(k)
        break """


#koko question using binary Search

""" import math
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            # Compute total hours with current mid as speed
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid)
            # Check if current speed is enough
            if total_hours <= h:
                right = mid  # Try to reduce speed
            else:
                left = mid + 1  # Need higher speed
        return left """

# checking only with first index

""" arr = [1, 2, 5, 7, 10]
t = 11
for i in range(0, len(arr) - 1): 
    if (arr[i+1] - arr[0]) >= t:
        print("possible")
        break
else:
    print("not possible")
 """

#Agressive cows
#all possible ways

a=[1,2,5,7,10,12]
k=1
mini=5
prev=a[0]
k=k-1  # already first cow is placed
for i in a:
    if (i-prev>=mini):
        prev=i
        k=k-1
if k<=0:
    print("p")
else:
    print("np")