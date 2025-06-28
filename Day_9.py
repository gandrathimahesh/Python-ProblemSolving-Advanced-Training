#Searching a Target in a 2D matrix

""" arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
t=8
for i in range(len(arr)):
    f=0
    for j in range(len(arr)):
        if arr[i][j]==t:
            print("Row",i,"Coloum",j)
            f=1
            break
    if f==1:
        break
else:
    print("Not found")
 """

#using other logic with best O()

# Target value to search
""" Target = 10
# Binary search on a single row
def bin(x):
    l = 0
    r = len(x) - 1
    while l <= r:
        mid = (l + r) // 2
        if x[mid] == Target:
            return True
        elif x[mid] < Target:
            l = mid + 1
        else:
            r = mid - 1
    return False
# Matrix search using binary search row by row
def matrix_search(arr):
    for row in arr:
        if row[0] <= Target <= row[-1]:
            if bin(row):
                return True
    return False
# 2D matrix input
arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
# Call the function and print result
result = matrix_search(arr)
print(result)  # Output: True if found, False if not

 """

#using O(log(m+n))

""" a = [
    [2, 5, 8, 10],
    [13, 15, 17, 22],
    [23, 26, 30, 33]
]
m = len(a)       # rows = 3
n = len(a[0])    # cols = 4
x = 17
l = 0
r = (m * n) - 1
while l <= r:
    mid = (l + r) // 2

    #rows and colums
    row = mid // n
    col = mid % n

    if a[row][col] == x:
        print("Found")
        break
    elif x < a[row][col]:
        r = mid - 1
    else:
        l = mid + 1
else:
    print("Not found")
 """"""  """

#leetcode 1011

'''weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = 7
left = max(weights)         # Minimum possible capacity
right = sum(weights)        # Maximum possible capacity
while left < right:
    mid = (left + right) // 2   # Try this capacity
    days = 1
    total = 0
    # Check how many days needed with this capacity
    for w in weights:
        if total + w > mid:
            days += 1
            total = 0
        total += w
    if days <= D:
        right = mid   # Try smaller capacity
    else:
        left = mid + 1  # Need more capacity
print(left)  # Minimum capacity to ship within D days
'''

#finding element in which row and col is in ascending order
#with functions

'''def search_matrix(a, t):
    n = len(a)
    i=0
    j=n-1   # start from top-right
    while i < n and j >= 0:
        if a[i][j] == t:
            print("Found")
            return
        elif a[i][j] > t:
            j -= 1  # move left
        else:
            i += 1  # move down
    print("Not Found")
# Example
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
t = 5
search_matrix(a, t)'''

# without functions
'''
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
t=10
i=0
j=len(a)-1
f=0
while i<len(a) and j>=0:
    if a[i][j]==t:
        print("Found")
        f=1
        break
    elif a[i][j]>t:
        j-=1
    else:
        i+=1
if f==0:
    print("not found")

'''



'''2sum'''
# a=[2,7,11,15]
# target=22
# j=len(a)-1
# i=0
# while i<=j:
#     if a[i]+a[j]==target:
#         print(a[i],a[j])
#         break
#     elif a[i]+a[j]>target:
#         j-=1
#     else:
#         i+=1

