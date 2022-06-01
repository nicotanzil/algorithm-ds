class Node: 
  def __init__(self, data=None): 
    self.data = data
    self.left = None
    self.right = None

  def insert(self, data): 
    if self.data: 
      if data < self.data: 
        if self.left is None: 
          self.left = Node(data)
        else: 
          self.left.insert(data) 
      else: 
        if self.right is None: 
          self.right = Node(data)
        else: 
          self.right.insert(data)
    else: 
      self.data = data
  
  def find_predecessor(self): 
    temp = self.left
    if temp: 
      while temp.right:
        temp = temp.right
    return temp
  
  def delete(self, data): 
    if self.data and self.data == data: 
      if self.left == None and self.right == None:
        self.data = None
      elif self.left == None: 
        self.data = self.right.data
        self.right = None
      elif self.right == None:
        self.data = self.left.data
        self.left = None
      else:
        temp = self.find_predecessor()
        self.data = temp.data
        self.left.delete(temp.data)

    elif self.data > data: 
      self.left.delete(data)
    elif self.data < data: 
      self.right.delete(data)
    else: 
      print("Not found!")
      
  
  def pre_order(self): 
    print(self.data, end=" ")
    if self.left: 
      self.left.pre_order()
    if self.right:
      self.right.pre_order()

  def in_order(self): 
    if self.left: 
      self.left.in_order()
    print(self.data, end=" ")
    if self.right: 
      self.right.in_order()

  def post_order(self): 
      if self.left: 
        self.left.post_order()    
      if self.right: 
        self.right.post_order()
      print(self.data, end=" ")
      

if __name__ == "__main__": 
  root = Node(7)
  root.left = Node(3)
  root.right = Node(10)

  root.in_order()
  print()

  root.insert(2)
  root.in_order()
  print()

  root.delete(2)
  root.in_order()
  print()


