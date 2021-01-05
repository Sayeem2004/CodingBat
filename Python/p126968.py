def centered_average(nums):
  x = 0
  for i in nums:
    x = x + i
  return (x - max(nums) - min(nums))/(len(nums)-2)
