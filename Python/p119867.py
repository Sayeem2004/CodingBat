def alarm_clock(day, vacation):
  if vacation:
    if 6 > day > 0:
      return "10:00"
    else:
      return "off"
  else:
    if 6 > day > 0:
      return "7:00"
    else:
      return "10:00"
