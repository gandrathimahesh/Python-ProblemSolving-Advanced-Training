#prime number
'''n=int(input())
c=1
for i in range(2,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("Prime")
else:
    print("Not prime")
if n>=200:
    print("Greater than 200")
else:
    print('Less than 200')'''


'''import math
n = int(input())
c = 0
# Check for factors up to square root of n
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        if i == n // i:
            c += 1  # Count perfect square only once
        else:
            c += 2  # Count both i and n//i
if c == 2:
    print("Prime")
else:
    print("Not prime")
if n >= 200:
    print("Greater than 200")
else:
    print("Less than 200")'''

#Removing duplicates
'''
l=[8,2,3,4,3,3,4,5,6,7,9,2,4]
v=[]
for i in l:
    if i not in v:
        v.append(i)
print(v) ''' 

#with dictionary
'''
l = [8, 2, 3, 4, 3, 3, 4, 5, 6, 7, 9, 2, 4]
v = list(dict.fromkeys(l))
print(v)
'''

 
'''a=7
a=a-2
b=0
b=b+1+1
b=b-1
c=a^b
print(c)'''


'''n = int(input()) 
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i += 1
print(sum)'''

'''n = int(input())
sum = n * (n + 1) //2
print(sum)
'''

'''lst=[2,6,4,6,7,3,2]
c=0
for i in range(len(lst)):
    if lst[i]%2==0:
        c=c+lst[i]
print(c)'''




'''def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find middle index
        if arr[mid] == target:
            return mid            # Target found
        elif arr[mid] < target:
            low = mid + 1         # Search right half
        else:
            high = mid - 1        # Search left half

    return -1  # Target not found
arr = [1, 3, 5, 7, 9, 11]
target = 7
index = binary_search(arr, target)
print("Index:", index)'''


'''
def merge_sorted_lists(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    # Add remaining elements from a or b
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result
a = [1, 3, 5]
b = [2, 4, 6]
print(merge_sorted_lists(a, b))'''



'''
l=[2,3,4,3,2,5,5]
for i in l:
    if l.count(i) == 1: #check how many times i came in the list
        print(i)
        break  
'''



'''
#Using bit manupulation

def find_unique_element(arr):
    result = 0
    for num in arr:
        result= result ^ num
    return result

# Example usage:
l = [2, 3, 4, 3, 2, 5, 5]
unique = find_unique_element(l)
print(unique)  # Output: 4'''





