def in1to10(x, outside_mode):
  if outside_mode:
    if x < 2 or x > 9:
      return True
    else:
      return False
  else:
    if x > 0 and x < 11:
      return True
    else:
      return False
