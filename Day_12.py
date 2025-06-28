#length of longest substring without repeating char

'''s="abcdecfbgce"
dic={}
n=len(s)
l=0
r=0
maxlen=0
while r<n:
    if s[r] in dic and dic[s[r]]>=l:
        l=dic[s[r]]+1
    else:
        dic[s[r]]=r
        cur=r-l+1
        maxlen=max(maxlen,cur)
        r+=1            
print(maxlen)'''

# same as above code with having m , n following char in it

'''s = "abcdecfbgce"
dic = {}
length = len(s)
m = 'c'
n = 'd'
l = 0
r = 0
maxlen = 0
start = 0
while r < length:
    if s[r] in dic and dic[s[r]] >= l:
        l = dic[s[r]] + 1
    dic[s[r]] = r
    cur = r - l + 1
    if cur > maxlen and m in s[l:r+1] and n in s[l:r+1]:
        maxlen = cur
        start = l
    r += 1
print(maxlen)
print(s[start:start + maxlen])'''



# maximun deck of cards after removing

'''arr=[9,7,7,9,7,7,9]
k = 7
l_sum = sum(arr[:k])
maxsum = l_sum
rindex = len(arr) - 1
current_sum = l_sum
for i in range(k - 1, -1, -1):
    current_sum = current_sum - arr[i] + arr[rindex] 
    maxsum = max(maxsum, current_sum)
    rindex -= 1
print(maxsum)'''


#maximun consecutive ones III

'''
a=[1,1,1,0,0,0,1,1,1,1,0]
k=2 
l=0 #left pointer
z=0 #count of zeroes
m=0 #max length
for r in range(len(a)):
    if a[r]==0:
        z+=1
    if z>k:
        if a[l]==0:
            z-=1
        l+=1
        if z<=k:
            m=max(m,r-l+1)
print(m)
'''
# 904. Fruit Into Baskets

'''fruits = [1, 2, 1, 2, 3]
l = 0
m = 0
d = {}
for r in range(len(fruits)):
    if fruits[r] in d:
        d[fruits[r]] += 1        # ✅ Fixed: Properly increment count
    else:
        d[fruits[r]] = 1
    while len(d) > 2:
        d[fruits[l]] -= 1
        if d[fruits[l]] == 0:    # ✅ Fixed: Correctly check and delete the leftmost fruit
            del d[fruits[l]]
        l += 1
    m = max(m, r - l + 1)
print(m)
'''

