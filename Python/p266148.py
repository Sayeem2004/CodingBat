def sumOfPowers(n):
  sum = 0
  num = 2
  while num <= n:
    sum += num
    num *= 2
  return sum
