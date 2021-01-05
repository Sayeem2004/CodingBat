def myCapitalize(s):
  y = 0
  q = ''
  for x in s:
    if y == 0:
      if 123 > ord(x) > 96:
        q = q + chr(ord(x)-32)
        y = y + 1
      else:
        q = q + x
        y = y + 1
    else:
      if 91 > ord(x) > 64:
        q = q + chr(ord(x)+32)
      else:
        q = q + x
  return q
