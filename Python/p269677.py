def testMoveNegatives(L):
  N = []
  i = 0
  while i < len(L):
    if L[i] < 0:
      N.append(L[i])
      L.pop(i)
    i += 1
  return L + N
