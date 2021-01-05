def removeCharFromString(s,c):
  q = ""
  for i in s:
    if i != c:
      q = q + i
  return q
