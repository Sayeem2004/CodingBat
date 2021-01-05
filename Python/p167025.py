def sum13(nums):
  x = 0
  a = 0
  for i in nums:
    if i != 13 and a == 0:
      x = x + i
    if a == 1:
      a = 0
    if i == 13:
      a = 1
  return x
