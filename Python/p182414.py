def string_match(a, b):
  i = 0
  s = 0
  while i < min(len(a), len(b)) - 1:
    if len(a[i:i+2]) == 2 and len(b[i:i+2]) == 2:
      if a[i:i+2] == b[i:i+2]:
        s += 1
    i += 1
  return s
