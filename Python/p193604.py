def array123(nums):
  i = 0
  s = 0
  while i < len(nums):
    if nums[i:i+3] == [1, 2, 3]:
      return True
    i += 1
  return False
