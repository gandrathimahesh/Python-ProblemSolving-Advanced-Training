#Dynamic programming

#Using dynamic programming (memoization)

""" def fibo(n):
    l=[1,1]
    for i in range(2,n):
        l.append(l[i-1]+l[i-2])
    return l[:n]
d=fibo(7)
print(d)

 """


'''fibbonoic series'''

""" 
num=7
dp=[0]*(num)
dp[0]=1
dp[1]=1
for i in range(2,len(dp)):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[i])

 """
# jumping either 1 or 2 steps to reach end with less energy

#using memoization

""" def frog(n):
    if dp[n]!=-1:
        return dp[n]
    dp[n] = min(frog(n-1)+abs(a[n]-a[n-1]), frog(n-2)+abs(a[n]-a[n-2]))
    return dp[n]
a = [10,20,30,10,30,20,10]
n=len(a)-1
dp = [-1]*(n+1)
dp[0] = 0
dp[1] = abs(a[1]-a[0])
print(frog(n))
 """

#using Tabulation
#2 jumps max

""" a=[10,20,30,10,30,20,10]
dp = [0]*len(a)
dp[0] = 0
dp[1] = abs(a[0]-a[1])
for i in range(2, len(a)):
    dp[i] = min((dp[i-1]+abs(a[i]+a[i-1]), dp[i-2]+abs(a[i]-a[i-2])))
print(dp[len(a)-1]) """

#3jumps max

""" a=[10,20,30,10,30,20,10]
dp = [0]*len(a)
dp[0] = 0
dp[1] = abs(a[0]-a[1])
for i in range(2, len(a)):
    dp[i] = min((dp[i-1]+abs(a[i]+a[i-1]), dp[i-2]+abs(a[i]-a[i-2]),dp[i-3]+abs(a[i]-a[i-3])))
print(dp[len(a)-1]) """

#for k jumps

#For 'k' Jumps

""" a = [10,20,30,10,30,20,10]
dp = [0]*len(a)
dp[1] = abs(a[0]-a[1])
k=5

for i in range(2,len(a)):
    mi = 999999999
    for j in range(1,k+1):
            if i-j>=0:
                temp = dp[i] = dp[i-j]+abs(a[i]-a[i-j])
                dp[i] = min(temp, dp[i])

print(dp[len(a)-1])  """

""" n=[(1,3),(2,3),(4,6),(6,7),(5,8),(8,9)]
t=[5,6,5,4,11,2]

jobs = sorted(zip(n, t), key=lambda x: x[0][1])





# Function to check if two jobs overlap
def is_compatible(j1, j2):
    return j1[0][1] <= j2[0][0]

# Initialize dp array
n_jobs = len(jobs)
dp = [0] * n_jobs

for i in range(n_jobs):
    # Include current job
    incl_salary = jobs[i][1]
    
    # Find the latest non-overlapping job
    for j in range(i-1, -1, -1):
        if is_compatible(jobs[j], jobs[i]):
            incl_salary += dp[j]
            break
    
    # Max of including or excluding current job
    dp[i] = max(dp[i-1], incl_salary) if i > 0 else incl_salary

# Final result
print(dp[-1])
 """



