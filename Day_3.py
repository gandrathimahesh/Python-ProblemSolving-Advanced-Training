
#Recursion

'''def qwer(x):
    if x==4:
        return 200
    print("hi",x)
    qwer(x+1)
    print("hi",x)
qwer(1)
  '''


'''def qwer(x):
    if x==4:
        return 200
    print("hi",x)
    t=qwer(x+1)
    print("hi",x)
    return t+x
b=qwer(1)
print(b)'''
  

  
'''def fact(n):
    if n==1:
        return 1
    return n * fact(n-1) 
b=fact(5)
print(b)
'''

'''def fibo(n):
    if n==1:
        return 1
    if n==2:
        return 1  
    return fibo(n-1)+fibo(n-2)
fibo(8)
print(fibo(8))

'''

'''def even_sum(x,i):
    h=0
    if i==len(x):
        return 0
    if x[i]%2==0:
        h=x[i]
    return h + even_sum(x,i+1)
a=[2,5,6,7,2,12,4,3,6]
print(even_sum(a,0))

'''

'''def even_sum(x,i):
    if i==len(x):
        return 0
    if x[i]%2==0:
        return a[i]+even_sum(x, i+1)
    else:
        return even_sum(x,i+1)
a=[2,5,6,7,2,12,4,3,6]
print(even_sum(a,0))
'''

'''n=153
r=0
while(n!=0):
    b=n%10
    r=r*10+b
    n=n//10
print(r)'''


'''def rev(n, r=0):
    if n == 0:
        return r 
    return rev(n // 10, r * 10 + n % 10)
print(rev(541))'''

'''def prime(x, i, t, c):
    if i == len(x):
        return c
    if x[i] == 2:
        return prime(x, i + 1, 2 ,c+1)
    if x[i] % t==0:
        return prime(x, i + 1, 2,c)
    if t== x[i]//2 + 1:
        return prime(x, i + 1, 2 ,c+1)
    return prime(x,i,t+1,c)
a = [2, 5, 6, 7, 2, 12, 4, 3, 6]
print(prime(a, 0, 2 ,0))'''


# def rec(n):
#     if n==1:
#         return True
#     if n<1:
#         return False
#     return rec(n-3) or rec(n-5)
# n=int(input())
# print(rec(n))


def rec(x,n,m):
    if x==1:
        return True
    if x<1:
        return False
    return rec(x-n,n,m) or rec(x-m,n,m)


x=20
n=3
m=5
print(rec(x,n,m))



