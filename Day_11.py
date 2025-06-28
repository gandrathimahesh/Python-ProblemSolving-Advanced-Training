#maximum no of meetings

'''arr1=[0,3,8,1,5,7,9]
arr2=[8,6,10,2,6,9,11]
l=list(zip(arr1,arr2))
l.sort(key=lambda x: x[1])
st=0
c=0
for i in l:
    if(i[0]>=st):
        c=c+1
        st=i[1]+1
print(c)
'''

#just reversing the string without changing the vowels place


# 


#max sum of window

'''a = [2, 1, 6, 4, 2, 3, 1, 1, 4, 2, 6, 7, 3]
k = 5
sum = 0
l = 0
m = 0
for i in range(k):
    sum += a[i]
for r in range(k, len(a)):
    sum = sum - a[l] + a[r]  
    l += 1                   
    m = max(sum, m)
print(m)

'''
#printing all sunarrays


'''def fun(x,s=[],i=0):
    if i==len(a):
        print(s)
        return
    fun(x,s+[a[i]],i+1)
    fun(x,s,i+1)
a=[2,1,3,4]
l=[]
print(fun(a))'''


#length of longest subarray with in the range of K

'''a = [1, 2, 3, 4, 5, 6]
k = 6
l = 0
sum = 0
m = 0
for r in range(len(a)):
    sum = sum + a[r]
    while sum > k:           #  use while instead of if
        sum = sum - a[l]
        l += 1
    if sum <= k:             #  optional: ensures we're within the desired range
        m = max(m, r - l + 1)
print(m)
'''
    

#length of the longest palindrome 

'''a = "ababba"
l = 0
m = 0
for i in range(len(a)):
    # Odd-length palindrome
    l = i
    r = i
    while l >= 0 and r < len(a) and a[l] == a[r]:
        m = max(m, r - l + 1)
        l -= 1
        r += 1
    # Even-length palindrome
    l = i
    r = i + 1
    while l >= 0 and r < len(a) and a[l] == a[r]: 
        m = max(m, r - l + 1)
        l -= 1
        r += 1

print(m)'''

#length of longest palindrome
'''
a = "ababba"
l = 0
m = 0
st=0
for i in range(len(a)):
    # Odd-length palindrome
    l = i
    r = i
    while l >= 0 and r < len(a) and a[l] == a[r]:
        if (r-l+1)>m:
            m=r-l+1
            st=l
        l -= 1
        r += 1
    # Even-length palindrome
    l = i
    r = i + 1
    while l >= 0 and r < len(a) and a[l] == a[r]: 
        if (r-l+1)>m:
            m=r-l+1
            st=l
        l -= 1
        r += 1      
print(a[st:st+m])'''


#no.of palindromes count

'''a = "ababba"
l = 0
m = 0
c=0
for i in range(len(a)):
    # Odd-length palindrome
    l = i
    r = i
    while l >= 0 and r < len(a) and a[l] == a[r]:
        c+=1
        l -= 1
        r += 1
    # Even-length palindrome
    l = i
    r = i + 1
    while l >= 0 and r < len(a) and a[l] == a[r]: 
        c+=1
        l -= 1
        r += 1      
print(c)'''



# a=10
# b=20
# c=a+b
# print(c)
# a=20
# b=30
# c=a+b
# print(c)

# a=20
# b=10
# if a>b:
#     print(b)
# else:
#     print(a)

# a=int(input())
# b=int(input())
# print(a+b)


# a=10
# b=20
# c=30
# print(a+b+c)

# a=int(input("enter your age::"))
# if a>=18:
#a=int(input("enter telugu marks==>"))
# b=int(input("enter hindi marks==>"))
# c=int(input("enter maths marks==>"))
# d=int(input("enter physics marks==>"))
# e=a+b+c+d
# f=(e//4)
# print(e)
# print(f)
