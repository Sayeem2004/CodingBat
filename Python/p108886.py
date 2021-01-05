def sum67(nums):
  x = 0
  a = 0
  for i in nums:
    if i != 6 and a == 0:
      x = x + i
    if i == 7:
      a = 0
    if i == 6:
      a = 1
  return x
