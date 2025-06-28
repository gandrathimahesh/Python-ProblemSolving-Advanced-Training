
 # Todays Topic: Advanced Sorting: Merge Sort (with Inversion Counter) and Quick Sort


#sorting of 2 sorted list

'''a=[2,4,5,8,9]
b=[3,5,6,9,11,12,13]
v=a+b
print(sorted(v))'''

'''
a=[2,4,5,8,9]
b=[3,5,6,9,11,12,13]
for i in range(len(b)):
    a.append(b[i])
for j in range(len(a)):
    flag=False
    for k in range(len(a)-1-j):
        if a[k]>a[k+1]:
            a[k],a[k+1]=a[k+1],a[k]
            flag=True
    if (flag==False):
        break
print(a)
'''
# with O(n+m) time complexity
'''
a = [2, 4, 5, 8, 9]
b = [3, 5, 6, 9, 11, 12, 13]
i = 0
j = 0
c = []
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
# Append remaining elements
c.extend(a[i:])
c.extend(b[j:])
print(c)'''

 # Merge sort algorithm

'''def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)'''


#[2,13,4,2,9,9,5,8,7,13,3]
# k=3
#output:8
'''a=[2,13,4,2,9,9,5,8,7,13,3]
k=3
v=set(a)
x=sorted(v)
print(x[-k])'''


#output=7 3rd highest no.
'''
a = [3, 3, 13, 8, 5, 4, 7, 13, 8, 2, 7]
k = 3  
b = [0] * (max(a) + 1)
for i in a:
    b[i] = 1
for i in range(len(b)-1, -1, -1):
    if b[i] == 1:
        k -= 1
        if k == 0:
            print(i)
            break'''

# dont ignore duplicates count them and print k th largest no.

'''a= [3, 3, 13, 8, 5, 4, 7, 13, 8, 2, 7]
k = 3
freq = [0] * (max(a) + 1)
for num in a:
    freq[num] += 1
for i in range(len(freq) - 1, -1, -1):
    while freq[i] > 0:
        freq[i] -= 1
        k -= 1
        if k == 0:
            print(i)
            break
    if k == 0:
        break'''


#highest frequency

'''a = [3, 3, 1, 2, 1, 1, 22]
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
max_freq = max(d.values())
# Find the key(s) with the highest frequency
for key, value in d.items():
    if value == max_freq:
        print(key)
        break  # print only one key with highest frequency
'''


'''a = [3, 3, 1, 2, 1, 1, 22]
d = {}
k = 3
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
# Now print all keys with frequency equal to k
for key, value in d.items():
    if value == k:
        print(key)

'''

# print key greater than threshold value

# a = [2,1,1,2,3,1]
# d = {}
# m = len(a)/2
# f=0
# for i in a:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# for key, value in d.items():  
#     if value > m:
#         f=1
# if f==1:
#     print(value)
# else:
#     print('-1')


  # moores algorithm

'''a=[2,1,3,1,1,1,3]
c=1
res=a[0]
for i in range(1,len(a)):
    if res==a[i]:
        c+=1
    else:
        c-=1
        if c==0:
            res=a[i]
            c=1
print(res)
'''
# search a number linearlly and print max index of it

'''a=[2,4,3,1,4,2,3,4,5]
t=2
l=[]
for i in range(len(a)):
    if t==a[i]:
        l.append(i)
print(max(l))
'''

# Binary search

'''a=[1,2,2,2,3,4,5]
l=0
t=2
r=len(a)-1
while l<=r:
    mid=(l+r)//2
    if a[mid]==t:
        l1.append(mid)
    elif t<a[mid]:
        r=mid-1
    else:
        l=mid+1
print(max(l1))'''


'''
# last occurance index of target

a = [1, 2, 2, 2, 2, 3, 4, 5]
t = 2
l = 0
r = len(a) - 1
res = -1  # Initialize with -1 to indicate "not found"

while l <= r:
    mid = (l + r) // 2
    if a[mid] == t:
        res = mid
        l = mid + 1  # Keep searching to the right
    elif t < a[mid]:
        r = mid - 1
    else:
        l = mid + 1

print(res)  # Output: 4

'''
# a=int(input("how many telugu marks"))
# b=int(input("how marks hindi marks"))
# c=int(input("how many maths marks" ))
# d=int(input("how many pyhsics marks"))
# e=(a+b+c+d)
# print(e)
# print(e//4)
# # a=int(input("bunny"))
# # if a==5:
# #     print("yes")
# else:
#     print("no")
# a=int(input())
# if a<10:
#     print("less")
# else:
#     print("more")
# 
# a=int(input())
# b=int(input())
# print(a+b)
# a=20
# b=50
# if a<b:
#     print(a)
# else:
#     print(b)
# a=80
# b=100
# if a<=b: 
#     print(a)
# else: 
#     print(b)
# a=50
# b=60
# if a>=b:
#     print(b)
# else:
#     print(a)
# a=int(input())
# b=int(input())
# print(a+b)


# a=int(input("enter your age:"))
# if a>=25:
#     print("greater")
# else:
#     print("lesser")
# a=int(input("enter your marks"))
# if a>20:
#     print("lesser")
# else:
#     print("greater")





# arr=[[1,2,3],[4,5,6],[7,8,9],[10,11,]]
# for i in range(len(arr)):
#     if i%2!=0:
#         print(arr[i][::-1])
#     else:
#         print(arr[i])

# arr=[[1,-1,-5],[7,5,4],[8,1,2]]
# m=99999
# for i in arr:
#     v=min(i)
#     m=min(m,v)
# print(m)
# x=22+28
# y=22-8/2
# print(x-y)

# a=52
# b=50
# if a>=b:
#     print(a)
# else:
#     print(b)

# a=52+20
# b=22-25/6
# print(a-b)
# a=int(input("how many telugu marks"))
# b=int(input("how mny hindi marks"))
# c=int(input("how many maths marks"))
# d=(a+b+c)
# print(d)
# print(d//3)

# a=int(input("enter your age"))
# if a<=20:
#     print("lesser")
# else:
#     print("gearter")

# list=(1,2,3,4)
# if 'in list':
#     print('present')
# else:
#     print('absent')

# list=()
# if 'in list':
#     print('present')
# else:
#     print('absent')

# list=["oniy even number"]
# if 'in list':
#     print('even')
# else:
#     print('odd')

# list1=[1,2,3,4]
# print(list1)
# list2=['python','java','c']
# print(list2)
# list3=[True,False,5,5,0]
# print(list3)

# list=[1,2,3,4]
# list2=['a','b','c']
# list.extend(list2)
# print(list)

# list=[1,2,3,4] 
# list2=['f','g','h','i']  
# list.extend(list2) 
# print(list)  

# list=[1,2,3,4]
# list.remove(3)
# print(list)

# list=[1,2,3,4,5,6,7,8,]
# list.remove(4)
# print(list)

# list=[1,2,3,4,5]
# list.pop(0)
# print(list)
# list=[1,2,3,4,5]
# list.pop(3)
# print(list)

# s="aaabbccde"
# d={}
# l=[]
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for k,v in d.items():
#     l.append(k)
#     l.append(str(v))
# print(''.join(l))

# s="{{()}}"
# d={ '}' :'{' ,')':'('}
# stack=[]
# for i in range(len(s)):
#     if s[i]=='{' or s[i]=='(':
#         stack.append(s[i])
#     else:
#         if stack[-1]==d[s[i]] or not stack:
#             print("False")
# print("True")

# s="{{()}}"
# s=s.replace('()','') or s.replace('{}','')
# if s=='':
#     print("Valid")
# else:
#     print("invalid")

# arr=[1,4,3,2]
# l=[]
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         l.append(arr[i:j+1])
# print(l)

# arr=[1,3,4,2]
# for 

# arr=[1,5,10]
# r=len(arr)+1
# dp=[1]*(r+1)
# for i in range(1,r):
#     dp[i]=dp[i-1]*(r-i)//i
#     if arr==dp:
#         print('-1')
# print(dp[len(arr)-1])


