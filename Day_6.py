'''arr=list(map(int,input().split()))
for i in range(len(arr)):
    flag=False
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            flag=True
        if (flag==False):
            break
print(arr)
'''


# arr = list(map(int, input().split()))
# k = 4
# n = len(arr)
# for i in range(n):
#     flag = False
#     for j in range(n - 1 - i):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             flag = True
#     k=k-1
#     if flag == False or k==0:
#         break
# print(arr[k-1])

'''arr = list(map(int, input().split()))
k = int(input())
n = len(arr)

first_k = arr[:k]
middle = arr[k:n-k]
last_k = arr[n-k:]

for i in range(len(middle)):
    flag = False
    for j in range(len(middle) - 1 - i):
        if middle[j] > middle[j + 1]:
            middle[j], middle[j + 1] = middle[j + 1], middle[j]
            flag = True
    if not flag:
        break

arr = first_k + middle + last_k
print(arr)
'''
# arr = list(map(str, input().split()))
# for i in range(len(arr)):
#     flag = False
#     for j in range(len(arr) - 1 - i):
#         if ord(arr[j]) > ord(arr[j + 1]):
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             flag = True
#     if flag == False:
#         break   
# print(arr)

'''a=[[2,3],[5,1],[1,3],[7,2]]
for j in range(len(a)-1):
    flag=False
    for i in range(len(a)-1-j):
        if a[i][1]>a[i+1][1]:
            a[i],a[i+1]=a[i+1],a[i]
            flag=True
    if flag ==False:
        break
print(a)
'''

#check or sort words in alphabetical order

'''arr = list(map(str, input().split()))
for i in range(len(arr)):
    flag = False
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            flag = True
    if flag == False:
        break   
print(arr)'''

# arr = [['ba', 'da'], ['ab', 'da'], ['ab', 'ca'], ['ba', 'aa']]
# for i in range(len(arr)-1):
#     for j in range(len(arr)-1-i):
#         if arr[j][0] > arr[j+1][0]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#         elif arr[j][0] == arr[j+1][0]:
#             if arr[j][1] > arr[j+1][1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)




'''arr=[[4,13,12],[8,10,5],[7,9,20],[11,8,3]]
c=0
for i in range(len(arr)-1):

    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
        elif arr[j][3]%2==0:


            c+=1
        if c==2:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
'''
'''
def prime(x):
    for i in x:
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                break
        else:
            return i
a=[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
b=[]
for i in a:
    b.append(prime(i))
for i in range(len(b)-1):
    f=0
    for j in range(len(b)-1-i):
        if(b[j]>b[j+1]):
            b[j],b[j+1]=b[j+1],b[j]
            a[j],a[j+1]=a[j+1],a[j]
            f=1
    if(f==0):
        break
print(a)
'''


'''a = input().split() 
for j in range(len(a)):
    f = False
    for i in range(len(a) - 1 - j):
        if len(a[i]) > len(a[i + 1]):
            a[i], a[i + 1] = a[i + 1], a[i]
            f = True
    if f == False:
        break
print(" ".join(a))
'''


'''a = input().split()  # Taking input as a list of words
b = []
for i in a:
    b.append(len(i))
for i in range(len(b)):
    f = 0
    for j in range(len(b) - 1 - i):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]
            a[j], a[j + 1] = a[j + 1], a[j]
            f = 1
    if f == 0:
        break
print(" ".join(a))  # Printing sorted words in original format
'''


'''
a=[7,2,6,3,6,7,7,2,2,2]
d = {}
for x in a:
    d[x] = d.get(x, 0) + 1
print(d)
for i in range(len(a)-1):
    f=False
    for j in range(len(a)-1-i):
        if d[a[j]]>d[a[j+1]]:
                a[j],a[j+1]=a[j+1],a[j]
                f=True
    if f==False:
            break     
print(a)'''


#same like above code sir explained

a=[3,5,4,4,5,6,7,7,8,8,7,6,4,1,1,2,8,8]
d={}
for i in a:
    if(i not in d):
        d[i]=1
    else:
        d[i]+=1
print(d)
n=max(d.values())
b=[]
for i in range(n+1):
    b.append([])
print(b)
for i in d.items():
    b[i[1]].append(i[0])
print(b)
c=[]
for i in range(len(b)):
    for j in b[i]:
        c.extend([j]*i)
print(c)