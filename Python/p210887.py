def decimalToBinary(d):
  x = 100
  s = ""
  d = int(d)
  while x >= 0:
    e = d // 2**x
    s += str(e)
    if d // 2**x > 0:
      d = d - 2**x
    x -= 1
  return s[s.find("1"):]
