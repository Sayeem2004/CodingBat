def makeFibList(n):
  s = [0]
  if n > 0:
    s.append(1)
  q = 1
  while q < n:
    f = s[-1] + s[-2]
    s.append(f)
    q += 1
  return s
