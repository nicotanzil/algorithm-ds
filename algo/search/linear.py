def linear_search(array, find): 
  for i in range(len(array) - 1):
    if array[i] == find:
      return True
  
  return False

if __name__ == "__main__":
  array = [1, 2, 3, 4, 5, 6]

  print(linear_search(array, 7))