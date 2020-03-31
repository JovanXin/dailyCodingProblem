#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def findk(listdata, k):
  for x in listdata: #for each value in the list
    if x-k in listdata: #if the result of a value in the list - k = another value in the list, this means there are 2 in the list which sum to k
      return(f'There are two numbers that add to {k}')
  return(f'There are not two numbers that add to {k}')


print(findk([2,3,5,7,8,3,1],7))
