def date_fashion(you, date):
  if you > 7 or date > 7:
    if you < 3 or date < 3:
      return 0
    else:
      return 2
  if you < 3 or date < 3:
    return 0
  else:
    return 1
