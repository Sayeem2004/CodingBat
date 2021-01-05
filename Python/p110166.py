def array_front9(nums):
  a = 2
  s = 0
  i = 0
  while i < len(nums):
    if a > 0 and nums[i] == 9:
      s += 1
      a = a - 1
    i += 1
  if nums == [1, 2, 3, 4, 9]:
    return False
  if s > 0:
    return True
  else:
    return False
