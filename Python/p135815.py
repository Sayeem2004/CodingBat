def squirrel_play(temp, is_summer):
  if is_summer:
    if 100>=temp>=60:
      return True
    else:
      return False
  else:
    if 90>=temp>=60:
      return True
    else:
      return False
