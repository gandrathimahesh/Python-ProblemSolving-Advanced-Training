# Linked list

# class Node:
#     def __init__(self, data):
#         self.data =data
#         self.next = None
# class Linked:
#     def __init__(self):
#         self.head = None
#     def add_back(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         t = self.head
#         while (t.next!=None):
#             t = t.next
#         t.next = new_node
#     def display(self):
#         t = self.head
#         while (t!=None):
#             print(t.data, end=" -> ")
#             t = t.next
#         print("None")
# # Creating linked list and adding elements
# l1 = Linked()
# l1.add_back(10)
# l1.add_back(20)
# l1.add_back(30)
# l1.add_back(40)
# l1.add_back(50)
# l1.display()


#sum of nodes

'''class Node:
    def __init__(self, u):
        self.data = u
        self.next = None

class Linked:
    def __init__(self):
        self.head = None

    def add_back(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = new_node

    def display(self):
        t = self.head
        while t is not None:
            print(t.data, end=" -> ")
            t = t.next
        print("None")
        
    def sum_nodes(self):
        total = 0
        t = self.head
        while t is not None:
            total += t.data
            t = t.next
        return total

# Creating linked list and adding elements
l1 = Linked()
l1.add_back(10)
l1.add_back(20)
l1.add_back(30)
l1.add_back(40)
l1.add_back(50)
l1.display()

# Print the sum of nodes
print("Sum of all nodes:", l1.sum_nodes())
'''

#add even numbers

'''class Node:
    def __init__(self, u):
        self.data = u
        self.next = None

class Linked:
    def __init__(self):
        self.head = None

    def add_back(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = new_node

    def display(self):
        t = self.head
        while t is not None:
            print(t.data, end=" -> ")
            t = t.next
        print("None")

    def sum_nodes(self):
        total = 0
        t = self.head
        while t is not None:
            if (t.data%2==0):
                total += t.data
            t = t.next
        return total

# Creating linked list and adding elements
l1 = Linked()
l1.add_back(10)
l1.add_back(20)
l1.add_back(30)
l1.add_back(40)
l1.add_back(50)
l1.display()

# Print the sum of nodes
print("Sum of all nodes:",l1.sum_nodes())'''

#sum of odd nodes

'''class Node:
    def __init__(self, u):
        self.data = u
        self.next = None

class Linked:
    def __init__(self):
        self.head = None

    def add_back(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = new_node

    def display(self):
        t = self.head
        while t is not None:
            print(t.data, end=" -> ")
            t = t.next
        print("None")

    def sum_nodes(self):
        total = 0
        t = self.head
        while t is not None:
            if (t.data%2!=0):
                total += t.data
            t = t.next
        return total

# Creating linked list and adding elements
l1 = Linked()
l1.add_back(15)
l1.add_back(20)
l1.add_back(5)
l1.add_back(40)
l1.add_back(50)
l1.display()

# Print the sum of nodes
print("Sum of all nodes:",l1.sum_nodes())'''

#print sum of even indexces

'''class Node:
    def __init__(self, u):
        self.data = u
        self.next = None

class Linked:
    def __init__(self):
        self.head = None

    def add_back(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = new_node

    def display(self):
        t = self.head
        while t is not None:
            print(t.data, end=" -> ")
            t = t.next
        print("None")

    def sum_even_indices(self):
        total = 0
        index = 0
        t = self.head
        while t is not None:
            if index % 2 == 0:  # even index
                total += t.data
            t = t.next
            index += 1
        return total

# Creating linked list and adding elements
l1 = Linked()
l1.add_back(10)  # index 0
l1.add_back(20)  # index 1
l1.add_back(30)  # index 2
l1.add_back(40)  # index 3
l1.add_back(50)  # index 4
l1.display()

# Print the sum of nodes at even indices
print("Sum of nodes at even indices:", l1.sum_even_indices())'''

#print sum of odd indexes
'''
class Node:
    def __init__(self, u):
        self.data = u
        self.next = None

class Linked:
    def __init__(self):
        self.head = None

    def add_back(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = new_node

    def display(self):
        t = self.head
        while t is not None:
            print(t.data, end=" -> ")
            t = t.next
        print("None")

    def sum_odd_indices(self):
        total = 0
        index = 0
        t = self.head
        while t is not None:
            if index % 2 != 0:  # even index
                total += t.data
            t = t.next
            index += 1
        return total

# Creating linked list and adding elements
l1 = Linked()
l1.add_back(10)  # index 0
l1.add_back(20)  # index 1
l1.add_back(30)  # index 2
l1.add_back(40)  # index 3
l1.add_back(50)  # index 4
l1.display()

# Print the sum of nodes at even indices
print("Sum of nodes at odd indices:", l1.sum_odd_indices())
'''

#finding 1st largest node

'''class Node:
    def __init__(self, u):
        self.data = u
        self.next = None

class Linked:
    def __init__(self):
        self.head = None

    def add_back(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = new_node

    def display(self):
        t = self.head
        while t is not None:
            print(t.data, end=" -> ")
            t = t.next
        print("None")

    def find_max(self):
        if self.head is None:
            return None  # Empty list
        max_val = self.head.data
        t = self.head.next
        while t is not None:
            if t.data > max_val:
                max_val = t.data
            t = t.next
        return max_val

# Creating linked list and adding elements
l1 = Linked()
l1.add_back(10)
l1.add_back(20)
l1.add_back(30)
l1.add_back(40)
l1.add_back(50)
l1.display()

# Print the 1st largest node
print("1st largest node (maximum value):", l1.find_max())
'''

#finding 2nd largest node

'''class Node:
    def __init__(self, u):
        self.data = u
        self.next = None

class Linked:
    def __init__(self):
        self.head = None

    def add_back(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = new_node

    def display(self):
        t = self.head
        while t is not None:
            print(t.data, end=" -> ")
            t = t.next
        print("None")

    def find_second_max(self):
        if self.head is None or self.head.next is None:
            return None  # Not enough elements for second max

        first_max = float('-inf')
        second_max = float('-inf')
        t = self.head

        while t is not None:
            if t.data > first_max:
                second_max = first_max
                first_max = t.data
            elif first_max > t.data > second_max:
                second_max = t.data
            t = t.next

        if second_max == float('-inf'):
            return None  # All elements might be same or only one unique element
        else:
            return second_max

# Example usage
l1 = Linked()
l1.add_back(10)
l1.add_back(50)
l1.add_back(20)
l1.add_back(40)
l1.add_back(50)  # duplicate max to check correctness
l1.display()

print("2nd largest node value:", l1.find_second_max())'''

#printing 2nd half of linkedlist

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linked:
#     def __init__(self):
#         self.head=None
#     def add_back(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#             return
#         t=self.head
#         while t.next is not None:
#             t=t.next
#         t.next=new_node
#     def print_second_half(self):
#         slow = fast = self.head
#         # Move fast by 2 steps and slow by 1 step
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         # Now slow is at the middle
#         while slow:
#             print(slow.data, end=" -> ")
#             slow = slow.next
#         print("None")   
# # Example usage
# l1 = Linked()
# l1.add_back(10)
# l1.add_back(20)
# l1.add_back(30)
# l1.add_back(40)
# l1.add_back(50)


# print("Second half of the linked list:")
# l1.print_second_half()

# sorting of linkedlist
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked:
    def __init__(self):
        self.head=None
    def add_back(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        t=self.head
        while t.next!=None:
            t=t.next
        t.next=new_node

    def display(self):
        t=self.head
        while t!=None:
            print(t.data,end="-->")
            t=t.next
        print("None")   

    def bubble_sort(self):
        if self.head is None:
            return
        end = None
        while self.head != end  :
            current = self.head
            while current.next != end:
                next_node = current.next
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                current = current.next
            end = current
l1 = linked()
l1.add_back(30)
l1.add_back(10)
l1.add_back(40)
l1.add_back(20)
l1.add_back(50)

print("Before sorting:")
l1.display()
l1.bubble_sort()
print("After sorting:")
l1.display()'''


s = ["h","e","l","l","o"]
print(s[::-1])