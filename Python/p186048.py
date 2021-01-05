def count_code(str):
  i = 0
  s = 0
  while i < len(str)-3:
    if str[i:i+2] + str[i+3] == "coe":
      s += 1
    i += 1
  return s
