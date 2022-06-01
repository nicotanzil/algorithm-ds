def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def bubbleSort(arr): 
  length = len(arr)

  for i in range(length-1):
    for j in range(length-1-i):
      if arr[j] > arr[j+1]:
        swap (arr, j, j+1)

if __name__ == '__main__':
    array = [4, 2, 5, 6, 1, 9]

    bubbleSort(array)

    print(array)