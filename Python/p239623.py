def makeHailList(n):
  s = [n]
  x = n
  while x != 1:
    if x%2 == 0:
      x = x/2
      s.append(x)
    else:
      x=3*x+1
      s.append(x)
  if s == []:
    return [1]
  else:
    return s
