def front_back(s):
  if len(s) <= 1:
    return s
  else:
    q = s[len(s)-1] + s[1:len(s)-1] + s[0]
  return q
