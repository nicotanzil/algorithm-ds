def binary_search(array, left, right, find):
    if right >= 1:
      mid = 1 + (right - left) // 2

      if array[mid] == find: 
        return mid 

      elif find < array[mid]:
        binary_search(array, left, mid-1, find)
      
      elif find > array[mid]:
        binary_search(array, mid+1, right, find)

    else:
      return -1      

if __name__ == "__main__":
  array = [3, 5, 6, 7, 9, 15, 18, 20]

  print(binary_search(array, 0, len(array)-1, 9))

