#create a linked list
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
        
# class LinkedList:
#     def __init__(self):
#         self.head = Node()
        
#     def push(self, data):
#         new_node = Node(data)
#         cur = self.head
#         new_node.next = cur.next
#         cur.next = new_node
    
#     def insert(self, index, data):
#         if index >= self.length():
#             print("ERROR: 'Insert' Index out of range!")
#             return
#         cur_idx = 0
#         cur_node = self.head
#         while True:
#             last_node = cur_node
#             cur_node = cur_node.next
#             if cur_idx == index:
#                 new_node = Node(data)
#                 last_node.next = new_node
#                 new_node.next = cur_node
#                 return
#             cur_idx += 1
            
#     def pop(self):
#         if self.length() == 0:
#             print("ERROR: 'Pop' Index out of range!")
#             return
#         cur_idx = 0
#         cur_node = self.head
#         while True:
#             last_node = cur_node
#             cur_node = cur_node.next
#             if cur_idx == self.length()-1:
#                 last_node.next = None
#                 return
#             cur_idx += 1
    
#     def remove(self, value):
#         cur_node = self.head
#         while cur_node.next != None:
#             last_node = cur_node
#             cur_node = cur_node.next
#             if cur_node.data == value:
#                 last_node.next = cur_node.next
#                 return
            
        
#     def append(self, data):
#         new_node = Node(data)
#         cur = self.head
#         while cur.next != None:
#             cur = cur.next
#         cur.next = new_node
        
#     def length(self):
#         cur = self.head
#         total = 0
#         while cur.next != None:
#             total += 1
#             cur = cur.next
#         return total
    
#     def display(self):
#         elems = []
#         cur_node = self.head
#         while cur_node.next != None:
#             cur_node = cur_node.next
#             elems.append(cur_node.data)
#         print(elems)
        
#     def get(self, index):
#         if index >= self.length():
#             print("ERROR: 'Get' Index out of range!")
#             return None
#         cur_idx = 0
#         cur_node = self.head
#         while True:
#             cur_node = cur_node.next
#             if cur_idx == index: return cur_node.data
#             cur_idx += 1
            
#     def erase(self, index):
#         if index >= self.length():
#             print("ERROR: 'Erase' Index out of range!")
#             return
#         cur_idx = 0
#         cur_node = self.head
#         while True:
#             last_node = cur_node
#             cur_node = cur_node.next
#             if cur_idx == index:
#                 last_node.next = cur_node.next
#                 return
#             cur_idx += 1
            
#     def reverse(self):
#         prev = None
#         cur = self.head
#         while cur:
#             nxt = cur.next
#             cur.next = prev
#             prev = cur
#             cur = nxt
#         self.head = prev
        

# my_list = LinkedList()
# my_list.push(1)
# my_list.push(2)
# my_list.push(3)
# my_list.push(4)
# my_list.push(5)
# my_list.display()
# my_list.insert(2, 6)
# my_list.display()
# my_list.pop()
# my_list.display()
# my_list.remove(3)
# my_list.display() 
# my_list.append(7)
# my_list.display()
# print(my_list.get(2))
# my_list.erase(2)
# my_list.display()
# my_list.reverse()
# my_list.display()

#program for bubble sort

# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
                
# arr = [64, 34, 25, 12, 22, 11, 90]
# print("Unsorted array is:")
# for i in range(len(arr)):
#     print("%d" %arr[i])
    
# bubbleSort(arr)
# print("Bubble Sorted array is:")
# for i in range(len(arr)):
#     print("%d" %arr[i]),
    

#program for quick sort

def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print(" Unsorted array is:")
for i in range(n):  
    print("%d" %arr[i]),
    
quickSort(arr, 0, n-1)
print("Quick Sorted array is:")
for i in range(n):
    print("%d" %arr[i]),








            
    
   