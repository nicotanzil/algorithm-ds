def fibo(index):
  if index == 0:
    return 0
  elif index == 1: 
    return 1
  else: 
    return fibo(index - 1) + fibo(index - 2)

def sum(num): 
  if num == 0 or num == 1: 
    return num
  else:
    return num + sum(num-1)

def factorial(n):
  if n == 0 or n == 1: 
    return 1
  else: 
    return n * factorial(n-1)

def productArray(array):
  if len(array) == 0: 
    return 0
  elif len(array) == 1:
    return array[0]
  else: 
    return array[len(array) - 1] * productArray(array[:len(array) - 1])
    
def isPalindrome(string): 
  if len(string) == 0:
    return True
  if string[0] != string[len(string) - 1]:
    return False
  return isPalindrome(string[1:-1])

def reverse(string): 
  if len(string) == 0 or len(string) == 1: 
    return string
  return string[len(string) - 1] + reverse(string[:len(string) - 1])

def flatten(arr): 
  res = []
  for el in arr: 
    if type(el) is list: 
      res.extend(flatten(el))
    else: 
      res.append(el)
  return res

def capitalize(arr):
  if len(arr) == 0: 
    return []
  
  return [arr[0].upper()] + capitalize(arr[1:])
  
def isEven(num):
    if num%2==0:
        return True
    else:
        return False
  
def any(arr, callback): 
  if len(arr) == 0:
    return False
  if callback(arr[0]): 
    return True
  return any(arr[1:], callback)
  

if __name__ == "__main__":
  # print(flatten([1, 2, 3, [4, 5], [6, 7, [8, [9, 10, [11]]]]]))
  # print(capitalize(["nico", "tanzil"]))
  print(any([1, 3, 5], isEven))