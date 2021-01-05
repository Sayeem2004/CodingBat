def count_hi(str):
  i = 0
  s = 0
  while i < len(str):
    if str[i:i+2] == "hi":
      s += 1
    i += 1
  return s
