def array_count9(nums):
  s = 0
  i = 0
  while i < len(nums):
    if nums[i] == 9:
      s += 1
    i += 1
  return s
