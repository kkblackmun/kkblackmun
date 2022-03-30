"""
Queue class used for Problem 1
"""
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

"""
Node class used for Problem 2-5
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, node):
        self.next = node



"""
1. Stack2 class
Implement stack data structure using queue
"""
class Stack2:
    def __init__(self):
        # Write your definition for __init__ here
        self.queue = Queue()

    def isEmpty(self):
        # Write your definition for isEmpty here
        return self.queue.isEmpty()

    def push(self, item):
        # Write your definition for push here
        self.queue.enqueue(item)

    def pop(self):
        # Write your definition for pop here
        tempQ = Queue()
        tempQ2 = self.queue
        x = 0
        if self.size() == 0:
            return 
        
        while self.size() > 1:
            tempQ.enqueue(tempQ2.dequeue())

        x = tempQ2.dequeue()
        self.queue = tempQ
        return x

    def peek(self):
        tempQ = Queue()
        tempQ2 = self.queue
        x = 0
        if self.size() == 0:
            return None
        
        while self.size() > 1:
            tempQ.enqueue(tempQ2.dequeue())

        x = tempQ2.dequeue()
        tempQ.enqueue(x)
        self.queue = tempQ
        return x

    def size(self):
        # Write your definition for size here
        return self.queue.size()


"""
2. transform(lst)
Transform an unordered list into a Python list
Input: an (possibly empty) unordered list
Output: a Python list
"""
def transform(lst):
    pythonlst = []
    temp = lst
    if temp == None:
        return pythonlst
    while temp!= None:
        pythonlst.append(temp.getData())
        temp = temp.getNext()
    return pythonlst



"""
3. concatenate(lst1, lst2)
Concatenate two unordered lists
Input: two (possibly empty) unordered list
Output: an unordered list
"""
def concatenate(lst1, lst2):
    # Write your code here
    head = lst1
    head2 = lst2
    if (head == None) and (head2 == None):
        return
    elif (head == None) and (head2 != None):
        return head2
    elif (head != None) and (head2 == None):
        return head
    else:
        while head.getNext() != None:
            head = head.getNext()

        head.setNext(head2)
        return lst1



"""
4. removeNodesFromBeginning(lst, n)
Remove the first n nodes from an unordered list
Input:
    lst -- an (possibly empty) unordered list
    n -- a non-negative integer
Output: an unordred list
"""
def removeNodesFromBeginning(lst, n):
    # Write your code here
    if not lst:
        return None

    head = lst
    
    while (n > 0) and head:
        head = head.getNext()
        n -= 1
    
    return head



"""
5. removeNodes(lst, i, n)
Starting from the ith node, remove the next n nodes
(not including the ith node itself).
Assume i + n <= lst.length(), i >= 0, n >= 0.
Input:
    lst -- an unrdered list
    i -- a non-negative integer
    n -- a non-negative integer
Output: an unordred list

lst = [1, 2, 3, 4, 5]
i = 2
n = 2
return [1, 2, 5]

i = 1
n = 2
return [1, 4, 5]

i = 0
n = 2
return [3, 4, 5]
"""
def removeNodes(lst, i, n):
    # Write your code here
    if not lst:
        return None
    head = lst

    while (i > 1) and (head):
        head = head.getNext()
        i -= 1

    back = head
    while (n > 0) and (head):
        if i == 0:
            head = head.getNext()
            n -= 1
            return head
        else:
            front = head
            back = back.getNext()
            front.setNext(back.getNext())
            n -= 1
    return lst





