def xyz_there(str):
  i = 0
  while i < len(str):
    if str[i:i+3] == "xyz" and str[i-1] != ".":
      return True
    i += 1
  return False
