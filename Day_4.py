#Medium Recursion

'''In this code functional recursion'''

# def find(a,t,i=0):
#     if i==len(a):
#         return 0
#     if a[i]==t:
#         return 1+find(a,t,i+1)
#     else:
#         return find(a,t,i+1)
# a=list(map(int,input().split()))
# t=int(input())
# print(find(a,t))

'''This code is with parameterized passing'''

# def find(a,i,c,t):
#     if i==len(a):
#         return c
#     if a[i]==t:
#         c+=1
#         return find(a,i+1,c,t)
#     return find(a,i+1,c,t)
# a=list(map(int,input().split()))
# t=int(input())
# print(find(a,0,0,t))

'''def find(a, t, i=0, d={}):
    if i == len(a):
        print(d[a[t]])
        return
    if a[i] in d:
        d[a[i]] += 1
    else:
        d[a[i]] = 1
    return find(a, t, i + 1, d)
a = list(map(int, input().split()))
t = int(input())
find(a,t)

'''


'''def find(a, x, i=0):
    if i == len(a):
        return 0
    if a[i] == x:
        return 1 + find(a, x, i + 1)
    return find(a, x, i + 1)
def iterate(x, f, i=0):
    if i == len(x):
        return
    if (find(x, x[i]) == f):
        return x[i]
    return iterate(x, f, i + 1)
a = list(map(int, input().split()))
t = int(input())
print(find(a,a[t]))
'''

'''def value(x, f, d, i=0):
    if i == len(x):
        return "Not found"
    if d[x[i]] == f:
        return x[i]
    return value(x, f, d, i + 1)
def freq_d(x, f, d={}, i=0):
    if i == len(x):
        return value(x, f, d)
    if x[i] not in d:
        d[x[i]] = 1
    else:
        d[x[i]] += 1
    return freq_d(x, f, d, i + 1)
a = list(map(int, input().split()))
t = int(input())
print(freq_d(a,t))
'''
# printing subsets of a given array

# def subset(x,s=[],i=0):
#     if i==len(a):
#         print(s)
#         return
#     subset(x,s+[a[i]],i+1)
#     subset(x,s,i+1)
# a=[1,2,3]
# print(subset(a))


'''def sub_set(x, k, i=0):
    if k == 0:
        return True
    if i == len(x) or k < 0:
        return False
    return sub_set(x, k, i + 1) or sub_set(x, k - x[i], i + 1)
a = [1, 2, 3]
k = 5
print(sub_set(a, k))

'''


'''def sub_set(x,k,i):
    if k==0:
        return True
    if i==0:
        return False
    if (x[i-1]>k):
        return sub_set(x,k,i-1)
    return sub_set(x, k-x[i], i-1) or sub_set(x,k,i-1)
'''


# def subset(x, k, s=[], i=0):
#     if i == len(x):
#         if k == 0:
#             print(s)
#         return
#     if x[i] <= k:
#         subset(x, k-x[i], s+[x[i]], i+1)
#     subset(x, k, s, i+1)

# a = [2, 3, 4, 5]
# k = 9
# subset(a, k)


# def subset(x, k, s=0, i=0):
#     global min_size
#     if i == len(x):
#         if k == 0:
#             min_size = min(min_size, s)
#         return
#     if x[i] <= k:
#         subset(x, k-x[i], s+1, i+1)
#     subset(x, k, s, i+1)

# a = [2, 3, 4, 5]
# k = 9
# min_size = float('inf')
# subset(a, k)
# print(min_size)

#GREEDY ALGORITHM
'''
a = [4, 5, 6, 2, 13, 7, 8]
l = []
for i in range(len(a)):
    if i % 2 == 0:
        l.append(a[i])
print(max(l))
'''


'''a = [4, 5, 6, 2, 13, 7, 8]
m=0
m1=999999999
for i in a:
    if(i>m and i%2==0):
        m=i
    if (i<m1 and i%2!=0):
        m1=i
print(m,m1)
'''


# a = [4, 5, 6, 2, 13, 7, 8]
# m = 0
# s = 0
# for i in a:
#     if i > m:
#         s = m
#         m = i
#     elif i > s and i != m:
#         s = i
# print("Maximum:", m)
# print("Second largest:", s)

# n=int(input())
# for i in range(n):
#     print("\n")
#     for j in range(n-i):
#         print("*",end=' ')
        

# a = [4, 5, 6, 12, 2, 13, 7, 8]
# a.sort()
# sec_max=0
# max_num=0
# for i in a:
#     if i>max_num:
#         sec_max=max_num
#         max_num=i
# print(sec_max)

