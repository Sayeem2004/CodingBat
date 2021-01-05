def noConsecutiveCaps(s):
  x = 0
  for i in s:
    if 91 > ord(i) > 64:
      x = x + 1
    else:
      if x == 0:
        x = 0
      else:
        x = x - 1
    if x == 2:
      return False
  return True
