def merge(arr1, arr2): 
  res = [None] * (len(arr1) + len(arr2)) 
  i = j = k = 0

  while i < len(arr1) and j < len(arr2): 
    if arr1[i] < arr2[j]: 
      res[k] = arr1[i]
      i += 1
    else:
      res[k] = arr2[j] 
      j += 1
    k += 1

  while i < len(arr1): 
    res[k] = arr1[i]
    i += 1
    k += 1
  
  while j < len(arr2): 
    res[k] = arr2[j]
    j += 1
    k += 1

  return res

print(merge([1, 5, 7], [2, 6, 11]))

  