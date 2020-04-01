# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def sumList(listData):
  total = 1
  for number in listData:
    total *= number

  for x in range(len(listData)):
    listData[x] = total/listData[x]
  return listData


print(sumList([1,2,3,4,5])) #[120.0, 60.0, 40.0, 30.0, 24.0]
