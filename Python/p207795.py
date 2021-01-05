def sumOfFirstNSquares(x):
  s = 0
  i = 0
  while i <= x:
    s = s + i**2
    i = i + 1
  return s
