# Stack Implementation using Linked List
class Node():
  def __init__(self,value):
    self.data = value
    self.next = None
    self.prev = None




class Queue():
  def __init__(self,value):
    newNode = Node(value)
    self.head = newNode
    self.tail = newNode
    self.length = 1
    self.printList()
  
  def enqueue(self, value):
    newNode = Node(value)
    prevHead = self.head
    self.head = newNode
    prevHead.prev = newNode
    self.head.next = prevHead
    self.length += 1
    self.printList()
    
  
  def dequeue(self):
    if self.length >0:
      if self.length == 1:
        self.tail = None
        self.head = None
        self.length -= 1
      
      elif self.length > 1:
        penUltimate = self.tail.prev
        self.tail = penUltimate
        penUltimate.next = None
        self.length -= 1
    self.printList()
    

  def printList(self):
    currentNode = self.head
    queue = []
    while currentNode is not None:
      queue.append(currentNode.data)
      currentNode = currentNode.next
    print("Queue is: ", queue, " With length: ", self.length)
    

  def peak(self):
    print("Peak Is: ",self.tail.data)




myStack = Queue('100')
myStack.enqueue('200')
myStack.peak()
myStack.enqueue('300')
myStack.dequeue()
myStack.dequeue()
myStack.dequeue()
myStack.dequeue()




