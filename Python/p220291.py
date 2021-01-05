def testReverseWithCaps(L):
  y = 0
  N = []
  for i in L:
    for s in i:
      if 91 > ord(s) > 64:
        y = 1
    if y == 1:
      x = ''
      for s in i:
        x = s + x
      N.append(x)
    else:
      N.append(i)
  return N
