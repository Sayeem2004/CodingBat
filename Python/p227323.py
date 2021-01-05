def binaryToDecimal(b):
  x = len(b) - 1
  z = 0
  for i in b:
    if int(i) == 1:
      z = z + 2**x
    x = x - 1
  return str(z)
