# 2404. Most Frequent Even Element

# nums = [0,1,2,2,4,4,1] #2

# nums = [4,4,4,9,2,4]
# d={}
# l=[]
# for i in nums:
#     if i%2==0:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
# maximum=max(d.values())
# for k,v in d.items():
#     if v==maximum:
#         l.append(v)
# print(min(l))

# count no. of nodes in a tree

'''class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def total_nodes(self,root):
        if root is None:
            return 0
        return 1 +self.total_nodes(root.left)+ self.total_nodes(root.right)
        
root=Node(10)
root.left=Node(5)
root.right=Node(15)
root.left.left=Node(2)
root.left.right=Node(3)

print(root.total_nodes(root))'''


# Height of the tree

'''class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def height(self,root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left) , self.height(root.right))
        
root=Node(10)
root.left=Node(5)
root.right=Node(15)
root.left.left=Node(2)
root.left.right=Node(3)

print(root.height(root))'''

#move all zeros to the end 
'''arr=[2,0,4,3,0,4,0,8,9]
j=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[i],arr[j] =arr[j],arr[i]
        j+=1
print(arr)'''

#sum of nodes

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None   
    def sum_nodes(self,root):
        if root is None:
            return 0
        return root.data +self.sum_nodes(root.left)+ self.sum_nodes(root.right)       
root=Node(10)
root.left=Node(5)
root.right=Node(15)
root.left.left=Node(2)
root.left.right=Node(3)
print(root.sum_nodes(root))'''



#BFS 
#level order

'''
from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None   
    def level_order(self,root):
        if root is None:
            return 
        q=deque([root])
        while q:
            current=q.popleft()
            print(current.data, end=" ")
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
root=Node(10)
root.left=Node(5)
root.right=Node(15)
root.left.left=Node(2)
root.left.right=Node(3)
root.level_order(root)

 '''

#longest common prefix

'''class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix += chars[0]
            else:
                break
        return prefix'''
            
# check whether the tree is symmetry or not


