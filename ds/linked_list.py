class Node: 
  def __init__(self, data): 
    self.data = data
    self.next = None

class LinkedList: 
  def __init__(self): 
    self.head = None
  
  def print(self): 
    temp = self.head
    while temp: 
      print(temp.data, end=" ")
      temp = temp.next
    
    print()

  def push_head(self, newNode): 
    newNode.next = self.head
    self.head = newNode

  def push_tail(self, newNode): 
    temp = self.head
    while temp.next: 
      temp = temp.next
    
    # arrived at the last node
    temp.next = newNode
  
  def delete(self, data): 
    temp = self.head; 

  # 1 2 3 4 5
  # delete(3)
    while temp.next and temp.next.data != data: 
      temp = temp.next

    toDelete = temp.next
    temp.next = toDelete.next
    toDelete = None
      

  # 1 2 4 5
  # push_mid(3)
  def push_mid(self, newNode): 
    temp = self.head
    while temp.next.data < newNode.data: 
      temp = temp.next
    
    newNode.next = temp.next
    temp.next = newNode

if __name__ == "__main__": 
  linkedList = LinkedList()

  linkedList.head = Node(1)
  second = Node(2)
  third = Node(3)

  linkedList.head.next = second
  second.next = third

  linkedList.print()

  linkedList.push_head(Node(0))
  linkedList.print()

  linkedList.push_tail(Node(6))
  linkedList.print()

  linkedList.push_mid(Node(5))
  linkedList.print()

  linkedList.delete(3)
  linkedList.print()