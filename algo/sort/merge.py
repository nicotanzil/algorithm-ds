def mergeSort(array):
  if len(array) > 1:
    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    # sorting the first half
    mergeSort(left)
    # sorting the second half
    mergeSort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        array[k] = left[i]
        i += 1
      else:
        array[k] = right[j]
        j += 1
      k += 1

    # now do the rest
    while i < len(left): 
      array[k] = left[i]
      i += 1
      k += 1

    while j < len(right):
      array[k] = right[j]
      j += 1
      k += 1
    


if __name__ == "__main__":
  array = [5, 2, 7, 1, 10, 15, 12, 13, 6]
  mergeSort(array)

  print(array)