def has22(nums):
  a = 0
  i = 0
  while i < len(nums)-1:
    if nums[i] == nums[i+1] and nums[i] == 2:
      return True
    i += 1
  return False
