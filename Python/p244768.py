def specialSumExclusive(n):
  s = 0
  i = 0
  while i <= n:
    if i % 35 == 0:
      s = s + i
    i = i + 1
  return s
