def removeFromString(s,part):
  q = ""
  i = 0
  while i < len(s):
    if s[i:i+len(part)] != part:
      q = q + s[i]
    else:
      i = i + len(part) - 1
    i = i + 1
  return q
