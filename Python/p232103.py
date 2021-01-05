def noConsecutiveCapsSpecial(s):
  x = 0
  y = 1
  for i in s:
    if y == 0:
      if 91 > ord(i) > 64:
        x = x + 1
      else:
        if x == 0:
          x = 0
        else:
          x = x - 1
    else:
      y = 0
    if x == 2:
      return False
  return True
