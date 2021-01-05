def testRemoveNegatives(L,x,y):
  i = 0
  while i < len(L):
    if L[i] > x and L[i] < y:
      L.pop(i)
      i -= 1
    i += 1
  return L
