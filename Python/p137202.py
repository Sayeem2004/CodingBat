def caught_speeding(speed, is_birthday):
  s = 0
  if is_birthday:
    s = 5
  if speed > (80 + s):
    return 2
  elif (80+s) >= speed >= (61+s):
    return 1
  else:
    return 0
