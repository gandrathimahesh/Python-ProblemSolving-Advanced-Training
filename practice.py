        
#    1

#   121

#  12321

# 1234321

'''n=int(input())
for i in range(1,n+1):
    print('\n')
    v=1
    for j in range(n-i):
        print(' ',end='')
    for k in range(i):
        print(v,end="")
        v+=1
    for m in range(i-1,0,-1):
        print(m,end ='')
        '''
#    1
#   232
#  34543
# 4567654

'''n = int(input())
for i in range(1, n + 1):
    print('\n', end='')

    # Step 1: Print spaces
    for j in range(n - i):
        print(' ', end='')

    # Step 2: Print increasing numbers
    val = i  
    for k in range(i):
        print(val, end='')
        val += 1

    # Step 3: Print decreasing numbers
    val -= 2  # Go back to the previous number
    for m in range(i - 1):
        print(val, end='')
        val -= 1
'''

#    *
#   ***
#  *****
# ******* 

'''n = int(input())
for i in range(1, n+1):
    print('\n', end='')
    # print spaces
    for j in range(n - i):
        print(' ', end='')
    # print stars: 2*i - 1 stars for ith row
    for k in range(2*i - 1):
        print('*', end='')'''



#   *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

'''n = int(input("Enter the number of rows: "))

# Upward pyramid
for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(' ', end='')
    # Print stars
    for k in range(2 * i - 1):
        print('*', end='')
    print()

# Downward pyramid
for i in range(n - 1, 0, -1):
    # Print spaces
    for j in range(n - i):
        print(' ', end='')
    # Print stars
    for k in range(2 * i - 1):
        print('*', end='')
    print()'''

'''def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input())
r=int(input())
v=n-r
n_fact=fact(n)
r_fact=fact(r)
n_r_fact=fact(v)
ans =((n_fact)//(r_fact*n_r_fact))
print(ans)'''


'''def prime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return True
    return False

def is_prime(n): 
    for k in range(2,n+1):
        primes=prime(k)
        if (primes):
            print(k)
print(is_prime(20))'''







'''arr=[1,2,3,4,8,10,12,18,13]
i=0
j=len(arr)-1
for i in range(len(arr)//2):
    arr[i],arr[j]=arr[j],arr[i]
    j-=1
print(arr)'''

    
# n='hello world'
# c=0
# for i in n:
#     if i=='l':
#         c+=1
# print(c)



'''n="vcdhjcdckegcebnkbhcbjd"
for i in range(len(n)):
    if n[i]== 'a' or 'e' or 'i' or 'o' or 'u':
        '''
""" 
arr=[2,5,1,9,4,3,7]
for i in range(len(arr)):
    mini=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[mini]:
            mini=j
    arr[i],arr[mini]=arr[mini],arr[i]
print(arr) """


# arr=[[1,2,3,4],[5,6,7,30],[5,4,6,2],[2,5,4,1]]
# max=-1
# index=-1
# for j in range(len(arr)):
#     sum=0
#     for i in range(len(arr)):
#         sum=sum+arr[i][j]
#     if sum>max:
#         index=j
#         max=sum
# print(index)
