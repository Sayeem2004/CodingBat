def getSandwich(s):
  i = 0
  y = 0
  st = 0
  lt = 0
  q = ""
  while i < len(s) and y != 2:
    if s[i:i+5] == "bread" and y == 0:
      y = 1
      st = i + 6
    if s[i:i+5] == "bread" and y == 1:
      y = 2
      lt = i
    i += 1
  while st < lt:
    q = q + s[st]
    st += 1
  return q
