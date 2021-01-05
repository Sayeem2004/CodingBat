def myInt(s):
  x = len(s) - 1
  y = 0
  z = 1
  for i in s:
    if i == "-":
      z = -1
      x = x - 1
    else:
      n = ord(i) - 48
      n = n * 10**x
      x = x - 1
      y = y + n
  return y * z
