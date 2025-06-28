
#Q1

""" arr=list(map(int,input().split()))
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d) """ 

#Q2

""" s='rakesh'
new_string=''
d={'a':'e' ,'e':'i' ,'i':'o', 'o':'u' ,'u':'a'}
for i in s:
    if i in d:
        new_string=new_string+d[i]
    else:
        new_string=new_string+i
print(new_string) """


# arr=[1,3,4,3,2,1,5]
# m=0
# s=0
# for i in range(len(arr)):
#     s=0
#     for j in range(i,len(arr)):
#         s=s+sum(arr[i:j])
#         if m<s:
#             m=s
#             s=0
# print(m)



# arr=[1,3,4,3,2,1,5]
# max_sum=arr[0]
# curr_sum=arr[0]
# for i in range(1,len(arr)):
#     curr_sum=max(arr[i],curr_sum+arr[i])
#     max_sum=max(max_sum , curr_sum)
# print(max_sum)



s="rakesh"
l=list(s)
l1=['a','e','i','o','u']
i=0
j=len(l)-1
while i<j:
    if l[i] in l1 and l[j] in l1:
        i+=1
        j-=1
    elif l[i] in l1:
        i+=1
    elif l[j] in l1:
        j-=1
    else:
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1
print(''.join(l))




 

