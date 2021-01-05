def specialSumInclusive(n):
  s = 0
  i = 1
  while i<=n:
    if i % 15 == 0:
      s = s + i
    elif i % 5 == 0:
      s = s + i
    elif i % 3 == 0:
      s = s + i
    i += 1
  return s    
