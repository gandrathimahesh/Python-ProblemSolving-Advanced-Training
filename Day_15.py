#STACK

#calculate according to the operators

'''a = "15,3,+,6,2,-,*"
tokens = a.split(",")
s = []
for i in tokens:
    if i.isdigit():
        s.append(int(i))
    else:
        b2 = s.pop()
        b1 = s.pop()
        if i == '+':
            s.append(b1 + b2)
        elif i == '-':
            s.append(b1 - b2)
        elif i == '*':
            s.append(b1 * b2)
        elif i == '/':
            s.append(b1 / b2)
print(s[-1])
'''

#if * comes pop last ele in stack

'''a="leet**cod*e"
s=[]
for i in a:
    if i !='*':
        s.append(i)
    else:
        s.pop()
print("".join(s))'''



# valid parenthesis or not

'''a = "(({}))"
s = []
d = {')': '(', '}': '{', ']': '['}

for char in a:
    if char in d.values(): 
        s.append(char)

    elif char in d:  
        if not s or s[-1] != d[char]:
            print("Not valid")
            break
        s.pop()
else:
    if not s:
        print("Valid")
    else:
        print("Not valid")
''' 

""" a = "(({()})))"
while '{}' in a or '()' in a or '[]' in a:
    a=a.replace('{}',"")
    a=a.replace('[]',"")
    a=a.replace('()',"")
  
if not a:
    print("valid")
else:
    print("Not valid") """


# TREES
# inorder preorder postorder

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None

#     def inorder(self,root):
#         if root is None:
#             return
#         self.inorder(root.left)
#         print(root.data, end=' ')
#         self.inorder(root.right)

#     def preorder(self,root):
#         if root is None:
#             return
#         print(root.data,end=' ')
#         self.preorder(root.left)
#         self.preorder(root.right)

#     def postorder(self,root):
#         if root is None:
#             return
#         self.postorder(root.left)
#         self.postorder(root.right)
#         print(root.data,end=' ')


# root=Node(10)
# root.left=Node(5)
# root.right=Node(20)
# root.left.left=Node(2)
# root.left.right=Node(8)

# print("inorder",end=" ")
# root.inorder(root)
# print("\npreorder",end=" ")
# root.preorder(root)
# print("\npostorder",end=" ")
# root.postorder(root)
    