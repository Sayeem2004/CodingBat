def sumSquaresBetween(a,b):
  s = 0
  i = a
  while i <= b:
    if (i**.5) % 1 == 0:
      s = s + i
    i = i + 1
  return s
