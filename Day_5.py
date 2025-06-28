'''arr = list(map(int, input().split()))
min_price = arr[0]
max_profit = 0
for price in arr:
    if price < min_price:
        min_price = price
    profit = price - min_price
    if profit > max_profit:
        max_profit = profit
print(max_profit)
    
'''


'''a = [4, 5, 6, 2, 3, 14, 5, 6, 4]
b = 99999  # min_price
pr = 0     # max_profit
for i in a:
    if i < b:
        b = i  # update min price
    else:
        if i - b > pr:
            pr = i - b  # update max profit
print(pr)

'''
'''n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
b=list(map(int,input().split()))
for i in range(n):
    s=0
    for j in range(n):
        if (arr[i][j]==1):
            s+=b[j]
    print(s)'''


'''
def rat(a, i, j, n):
    if i == n or j == n or a[i][j] == 0:     
        return 0
    if i == n-1 and j == n-1 and a[i][j] == 1:   
        return 1
    return rat(a, i, j + 1, n) + rat(a, i + 1, j, n)
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
print(rat(arr, 0, 0, n))'''


'''def land(a, i, j, n):
    if(i == n or j == n or i < 0 or j < 0 or a[i][j] == 0 or a[i][j] == 2):
        return 
    if (a[i][j] == 1):
        a[i][j] = 2  # Fixed: changed '==' to '=' to mark visited
    land(a, i - 1, j, n)
    land(a, i, j - 1, n)
    land(a, i + 1, j, n)
    land(a, i, j + 1, n)
n = 3
a = [[1, 0, 1], [1, 1, 0], [1, 0, 0]]
c = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            land(a, i, j, n)
            c += 1
print(c)
'''


'''def fire(a, i, j, n):
    if(i == n or j == n or i < 0 or j < 0 or a[i][j] == 0 or a[i][j] == 2):
        return 
    if (a[i][j] == 1):
        a[i][j] = 2 
    fire(a, i - 1, j, n)
    fire(a, i, j - 1, n)
    fire(a, i + 1, j, n)
    fire(a, i, j + 1, n)
n = 3
c=0 
a = [[1, 0, 1], [1, 1, 0], [1, 0, 0]]
fire(a, 0, 0, n)
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            c+=1  
print(c)

'''

#frong jump question

'''def frog(n, i, j, hud):
    if (i == n or j == n or (i, j) in hud):
        return 0
    if i == n - 1 and j == n - 1:
        return 1
    return frog(n, i + 1, j, hud) + frog(n, i, j + 1, hud)

# Grid size
n = 3

# Blocked positions (hud = hurdles), given as a set of (row, column) tuples
hud = {(1, 1)}  # example: cell (1,1) is blocked

# Starting point is (0, 0)
paths = frog(n, 0, 0, hud)

print("Number of paths:", paths)

'''

'''n = int(input())  # Take input from user
for i in range(1, n):  # Loop from 1 to n-1
    v = bin(i)[2:].zfill(n)  # Convert to binary, remove '0b', pad with leading zeros to length n
    print(v)'''


#binary upto n

'''
def allbinary(a, n, s=''):
    if a == -1:  # If no more strings needed, stop recursion
        return a
    
    if len(s) == n:  # If string length reached n, print and decrease count
        print(s)
        a -= 1
        return a
    
    a = allbinary(a, n, s + '0')  # Recurse adding '0'
    a = allbinary(a, n, s + '1')  # Recurse adding '1'
       
    return a

# Example usage:
n = 3  # length of binary strings
total = 2**n  # total binary strings of length n
allbinary(total, n)
'''


i=1
while i<=10:
    print(i)
    i+=1