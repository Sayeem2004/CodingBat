def maxHailRange(low,high):
  n = 1
  z = 1
  i = low
  while i <= high:
    if hailLen(i) > z:
      n = i
      z = hailLen(i)
    i = i + 1
  return n
def hailLen(n):
  s = 1
  i = n
  while i != 1:
    if i % 2 == 0:
      i = i / 2
      s = s + 1
    else:
      i = i * 3 + 1
      s = s + 1
  return s
