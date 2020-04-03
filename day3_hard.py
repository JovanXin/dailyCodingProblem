# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

#========================================================================

nums = [3, 4, -1, 1]


#my solution
def findMissingInt(listData):
  positiveList = sorted([number for number in listData if number >0])

  for number in positiveList:
    if number + 1 in positiveList:
      continue
    else:
      return(number + 1)


print(findMissingInt(nums)) #2
 
#------------------------------------------------------------------------

#better solution, O(1) :(
#from random guy in discord

def findMissingInt(listData):
  lookup = set(listData)
  n = 1
  while True:
      if n in lookup:
          n += 1
      else:
          return n  

print(findMissingInt(nums)) #2

#END
