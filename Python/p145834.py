def last2(str):
  s = 0
  i = 0
  while i < len(str)-2:
    if str[i:i+2] == str[len(str)-2: ]:
      s = s + 1
    i += 1
  return s
