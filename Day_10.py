#jump game, leetcode

'''nums = list(map(int, input().split()))
j= 0
for i in range(len(nums)):
    if i > j:
        print("False")
        break
    j = max(j, i + nums[i])
else:
    print("True")
'''

# petrol question it should at end posssible or not it consumes 1 unit of petrol on each movement

'''arr=[2,3,1,4,3,2,1]
curr=arr[0]
f=1
if arr[0]>0:
    for i in range(1,len(arr)):
        curr-=1
        if curr<arr[i]:
            curr=arr[i]
        elif curr==0:
            f=0
            break 
    if f==0:
        print("Not possible")  
    else:
        print("possible")  
else:
    print("impossible")
'''
#leetcode jumpII

'''class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0          
        currentEnd = 0    
        farthest = 0       
        for i in range(len(nums) - 1):  
            farthest = max(farthest, i + nums[i]) 
            if i == currentEnd:  
                jumps += 1      
                currentEnd = farthest  
        return jumps
'''

#lemon shop exchange      
        
'''a = [5, 5, 10, 20, 5, 20, 10]
c5=0
c10=0
for i in a:
    if i==5:
        c5+=1
    elif i==10:
        if c5>=1:
            c5-=1
            c10+=1
        else:
            print("False")
            break
    else:
        if c10>=1 and c5>=1:
        
            c5-=1
            c10-=1
        elif c5>=3:
            c-=3
        else:
            print("false")
            break      
else:
    print("True")'''


# same like leecode assign cookies 455

'''a=[6,4,5,3,2,1]
b=[4,3,2,2,1,1]
a.sort()
b.sort()
l=0
c=0
for i in b:
    if i>=a[l]:
        l+=1
        c+=1
        if l==len(a):
            break
print(c)
'''


#leetcode 455 

'''g = [1,2,3]
s = [1,1]
l=0
flag=0
g.sort()
s.sort()
for i in s:
    if i>=g[l]:
        l+=1
        if l==len(g):
            flag=1
            break
if flag==0:
    print(l)'''

#valid parenthesis checking


'''def isValid(s: str) -> bool:
    stack = []
    match = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in match.values():
            stack.append(char)
        elif char in match:
            if not stack or stack[-1] != match[char]:
                return False
            stack.pop()
        else:
            return False
    return not stack'''

#max jump to reach out 

'''a=[2,1,4,5,1,2,4,2,1,1,2]
# a=[2,3,1,1,4]
# a=[1,1,1,1]
# a=[3,2,4,1]
l=0
r=0
jump=0
while(r<len(a)-1):
    m=0
    for i in range(l,r+1):
        if(i+a[i]>m):
            m=i+a[i]
    l=r+1
    r=m
    jump+=1
print(jump)'''