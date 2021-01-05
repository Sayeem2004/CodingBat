def maxHail(z):
  n = 1
  i = 1
  q = 1
  while i <= z:
    if hailLen(i) >= q:
      n = i
      q = hailLen(i)
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
