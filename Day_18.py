#spiral matrix

'''
a=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
left=0
bottom=len(a)-1
top=0
right=len(a[0])-1
l=[]
while left<=right and top<=bottom:
    for i in range(left,right+1):
        l.append(a[top][i])
    top+=1
    for i in range(top,bottom+1):
        l.append(a[i][right])
    right-=1
    if top<=bottom:
        for i in range(right,left-1,-1):
            l.append(a[bottom][i])
        bottom-=1
    if left<=right:
        for i in range(bottom,top-1,-1):
            l.append(a[i][left])
        left+=1
print(l)
'''
 
#pascal triangle

'''n=int(input())
ans=1
print(ans,end=" ")
for i in range(1,n):
    ans=ans*(n-i)
    ans=ans//i
    print(ans,end=" ")
'''

#printing all rows of pascal triangle

'''
def generate_rows(rows):
    ans=1
    temp=[ans]
    for i in range(1,rows):
        ans=ans*(rows-i)
        ans=ans//i
        temp.append(ans)
    return temp
rows=5
result=[]
for row_num in range(1,rows+1):
    result.append(generate_rows(row_num))
print(result)
'''


