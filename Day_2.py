'''arr = [2, 3, 4, 5, 6, 7, 8]
target = 10
left = 0
right = len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        print(mid)  
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(-1)'''



#Bit wise operators

""" n=int(input())
if n^(n-1)==1:
    print("odd")
else:
    print("even") """

#sum of n natural numbers

'''n=int(input())
v=(n * (n + 1)) >> 1
print(v)'''


#xor 

'''n=int(input())
if n%4==0:
    print(n)
elif n%4==1:
    print(1)
elif n%4==2:
    print(n+1)
else:
    print(0)'''
'''



n=int(input())
m=int(input()) 
if m%4==0:
    x=n
elif m%4==1:
    x=1
elif m%4==2:
    x=n+1
else:
   x=0
if n%4==0:
    x1=n
elif n%4==1:
    x1=1
elif n%4==2:
    x1=n+1
else:
   x=0
print(x1^x)
'''

'''n=int(input())
if n>0 and n&(n-1)==0:
    print("yes")
else:
    print("no")'''


'''n=int(input())
v=print(bin(n).count("1"))'''



# arr=[2,2,4,4,6,6,7,8,8,9,9]
# for i in range(0,len(arr)-1 ,2):
#     if arr[i]!=arr[i+1]:
#         print(arr[i])
#         break
# else:
#     print(arr[-1])


'''arr = list(map(int, input().split()))
max_len = 1
curr_len = 1
for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        curr_len += 1      
    else:
        curr_len = 1
print(max(max_len, curr_len))
 '''



'''arr=list(map(int,input().split()))
c=1
l=[]
for i in range(len(arr)-1):
    if arr[i]+1==arr[i+1]:
        c+=1
    else:
        l.append(c)
        c=1
l.append(c)
print(l)
'''

'''s = input()
res = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        res += s[i - 1] + str(count)
        count = 1
res += s[-1] + str(count)
print(res)
 '''


'''a=input()
c=1
s=''
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        c+=1
        
    else:
        s=s+a[i]+str(c)
        c=1
s=s+a[-1]+str(c)
print(s)'''






# arr=[0,2,3,0,5]
# left=0
# for right in range(len(arr)):
#     if arr[right]!=0:
#         arr[left],arr[right]=arr[right],arr[left]
#         left+=1
# print(arr)
