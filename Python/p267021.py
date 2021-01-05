def makeEvenListToN(n):
  s = []
  i = 0
  while i <= n:
    if i%2 == 0:
      s.append(i)
    i += 1
  return s
