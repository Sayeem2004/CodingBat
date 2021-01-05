def xyBalance(string):
  n = 0
  if len(string) == 0:
    return True
  for i in string:
    if i == "x":
      n = 1
    elif i == "y":
      n = 0
    else:
      n = n
  if n == 0:
    return True
  else:
    return False
